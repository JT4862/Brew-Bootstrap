# Brew Bootstrap Install

I've written this as a script to run when setting up a new computer.

```bash
chmod +x bootstrap-brew.sh
./bootstrap-brew.sh
```
Does the following:
* Checks if [`brew`](https://brew.sh) is installed, if not installs it.
* Installs necessary command-line tools, casks (apps) and Mac App Store apps I would want on a computer. Includes things like: 
	* Slack
	* Notion
	* Spotify
	* Discord
	* VSCODE
* Changes system defaults to: show file extensions, and disable natural scroll.	