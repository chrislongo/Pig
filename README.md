# Info

Work in progress.  Supports syntax highlighting and command completion for most Pig functions and keywords.

Build (Super+B) will run the script under "pig -x local".

# Issues

* Error line highlighting not working.
* Currently some minor keywords and functions.

# Install

1. Change to Sublime Text packages folder:  

	* OS: "~/Libary/Application Support/Sublime Text 2/Packages/User"
	* Windows: "%APPDATA%\Sublime Text 2\Packages\User"
	* Linux: "~/.config/sublime-text-2/Packages/User"

2. Run the command:

	`git clone git://github.com/chrislongo/Pig.git`

3. Preferences->Package Settings->Pig->Settings Default contains settings that can be tweaked per system.

	* "**java_home:**" Your JAVA_HOME enviroment variable (needed if not set at the system level).
	* "**pig_home:**" Where Pig is installed on your system if the Pig binary in not in the system path.

# Help

	Error: JAVA_HOME is not set.

Set "java_home" in your Pig.sublime-settings file.

	[Errno 2] No such file or directory

Set "pig_home" in your Pig.sublime-settings file.

# Notes

Syntax highlighting based on Tommy Chheng's TextMate Bundle: http://tommy.chheng.com/2009/09/14/pig-textmate-bundle/
