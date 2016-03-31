# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

# So there is also this http://www.pygit2.org/
# which yeah maybe sure but today I am just trying to 
# move the git specific logic from git-whosonfirst-hooks
# in to a standalone library (20160331/thisisaaronland) 

import os
import subprocess

import logging

def get_current_hash():
    return get_commit_hash(1)

def get_previous_hash():
    return get_commit_hash(2)

def get_commit_hash(offset):

    str_offset = "-%s" % offset

    cmd = ["git", "log", str_offset, "HEAD"]
    logging.debug(" ".join(cmd))
    
    out = subprocess.check_output(cmd)
    out = out.splitlines()
      
    commits = 0
    hash = None

    for ln in out:

        if not ln.startswith("commit "):
            continue

        commits += 1

        if commits == offset:
            ln = ln.strip()
            ignore, hash = ln.split(" ")
            break

    return hash

def get_diff(start, stop):

    cmd = [ "git", "diff", "--name-only", start, stop ]
    logging.debug(" ".join(cmd))
    
    out = subprocess.check_output(cmd)
    out = out.splitlines()

    return out
