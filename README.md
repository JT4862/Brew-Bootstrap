# Brewfile Management Scripts

This repository contains two Python scripts for managing software installations and uninstalls using Homebrew based on a Brewfile. The scripts provide a user-friendly interface for installing, updating, or uninstalling software packages.

## Contents

- [`Brewfile`](https://github.com/JT4862/Brew-Bootstrap/blob/brewfile/Brewfile): A list of software to be installed, including Homebrew taps, development tools, utilities, fonts, and GUI applications, each accompanied by a brief description.
- [`install-bootstrap.py`](https://github.com/JT4862/Brew-Bootstrap/blob/brewfile/install-bootstrap.py): 
	-Lists software that needs to be installed or updated.
	-Allows installing all software at once, individually, or canceling the process.
	-Provides a summary of installed and updated items.
- [`un-install-bootstrap.py`](https://github.com/JT4862/Brew-Bootstrap/blob/brewfile/un-install-bootstrap.sh): 
	-Lists installed software that can be uninstalled.
	-Allows uninstalling all software at once, individually, or canceling the process.
	-Provides a summary of uninstalled items.

## Usage

### Installation

1. Clone the repository:
   git clone https://github.com/JT4862/Brew-Bootstrap.git

2. Modify the Brewfile.
	If you wish you can modify the Brewfile with your favorite hombrew packages

3. Run the Python script
	```python3 install-bootstrap.py```

4. Follow the Prompts or update the software


### Uninstallation

1. Ensure the Brewfile lists the software you want to uninstall.
	

2. Run the uninstall script
	```python3 uninstall-bootstrap.py```

3. 	Follow the prompts to uninstall software.


## Requirements
 - Python 3.x
 - Homebrew

## Customize the Brefile
You can customize the Brewfile to suit your specific software needs. Simply edit the file, following the existing format, to add or remove software.

## Note
 - The scripts assume that the Brewfile is named Brewfile_copy and is located in the same directory as the scripts.
 - Modify the Brewfile path in the scripts if your Brewfile has a different name or location.

## Contributing
Contributions to Brew-Bootstrap are welcome. Please feel free to submit pull requests or open issues to improve the scripts or add functionality.
