# coding: utf-8
## import a zip to Pythonista via share-sheet

import appex, os, shutil, sys

if not appex.is_running_extension():
    sys.stderr.write("Must run from share sheet")
    sys.exit(1)
else:
    filepath = appex.get_url()
    filepath = filepath[7:] if filepath.startswith("file://") else filepath
    filename = filepath.rsplit("/", 1)[-1]
    docsdir = os.path.expanduser("~/Documents")
    try:
        shutil.copy(
                    filepath,
                    os.path.join(docsdir, filename)
                    )
        print "Success! Copied {0} to {1}".format(filename, filepath)
    except:
        sys.stderr.write("Could not copy {0} from {1}".format(filename, filepath))
        
