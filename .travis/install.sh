#!/bin/bash

set -e
set -x

if [[ "${uname -s)" == 'Darwin' ]]; then
    sw_vers
    brew update || brew update

    brew outdated openssl || brew upgrade openssl
    brew install openssl@1.1

    # install pyenv
    git clone --depth 1 https://github.com/pyenv/pyenv ~/.pyenv
    PYENV_ROOT="$HOME/.pyenv"
    PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    case "${TOXENV}" in
        py35)
            pyenv install 3.5.3
            pyenv global 3.5.3
            ;;
        py36)
            pyenv install 3.6.1
            pyenv global 3.6.1
            ;;
    esac
    pyenv rehash
    python -m pip install --user virtualenv
fi

python -m virtualenv ~/.venv
source ~/.venv/bin/activate
pip install tox codecov coverage==4.5
