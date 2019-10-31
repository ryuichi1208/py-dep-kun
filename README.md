![Python](https://img.shields.io/badge/Python-3.6%2F3.7-red)
![CircleCI](https://img.shields.io/circleci/build/github/ryuichi1208/py-dep-kun/master)
[![codecov](https://codecov.io/gh/ryuichi1208/py-dep-kun/branch/master/graph/badge.svg)](https://codecov.io/gh/ryuichi1208/py-dep-kun)
![GitHub language count](https://img.shields.io/github/languages/count/ryuichi1208/py-dep-kun)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryuichi1208/py-dep-kun)
![GitHub](https://img.shields.io/github/license/ryuichi1208/py-dep-kun)

# py-dep-kun
A series of processing groups deployed to DockerHub

## Description

A series of pipelines on code style uniformity and deployment methods.

The trigger for the pipeline is set to be activated by detecting Push each time.

It is designed to use a set of tools that are basically required for Python development.

Of course, the code is basically written to conform to the Python standard style (pep8) etc., but there is an advantage that it can be used to detect it automatically.

## Requirement

Basically developed based on Python 3.6 or Python 3.7 (3.8 will be supported in the future)

The necessary libraries are as follows.

```
numpy==1.17.2
pylint==2.3.1
pytest==5.1.2
pytest-cov==2.7.1
pytest-randomly==3.1.0
black==19.3b0
pycodestyle==2.5.0
mypy==0.720
mypy-extensions==0.4.1
codecov==2.0.15
PyYAML==5.1.2
redis==3.3.8
requests==2.22.0
rope==0.14.0
rsa==4.0
setuptools==41.2.0
six==1.12.0
slackweb==1.0.5
soupsieve==1.9.3
toml==0.10.0
tqdm==4.35.0
typed-ast==1.4.0
typing-extensions==3.7.4
uptime==3.0.1
urllib3==1.25.3
utils==0.9.0
```

## Do lint

```
$ docker run -ti -v $(pwd):/app --workdir=/app coala/base coala --files run.py --bears PEP8Bear
```

## Authn

``` yaml
jobs:
  build:
    docker:
      - image: acme-private/private-image:321
        auth:
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD
```

## To deploy

[ryuichi1208/py-dep-kun](https://cloud.docker.com/repository/registry-1.docker.io/ryuichi1208/py-dep-kun)

Deploy to above with push with tag as a trigger.

## Author

[ryuichi1208](https://github.com/ryuichi1208)
