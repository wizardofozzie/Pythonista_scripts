## Downloadista, modified so that github_download() accepts:
##  * clipboard GitHub URL 
##  * GitHub URL 
##  * "user/repo"


import urllib
import zipfile
import tarfile
import shutil
import os, sys
import re
import clipboard

from os import path

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
    elif (len(args) == 1 and re.match(ur'^[0-9a-zA-Z]*/[0-9a-zA-Z]*$', str(args[0]))):
        user, repo = args[0].split("/", 1)
        branch = "master"
    elif len(args)==2:
        user, repo = args
        branch = "master"
    elif len(args) == 3:
        user, repo, branch = args
    else: return
    branch = "master" if not branch else branch
    
    #_change_dir("Documents")
    print 'Downloading {0}...'.format(repo)
    base_url = 'https://github.com/{0}/{1}/archive/{2}.zip'
    url = base_url.format(user, repo, branch)
    zipname = '{0}.zip'.format(repo)
    urllib.urlretrieve(url, zipname)

    print 'Extracting...'
    z = zipfile.ZipFile(zipname)
    z.extractall()
    os.remove(zipname)
    print 'Done.'

    # If branch is a version tag the directory
    # is slightly different
    if re.match('^v[0-9.]*$', branch):
        dirname = repo + '-' + branch[1:]
    else:
        dirname = repo + '-' + branch
    return dirname


def pypi_download(package, version):
    _change_dir("Documents")
    print 'Downloading {0}...'.format(package)
    url = 'https://pypi.python.org/packages/source/{0}/{1}/{1}-{2}.tar.gz'.format(package[0], package, version)
    tarname = package + '.tar.gz'
    urllib.urlretrieve(url, tarname)

    print 'Extracting...'
    t = tarfile.open(tarname)
    t.extractall()
    os.remove(tarname)
    print 'Done.'

    dirname = package + '-' + str(version)
    return dirname
