## Move video files downloaded with youtube-dl from Documents => Documents/VIDEO

import os, sys, shutil
from pprint import pprint as pp
import os.path as path

VIDEO_EXTENSIONS = [ 
    ".mp4", ".m4a", ".webm"
    ]


def get_vid_names(dir="~/Documents", fullpath=False):
    assert path.isdir(path.expanduser(dir))
    filez = [f for f in os.listdir(path.expanduser(dir)) if path.isfile(f)]
    ret = [x for x in filez if path.splitext(x)[-1] in VIDEO_EXTENSIONS]
    return ret if not fullpath else map(lambda x: path.join(path.expanduser(dir), x)[8:], ret)


def move_vids(fromdir='~/Documents', todir='~/Documents/VIDEO'):
    vidlist = get_vid_names(fromdir)
    for f in vidlist:
        try:
            os.rename(
                path.join(path.expanduser(fromdir), f)[8:], 
                path.join(path.expanduser(todir), f)[8:]
                )
            print("==> {0}/{1}".format(todir, f))
        except:
            print("Could not move file:\t {fn}".format(fn=f))


if __name__ == "__main__":
    move_vids()
