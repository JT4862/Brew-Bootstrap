# Brew-Bootstrap

Brew-Bootstrap is a convenient toolset for managing the installation and uninstallation of software on macOS using Homebrew. This repository contains scripts that leverage a `Brewfile` to automate the setup of a development environment.

## Contents

- [`Brewfile`](https://github.com/JT4862/Brew-Bootstrap/blob/brewfile/Brewfile): A list of software to be installed, including Homebrew taps, development tools, utilities, fonts, and GUI applications, each accompanied by a brief description.
- [`install-bootstrap.sh`](https://github.com/JT4862/Brew-Bootstrap/blob/brewfile/install-bootstrap.sh): A script to install software listed in the `Brewfile`. It checks for the presence of Homebrew, installs it if missing, updates Homebrew recipes, and then iterates through the `Brewfile`, prompting the user for confirmation before installing each item.
- [`un-install-bootstrap.sh`](https://github.com/JT4862/Brew-Bootstrap/blob/brewfile/un-install-bootstrap.sh): A script to uninstall software listed in the `Brewfile`. It checks for the presence of Homebrew and then iterates through the `Brewfile`, prompting the user for confirmation before uninstalling each item.

## Usage

### Installation

1. Clone the repository:
   git clone https://github.com/JT4862/Brew-Bootstrap.git
   cd Brew-Bootstrap

2. Make the script executable
	```chmod +x ./install-bootstrap.sh```

3. Run the install script
	```./install-bootstrap.sh ```

### Uninstallation

1. Make the script executable
	```chmod +x ./un-install-bootstrap.sh```

2. Run the uninstall script
	```./un-install-bootstrap.sh```


## Customize the Brefile
You can customize the Brewfile to suit your specific software needs. Simply edit the file, following the existing format, to add or remove software.

## Contributing
Contributions to Brew-Bootstrap are welcome. Please feel free to submit pull requests or open issues to improve the scripts or add functionality.
