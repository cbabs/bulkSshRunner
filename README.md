# bulkSshRunner
A python program to config large amounts of devices at once and creates a log.

## Monitor windows servers and processes

This was program created to config a bunch of devices/systems at once.  
It uses SSH and is not device specific.  It does give you a txt log
of all the commands that were entered and the output.

## Setup

You will need to clone from github and install 3 python libraries.  
If run pip install -r requirements from the cloned dir.  You will
need to have pip as a sys path or call it from the dir where it resides.

For example:

git clone https://github.com/cbabs/bulkSshRunner

cd bulkSshRunner

pip install -r requirements.txt

## Configure and run the app

You will need to edit two files.  The sshCmds.txt and hosts.txt files.
The sshCmds.txt file is where you define the commands.  You enter them
in the file like you would in a putty or a terminal. The hosts.txt file
is where you enter the hosts.  One host per line.  No leading or
trailing white space.

Once you have edited the txt files, you can run the program. 
Depending on you python setup changes how you run the program.  
Open powershell or a terminal window.  Go to the directory where the file is.  
Then run the command to have python execute the py file and make sure the
hosts.txt is present.  I have python installed in c:\python36\ so for me it would look

c:\tools\monitor>c:\python36\python.exe bulkSshRunner.py

A linux setup may look like this:

cbabcock@ubuntuMon:/usr/share/utils/winProcessMonitor$ /lib/bin/python36 ./bulkSshRunner.py

## Notes

Please feel very welcome to make suggestion and/or reports issues.

Cbabs
