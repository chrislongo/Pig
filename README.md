# Info

Work in progress.  Supports syntax highlighting and command completion for most Pig functions and keywords.
Build will run the script under "pig -x local".

# Issues

* PigLatin.sublime-build needs to be modified per system (I need to figure out global env vars in ST2).
* Error line highlighting not working.
* Currently some minor keywords and functions.

# Install

1. Copy the 'Pig' folder to your user packages folder.  

	OS: "~/Libary/Application Support/Sublime Text 2/Packages/User"
	Windows: "%APPDATA%\Sublime Text 2\Packages\User"
	Linux: "~/.config/sublime-text-2/Packages/User"

2. Edit "PigLatin.sublime-build" to match your system config. 

Syntax highlighting based on Tommy Chheng's TextMate Bundle: http://tommy.chheng.com/2009/09/14/pig-textmate-bundle/
