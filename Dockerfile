FROM centos:8.1.1911

RUN dnf -y update && dnf clean all && rm -rf /var/cache/dnf
RUN dnf install -y dnf-plugins-core \
    && dnf config-manager --set-enabled PowerTools \
    && dnf clean all && rm -rf /var/cache/dnf

RUN dnf install -y dnf-utils vim make wget git libxml2-devel libzip-devel \
    && dnf clean all && rm -rf /var/cache/dnf

# install SOPS
RUN wget -O sops.rpm https://github.com/mozilla/sops/releases/download/v3.6.1/sops-3.6.1-1.x86_64.rpm \
    && dnf localinstall -y sops.rpm

# install gcloud sdk
COPY ./google-cloud-sdk.repo /etc/yum.repos.d/google-cloud-sdk.repo
RUN yum install -y google-cloud-sdk && yum clean all && rm -rf /var/cache/yum