#!/bin/bash

# Check for Homebrew
if test ! $(which brew); then
    echo "Homebrew is not installed. Nothing to uninstall."
    exit 1
fi

# Uninstall software based on Brewfile
if [ -f Brewfile ]; then
    echo "Checking software from Brewfile for uninstallation..."
    while IFS= read -r line; do
        if [[ $line == brew* || $line == cask* ]]; then
            software=$(echo $line | cut -d ' ' -f 2)
            read -p "Do you want to uninstall $software? (y/n) " choice
            case "$choice" in 
                y|Y ) brew uninstall $software;;
                n|N ) echo "Skipping uninstallation of $software";;
                * ) echo "Invalid response. Skipping uninstallation of $software";;
            esac
        fi
    done < Brewfile
else
    echo "Brewfile not found, skipping uninstallation..."
fi

echo "Uninstallation process completed."
