# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This module contains the SDK general utilities.
"""
import os
import platform
import re
import subprocess
import urllib2

from ucsexception import UcsWarning, UcsValidationException

AFFIRMATIVE_LIST = ['true', 'True', 'TRUE', True, 'yes', 'Yes', 'YES']

reserved_keywords = [
    "and", "as", "assert", "break", "class", "continue", "def", "del", "elif",
    "else",
    "except", "exec", "finally", "for", "from", "global", "if", "import", "in",
    "is", "lambda", "not", "or", "pass", "print", "raise", "return", "try",
    "while", "with", "yield"
]


def is_python_reserved(word):
    return word in reserved_keywords


def to_safe_prop(word):
    return ('r_' + word if is_python_reserved(word) else word)


def from_safe_prop(word):
    return (re.sub("^r_", "", word))


def to_python_propname(word):
    return re.sub('_+', '_',
                  re.sub('^_', '',
                    re.sub('[/\-: +]', '_',
                      re.sub('([A-Z]+)([A-Z])([a-z0-9])', '\g<1>_\g<2>\g<3>',
                        re.sub('([a-z0-9])([A-Z])', '\g<1>_\g<2>',(word,
                          to_safe_prop(word))[is_python_reserved(word)])
                             )))).lower()


class Progress(object):
    """Internal class to show the progress of upload/download file."""

    def __init__(self):
        self._seen = 0.0

    def update(self, total, size, name):
        """Internal method to show the progress of upload/download file."""
        from sys import stdout

        self._seen += size
        status = r"%10d  [%3.2f%%]" % (self._seen, self._seen * 100 / total)
        status = status + chr(8) * (len(status) + 1)
        stdout.write("\r%s" % status)
        stdout.flush()


class FileWithCallback(file):
    """Internal class to support external utilities."""

    def __init__(self, path, mode, callback, *args):
        file.__init__(self, path, mode)
        self.seek(0, 2)
        self._total = self.tell()
        self.seek(0)
        self._callback = callback
        self._args = args

    def __len__(self):
        return self._total

    def read(self, size):
        data = file.read(self, size)
        self._callback(self._total, len(data), *self._args)
        return data


def word_l(word):
    """ Method makes the first letter of the given string as lower case. """
    return word[0].lower() + word[1:]


def word_u(word):
    """ Method makes the first letter of the given string as capital. """
    return word[0].upper() + word[1:]


def make_dn(rn_array):
    """ Method forms Dn out of array of rns. """
    return '/'.join(rn_array)


def check_registry_key(java_key):
    """ Method checks for the java in the registry entries. """
    from _winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey, \
        QueryValueEx

    path = None
    try:
        a_reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        r_key = OpenKey(a_reg, java_key)
        for i_cnt in range(1024):
            current_version = QueryValueEx(r_key, "CurrentVersion")
            if current_version is not None:
                key = OpenKey(r_key, current_version[0])
                if key is not None:
                    path = QueryValueEx(key, "JavaHome")
                    return path[0]
    except Exception:
        UcsWarning("Not able to access registry.")
        return None


def is_binary_in_path(path, binary):
    """
    Checks if the given binary is available in the specified path.

    Return:
        True or False (Boolean)
    """
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    path = path.strip('"')
    exe_file = os.path.join(path, binary)
    if is_exe(exe_file):
        return True
    return False


def get_binary_path(binary):
    """
    Checks the environment PATH variable for the specified binary file.
    If found, it returns the path in which it was found.

    Example usage:
        path = get_binary_path('javaws')
    """
    import os

    fpath, fname = os.path.split(binary)
    if fpath:
        raise UcsValidationException("Expects only binary name, not Path.")
    for path in os.environ["PATH"].split(os.pathsep):
        if is_binary_in_path(path, fname):
            return path
    return None


def get_java_installation_path():
    """ Method returns the java installation path in the windows or
    Linux environment. """
    # Get JavaPath for Ubuntu
    # if os.name == "posix":
    if platform.system() in ["Linux", "Darwin"]:
        path = os.environ.get('JAVA_HOME')
        # is javaws in $JAVA_HOME?
        if path and is_binary_in_path(path, 'javaws'):
            return path + '/' + 'javaws'

        # is javaws available in system path?
        path = get_binary_path('javaws')
        if path:
            return path + '/' + 'javaws'

        # javaws was not found
        raise UcsValidationException(
            "Please make sure JAVA is installed and variable JAVA_HOME"
            "is set properly.")

    # Get JavaPath for Windows
    # elif os.name == "nt":
    elif platform.system() == "Windows" or platform.system() == "Microsoft":

        path = os.environ.get('JAVA_HOME')

        if path is None:
            path = check_registry_key(
                r"SOFTWARE\\JavaSoft\\Java Runtime Environment\\")

        if path is None:  # Check for 32 bit Java on 64 bit machine.
            path = check_registry_key(
                r"SOFTWARE\\Wow6432Node\\JavaSoft\\Java Runtime Environment")

        if not path:
            raise UcsValidationException("Please make sure JAVA is installed.")
        else:
            path = os.path.join(path, 'bin')
            path = os.path.join(path, 'javaws.exe')
            if not os.path.exists(path):
                raise UcsValidationException(
                    "javaws.exe is not installed on System at path <%s>." % (
                        path))
            else:
                return path


def check_output(*popenargs, **kwargs):
    """Internal method to handle upload/download data from server."""
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    ret_code = process.poll()
    if ret_code:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(ret_code, cmd, output=output)
    return output


def get_java_version():
    """Method to get java version."""
    try:
        subprocess.check_output
    except Exception:
        subprocess.check_output = check_output

    java_ver_full_str = subprocess.check_output(["java", "-version"],
                                                stderr=subprocess.STDOUT)
    java_ver_match = re.match(r'java version.*?"(.*?)"', java_ver_full_str)
    java_ver_str = java_ver_match.groups()[0]
    return java_ver_str


def download_file(handle, source, destination):
    """
    Method provides the functionality to download file from the UCS Central.
    """
    from sys import stdout

    http_address = "%s/%s" % (handle.uri(), source)
    file_name = http_address.split('/')[-1]

    req = urllib2.Request(http_address)  # send the new url with the cookie.
    req.add_header('Cookie', 'ucsm-cookie=%s' % (handle.cookie))
    res = urllib2.urlopen(req)

    meta = res.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    out_file = open(destination, 'wb')
    file_size_dl = 0
    block_size = 8192
    while True:
        read_buffer = res.read(block_size)
        if not read_buffer:
            break
        file_size_dl += len(read_buffer)
        out_file.write(read_buffer)
        status = r"%10d  [%3.2f%%]" % (
            file_size_dl, file_size_dl * 100. / file_size)
        status += chr(8) * (len(status) + 1)
        stdout.write("\r%s" % status)
        stdout.flush()
    out_file.close()


def get_sha_hash(input_string):
    """ Method returns the sha hash digest for a given string.

     Attributes:
        input_string(str): the input string for which sha has to be computed
     """
    import hashlib

    return hashlib.md5(input_string).digest()


def expand_key(key, clen):
    """ Internal method supporting encryption and decryption functionality. """
    import hashlib
    from string import join
    from array import array

    blocks = (clen + 19) / 20
    x_key = []
    seed = key
    for i_cnt in xrange(blocks):
        seed = hashlib.md5(key + seed).digest()
        x_key.append(seed)
    j_str = join(x_key, '')
    return array('L', j_str)


def encrypt_password(password, key):
    """ Encrypts the password using the given key.

        Attributes:
        password (str): password to be encrypted
        key (str): key to be used to encrypt the password

     """
    from time import time
    from array import array
    import hmac
    import base64

    h_hash = get_sha_hash
    uhash = h_hash(','.join(str(x) for x in
                            [repr(time()), repr(os.getpid()),
                             repr(len(password)),
                             password, key]))[:16]
    k_enc, k_auth = h_hash('enc' + key + uhash), h_hash('auth' + key + uhash)
    pwd_len = len(password)
    password_stream = array('L', password + '0000'[pwd_len & 3:])
    x_key = expand_key(k_enc, pwd_len + 4)

    for i_cnt in xrange(len(password_stream)):
        password_stream[i_cnt] = password_stream[i_cnt] ^ x_key[i_cnt]

    cipher_t = uhash + password_stream.tostring()[:pwd_len]
    auth = hmac.new(cipher_t, k_auth).digest()
    encrypt_str = cipher_t + auth[:8]
    encoded_str = base64.encodestring(encrypt_str)
    encrypted_password = encoded_str.rstrip('\n')
    return encrypted_password


def decrypt_password(cipher, key):
    """ Decrypts the password using the given key with which the password
     was encrypted first. """
    import base64
    from array import array

    h_hash = get_sha_hash

    cipher += "\n"
    cipher = base64.decodestring(cipher)
    cipher_len = len(cipher) - 16 - 8

    uhash = cipher[:16]
    password_stream = cipher[16:-8] + "0000"[cipher_len & 3:]
    # auth = cipher[-8:]

    k_enc = h_hash('enc' + key + uhash)
    # k_auth = h_hash('auth' + key + uhash)
    # vauth = hmac.new(cipher[-8:], k_auth, sha).digest()[:8]

    password_stream = array('L', password_stream)
    x_key = expand_key(k_enc, cipher_len + 4)

    for i in xrange(len(password_stream)):
        password_stream[i] = password_stream[i] ^ x_key[i]

    decrypted_password = password_stream.tostring()[:cipher_len]
    return decrypted_password


def download_ext_file(url=None, credential=None, destination_path=None):
    """Method to download the external file.

        Attributes:
        url (str): URL of the file to be downloaded
        credential(str): credentials for file access
        destination_path(str): path to which file should be downloaded
    """
    from sys import stdout

    if not url:
        raise UcsValidationException("url parameter is not provided.")
    if not credential:
        raise UcsValidationException("credential parameter is not provided.")
    if not destination_path:
        raise UcsValidationException("path parameter is not provided.")

    file_name = os.path.basename(url)
    destination_file = os.path.join(destination_path, file_name)
    request = urllib2.Request(url)
    request.add_header("Authorization", "Basic %s" % credential)
    response = urllib2.urlopen(request)
    meta = response.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_handle = open(destination_file, 'wb')
    file_size_dl = 0
    block_sz = 64L
    while True:
        r_buffer = response.read(128 * block_sz)
        if not r_buffer:
            break

        file_size_dl += len(r_buffer)
        file_handle.write(r_buffer)
        status = r"%10d  [%3.2f%%]" % (
            file_size_dl, file_size_dl * 100. / file_size)
        status += chr(8) * (len(status) + 1)
        stdout.write("\r%s" % status)
        stdout.flush()
    print "Downloading Finished."
    file_handle.close()


def get_md5_sum(filename):
    """Method to get md5sum for the image.

        Attributes:
        filename (str): file for which md5sum is to be computed
    """
    import hashlib

    md5_obj = hashlib.md5()
    file_handler = open(filename, 'rb')
    for chunk in iter(lambda: file_handler.read(128 * md5_obj.block_size), ''):
        md5_obj.update(chunk)

    file_handler.close()
    return md5_obj.hexdigest()


def convert_to_python_var_name(name):
    """converts a ucs server variable to python recommended format

        Attributes:
        name (str): string to be converted to python recommended format
    """
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    python_var = re.sub(pattern, '_', name).lower()
    if python_var != "class":
        return python_var
    else:
        return "class_"