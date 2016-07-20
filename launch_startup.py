# coding: utf-8
import os, sys, console
import clipboard as cl

clset, clget = cl.set, cl.get
h = help


PYFW = os.path.join(sys.executable.rpartition("/")[0], "Frameworks/PythonistaKit.framework")
PYLIB = os.path.join(PYFW, "pylib")
HOME1 = os.path.expanduser("~")
HOME2 = DOCS = os.path.join(HOME1, "Documents")
PYBTC = os.path.join(HOME2, "pybitcointools-master") # os.path.expanduser("~/Documents/pybitcointools-master")

# PYBTC_source = os.path.expanduser("~/Documents/pybitcointools-master/bitcoin")
# PYBTC_dest = os.path.expanduser("~/Documents/site-packages/bitcoin")

#from pythonista_startup 
sys.path.insert(0, PYBTC)

# try:
#     from bitcoin import *
#     console.hud_alert("pybitcointools successfully imported!".title(), "success", 1.42)
# except ImportError:
#     console.hud_alert("Unable to import... pybitcointools".title(), "error", 1.42)

def to_bytes(x):
    if sys.version_info.major > 2 and isinstance(x, str):
        x = bytes(x, 'utf-8')
    return x

s2b = str2bytes = to_bytes


def from_bytes(x):
    if sys.version_info.major > 2 and isinstance(x, bytes):
        x = str(x, 'utf-8')
    return x

b2s = bytes2str = from_bytes

try:
    import cd_ls_pwd     # import the three functions
    cd = cd_ls_pwd.cd    # send up a top-level alias
    ls = cd_ls_pwd.ls    # send up a top-level alias
    pwd = cd_ls_pwd.pwd  # send up a top-level alias
except ImportError:
    pass
