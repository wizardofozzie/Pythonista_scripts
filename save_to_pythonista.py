# coding: utf-8
## import a file to Pythonista via share-sheet

import appex, os, shutil, sys
from urlparse import urlparse
from urllib import url2pathname

if not appex.is_running_extension():
    sys.stderr.write("Must run from share sheet")
    sys.exit(1)
else:
    file_url = appex.get_url()
    file_url = file_url[len("file://"):] if file_url.startswith("file://") else file_url
    p = urlparse(file_url)            # for % encoded URLs
    filepath = url2pathname(p.path)
    name = os.path.basename(filepath)
    docsdir = os.path.expanduser("~/Documents")
    dest = os.path.join(docsdir, name)
    try:
        shutil.copy(filepath, dest)
        print "Success! Copied {0} to {1}".format(filename, filepath)
    except:
        sys.stderr.write("Could not copy {0} from {1}".format(filename, filepath))
