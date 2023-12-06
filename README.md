# Brew-Bootstrap

Welcome to Brew-Bootstrap, a comprehensive toolkit for setting up and managing your development environment on macOS and Ubuntu systems using Homebrew and other utilities.

## Overview

Brew-Bootstrap provides a set of scripts and configurations to streamline the setup of a development environment. It includes scripts for installing, updating, and uninstalling packages, as well as scanning and managing Homebrew packages.

## Features

- **Bootstrap Scripts for macOS and Ubuntu**: Easy-to-use scripts to set up your environment on macOS and Ubuntu.
- **Homebrew Package Management**: Efficiently manage Homebrew packages, casks, and taps.
- **Automated Installation and Uninstallation**: Scripts to automate the installation and uninstallation of packages defined in a Brewfile.
- **Development Tools and Utilities**: Pre-configured list of essential tools and utilities for development.

## Repository Structure

- [`mac/bootstrap.sh`](https://github.com/JT4862/Brew-Bootstrap/blob/main/mac/bootstrap.sh): Script to install Homebrew and Python 3 if they are not already installed on macOS.
- [`mac/brewfile`](https://github.com/JT4862/Brew-Bootstrap/blob/main/mac/brewfile): A Brewfile containing a list of Homebrew packages, casks, and taps for macOS.
- [`mac/homebrew-scan.py`](https://github.com/JT4862/Brew-Bootstrap/blob/main/mac/homebrew-scan.py): Python script to scan and list installed Homebrew packages, casks, and taps.
- [`mac/install-bootstrap.py`](https://github.com/JT4862/Brew-Bootstrap/blob/main/mac/install-bootstrap.py): Script to install or update packages from the Brewfile.
- [`mac/uninstall-bootstrap.py`](https://github.com/JT4862/Brew-Bootstrap/blob/main/mac/uninstall-bootstrap.py): Script to uninstall packages listed in the Brewfile.
- [`ubuntu-bootstrap-install.py`](https://github.com/JT4862/Brew-Bootstrap/blob/main/ubuntu-bootstrap-install.py): Script to install packages listed in `ubuntu-packages.txt` for Ubuntu systems.
- [`ubuntu-packages.txt`](https://github.com/JT4862/Brew-Bootstrap/blob/main/ubuntu-packages.txt): List of packages for installation on Ubuntu systems.

## Getting Started

To get started with Brew-Bootstrap, follow these steps:

### For macOS:

 1. **Clone the Repository**: 
Clone the repository to your local machine and navigate to the `mac` directory.
	```bash
	git clone https://github.com/JT4862/Brew-Bootstrap.git

2. **Run the Bootstrap Script**:
	Make the bootstrap script executable and run it. This script will install Homebrew and Python 3 if they are not already installed then run the `install-bootstrap.py` automatically which installed packages from the `brewfile`.

	`chmod +x bootstrap.sh` then `./bootstrap.sh`

4. **Uninstall Packages (Optional)**:
	If you need to uninstall packages, run  `python3 uninstall-bootstrap.py` script.

### For Ubuntu:

1. **Clone the Repository**:
Clone the repository to your local machine.

`git clone https://github.com/JT4862/Brew-Bootstrap.git`

3. **Run the Ubuntu Bootstrap Install Script**:
Make the Ubuntu bootstrap install script executable and run it. This script will install the packages listed in ubuntu-packages.txt.

`chmod +x ubuntu-bootstrap-install.py` then run `./ubuntu-bootstrap-install.py`

## Contributions

Contributions to Brew-Bootstrap are welcome! Please read our contribution guidelines for more information.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

