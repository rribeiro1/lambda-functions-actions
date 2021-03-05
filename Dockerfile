# Dockerfile to install dependencies for AWS Lambda

FROM lambci/lambda:build-python3.7

RUN yum install -y postgresql-devel