# Lambda Functions Experiments

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![Build](https://github.com/rribeiro1/lambda-functions-actions/actions/workflows/pipeline.yml/badge.svg)](https://github.com/rribeiro1/lambda-functions-actions/actions/workflows/pipeline.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c1c06d7c884bf48be751/maintainability)](https://codeclimate.com/github/rribeiro1/lambda-functions-actions/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c1c06d7c884bf48be751/test_coverage)](https://codeclimate.com/github/rribeiro1/lambda-functions-actions/test_coverage)
[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com)
<a href="https://github.com/rribeiro1/lambda-functions-actions/commits/main"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rribeiro1/lambda-functions-actions?color=ffc30b"></a>

### 1. Requirements

1. [Python](https://www.python.org/downloads/)
2. [Nodejs](https://nodejs.org/en/)
3. [Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
4. [Postgres](https://www.postgresql.org/)

### 2. Getting Started

```bash
# install pipenv
pip install pipenv

# install dependencies
pipenv install

# install development dependencies
pipenv install --dev

# install dependencies for serverless and development
npm install
```

### 3. Running Unit Tests

```bash
npm run test:unit
```

### 4. Deployment

Example with [awsudo](https://pypi.org/project/awsudo/).

```bash
# Deployment
awsudo -u <profile> npm run deploy:development
```
