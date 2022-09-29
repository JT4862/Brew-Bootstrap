# Brew Bootstrap Install

I've written this as a script to run when setting up a new computer. [Download the entirety of the gist](https://gist.github.com/cooperpellaton/4d76ef3afdc78018af89dd6963d02481/archive/d0c8e6567825acaa58bd55a92435a33cf95726a6.zip) and then run: 

```bash
chmod +x bootstrap-brew.sh
./bootstrap-brew.sh
```
Does the following:
* Checks if [`brew`](https://brew.sh) is installed, if not installs it.
* Installs necessary command-line tools, casks (apps) and Mac App Store apps I would want on a computer. Includes things like: 
	* Ripgrep
	* NeoVim
	* Spotify
	* Discord
* Changes system defaults to: show file extensions, and disable natural scroll.	