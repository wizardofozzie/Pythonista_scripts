## Downloadista, modified so that github_download() accepts:
##  * clipboard GitHub URL
##  * GitHub URL
##  * "user/repo"


from __future__ import absolute_import
from __future__ import print_function
import zipfile
import tarfile
import shutil
import os, sys
import re
import clipboard

from os import path

try:
    from urllib.request import urlretrieve
except:
    from urllib import urlretrieve

DOCUMENTS = os.path.expanduser("~/Documents")

REGEX_GITHUB_URL = re.compile(r'''^http(s?)://([\w-]*\.)?github\.com/(?P<user>[\w-]+)/(?P<repo>[\w-]*)((/tree|/blob)/(?P<branch>[\w-]*))?''')


def extract_git_id(giturl):
    m = REGEX_GITHUB_URL.match(giturl)
    #print m.groupdict()    #{'repo': 'pybitcointools', 'user': 'wizardofozzie', 'branch': None}
    return m

def _change_dir(dir="Documents"):
    pwd = os.getcwd()
    if pwd != DOCUMENTS:
        os.chdir(os.path.expanduser("~/{0}".format(dir)))


def is_github_url(url):
    return bool(REGEX_GITHUB_URL.match(url))


def _decode_github_url(url):
    if is_github_url(url):
        ret = extract_git_id(url)
        gd = ret.groupdict()
        user, repo = gd.get("user"), gd.get("repo")
        branch = gd.get("branch")
        branch = "master" if branch is None else branch
        return (user, repo, branch)



def github_download(*args):
    branch = None
    if len(args) == 0:
        return github_download(clipboard.get())
    elif len(args) ==1 and is_github_url(args[0]):
        user, repo, branch = _decode_github_url(args[0])
    elif (len(args) == 1 and re.match(r'^[0-9a-zA-Z]*/[0-9a-zA-Z]*$', str(args[0]))):
        user, repo = args[0].split("/", 1)
        branch = "master"
    elif len(args)==2:
        user, repo = args
        branch = "master"
    elif len(args) == 3:
        user, repo, branch = args
    else: return
    branch = "master" if not branch else branch

    _change_dir("Documents")
    print(('Downloading {0}...'.format(repo)))
    base_url = 'https://github.com/{0}/{1}/archive/{2}.zip'
    url = base_url.format(user, repo, branch)
    zipname = '{0}.zip'.format(repo)
    urlretrieve(url, zipname)

    print('Extracting...')
    z = zipfile.ZipFile(zipname)
    z.extractall()
    dst = os.path.join(DOCUMENTS, zipname[:-len(".zip")])
    src = "{dir}-{branch}".format(dir=dst, branch=branch)
    os.remove(zipname)
    try:
        os.rename(src, dst)
    except OSError:
        os.rename(dst, "{}.BAK".format(dst))
        os.rename(src, dst)
    print('Done.')

    # If branch is a version tag the directory
    # is slightly different
    #if re.match('^v[0-9.]*$', branch):
    #    dirname = repo + '-' + branch[1:]
    #else:
    #    dirname = repo + '-' + branch

    return os.path.basename(dst)


gdl = github_download

def pypi_download(package, version):
    _change_dir("Documents")
    print(('Downloading {0}...'.format(package)))
    url = 'https://pypi.python.org/packages/source/{0}/{1}/{1}-{2}.tar.gz'.format(package[0], package, version)
    tarname = package + '.tar.gz'
    urlretrieve(url, tarname)

    print('Extracting...')
    t = tarfile.open(tarname)
    t.extractall()
    os.remove(tarname)
    print('Done.')

    dirname = package + '-' + str(version)
    return dirname

if __name__ == "__main__":
    github_download()
