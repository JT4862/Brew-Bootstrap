#!/bin/bash

# Function to check if a command exists
command_exists() {
    type "$1" &> /dev/null
}

# Check for Homebrew, install if we don't have it
if ! command_exists brew; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

# Update Homebrew
brew update

# Check for Python 3, install if we don't have it
if ! command_exists python3; then
    echo "Installing Python 3..."
    brew install python3
else
    echo "Python 3 is already installed."
fi

# Run the install-bootstrap.py script
echo "Running install-bootstrap.py..."
python3 install-bootstrap.py
