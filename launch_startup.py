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


sys.path.insert(0, PYBTC)

try:
    from bitcoin import *
    console.hud_alert("pybitcointools successfully imported!".title(), "success", 1.42)
except ImportError:
    console.hud_alert("Unable to import... pybitcointools".title(), "error", 1.42)
