# Usage - python3 git-clean-branches.py /var/www/html/lms 2101

import sys
import re
import subprocess
import datetime

gitdir = sys.argv[1]
prefix = sys.argv[2]
cmd_base=["git", "--git-dir="+gitdir+"/.git"]

def deleteLocal(branch):
    del_cmd = cmd_base.copy()
    del_cmd.append('branch')
    del_cmd.append('-D')
    del_cmd.append(branch)
    
    # print(del_cmd)
    return subprocess.Popen(del_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def deleteRemote(branch, remote='origin'):
    del_cmd = cmd_base.copy()
    del_cmd.append('push')
    del_cmd.append('-d')
    del_cmd.append(remote)
    del_cmd.append(branch)
    
    # print(del_cmd)
    return subprocess.Popen(del_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def fetch():
    fetch=cmd_base.copy()
    fetch.append('fetch')
    subprocess.run(fetch)

fetch()

# print(cmd_base)

branches_cmd = cmd_base.copy()
branches_cmd.append('branch')
branches_cmd.append('-r')

print(branches_cmd)
process=subprocess.Popen(branches_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

branches=process.stdout.readlines()
if len(branches) >= 1:
    regex = "origin/("+str(prefix)+"_[A-Za-z0-9_]*)"
    
    for branch in branches:
        branch = branch.decode('utf-8')
        match = re.search(regex, branch)
        if match:
            print("deleting local branch "+str(match.group(1)))
            dprocess=deleteLocal(match.group(1))
            if dprocess:
                result=dprocess.stdout.readlines()
                if len(result) > 0:
                    for line in result:
                        print(line)
                    
            print("deleting remote branch "+str(match.group(1)))
            rprocess=deleteRemote(match.group(1))
            if rprocess:
                result=rprocess.stdout.readlines()
                if len(result) > 0:
                    for line in result:
                        print(line)
                    
fetch()