# Tools
## SOPS Container
### A CentOS 8.1 Container with gcloud and SOPS

#### Set Up for gcloud kms
1.  run `docker-compose up -d`
2.  `docker exec -it toolchest /bin/bash`
3.  `gcloud init --console-only`
4.  copy link and paste in browser
5.  follow the instructions to allow access
6.  copy code and paste in terminal (hit enter)
7.  run `gcloud auth login --no-launch-browser`
8.  repeat steps 4-6
9.  run `gcloud auth application-default login`
10. repeat steps 4-6

Now you can run sops encrypt or decrypt commands using a gcloud kms key

## Gitlab Branch Cleaner
### A python application to delete gitlab branches

This tool will find gitlab branches (on the remote repository) and delete them if they match the prefix provided. i.e. If I provide `2101` as a branch prefix the tool will match any branch that starts with 2101_. Our current directive is to keep branches for one year.
#### Usage
Initiate Vritual environment (if not already done)
- `virtualenv .venv`

Activate Virtual environment
- `source .venv/bin/activate`

Install argparse (if not already done)
- `pip install argparse`

Remove branches based on prefix
- `python3 git-clean-branches.py <path to repository> <branch prefix (e.g. 2101)>`