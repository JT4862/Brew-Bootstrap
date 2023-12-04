#!/bin/bash

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
else
    echo "Homebrew already installed."
fi

# Update homebrew recipes
brew update

# Install from Brewfile
if [ -f Brewfile ]; then
    echo "Checking software from Brewfile..."
    while IFS= read -r line; do
        if [[ $line == brew* || $line == cask* ]]; then
            software=$(echo $line | cut -d ' ' -f 2)
            IFS= read -r next_line
            comment=$(echo $next_line | sed 's/# //')
            read -p "Do you want to install/update $software? $comment (y/n) " choice
            case "$choice" in 
                y|Y ) brew install $software;;
                n|N ) echo "Skipping $software";;
                * ) echo "Invalid response. Skipping $software";;
            esac
        fi
    done < Brewfile
else
    echo "Brewfile not found, skipping..."
fi

# Show filename extensions by default
defaults write NSGlobalDomain AppleShowAllExtensions -bool true

# Disable "natural" scroll
defaults write NSGlobalDomain com.apple.swipescrolldirection -bool false

echo "Completed."
