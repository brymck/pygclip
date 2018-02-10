#!/bin/bash

set -e
set -x

source ~/.venv/bin/activate
codecov --env TRAVIS_OS_NAME,TOXENV
