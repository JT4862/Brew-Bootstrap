Brew-Bootstrap

Brew-Bootstrap is a convenient toolset for managing the installation and uninstallation of software on macOS using Homebrew. This repository contains scripts that leverage a Brewfile to automate the setup of a development environment.

Contents

Brewfile: A list of software to be installed, including Homebrew taps, development tools, utilities, fonts, and GUI applications, each accompanied by a brief description.
install-bootstrap.sh: A script to install software listed in the Brewfile. It checks for the presence of Homebrew, installs it if missing, updates Homebrew recipes, and then iterates through the Brewfile, prompting the user for confirmation before installing each item.
un-install-bootstrap.sh: A script to uninstall software listed in the Brewfile. It checks for the presence of Homebrew and then iterates through the Brewfile, prompting the user for confirmation before uninstalling each item.
Usage

Installation
Clone the repository: git clone https://github.com/JT4862/Brew-Bootstrap.git

cd Brew-Bootstrap

Run the installation script: './install-bootstrap.sh'

Uninstallation
Run the uninstallation script: './un-install-bootstrap.sh'
Customizing the Brewfile

You can customize the Brewfile to suit your specific software needs. Simply edit the file, following the existing format, to add or remove software.

Contributing
Contributions to Brew-Bootstrap are welcome. Please feel free to submit pull requests or open issues to improve the scripts or add functionality.

This README provides a basic overview of the repository's purpose, contents, and usage instructions. It's designed to be clear and user-friendly for those looking to automate their macOS environment setup with Homebrew.