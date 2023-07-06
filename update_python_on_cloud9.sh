#!/bin/bash

# Update system
sudo yum update -y

# Install prerequisites
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel readline-devel sqlite-devel wget curl git xz-devel

# Clone pyenv repository
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Set up environment for pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

# Apply changes to the current session
source ~/.bash_profile

# Install Python 3.9
pyenv install 3.9

# Set Python 3.9 as global default
pyenv global 3.9
