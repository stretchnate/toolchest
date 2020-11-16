# A CentOS 8.1 Container with gcloud and SOPS

## Set Up for gcloud kms
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