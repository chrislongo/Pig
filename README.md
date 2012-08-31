# Info

![A picture of the syntax highlighting and build output](http://i.imgur.com/lpiu7.png)

Work in progress.  Supports syntax highlighting and command completion for most Pig functions and keywords.

Build (Super+B) will run the script under "pig -x local".

# Issues

* Error line highlighting not working.
* Currently some minor keywords and functions.

# Install

### Easy

[Install via Package Control](http://wbond.net/sublime_packages/package_control)

### Hard 

* Change to Sublime Text packages folder:  

	* **OS:** `~/Library/Application Support/Sublime Text 2/Packages/User`
	* **Windows:** `%APPDATA%\Sublime Text 2\Packages\User`
	* **Linux:** `~/.config/sublime-text-2/Packages/User`

* Run the command:

	`git clone git://github.com/chrislongo/Pig.git`

* `Preferences->Package Settings->Pig->Settings Default` contains settings that can be tweaked per system.

	* "**java_home:**" Your JAVA_HOME enviroment variable (needed if not set at the system level).
    * "**pig_home:**" Where Pig is installed on your system if the Pig binary in not in the system path.	
    * "**execution_mode:**" Whether to run in local or mapreduce mode (see Pig docs).
    * "**pig_classpath:**" May be needed per system when run in mapreduce mode.
    * "**log4j_properties:**" You can specify a custom log4j.properties for prettier output.

# Help

	Error: JAVA_HOME is not set.

Set "java_home" in your Pig.sublime-settings file.

	[Errno 2] No such file or directory

Set "pig_home" in your Pig.sublime-settings file.

# Attribution

Syntax highlighting based on Tommy Chheng's TextMate Bundle: 

https://github.com/tc/pig-latin-tmbundle