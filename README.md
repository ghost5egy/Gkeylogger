Gkeylogger

Notice : this code was built for eductional purpose any use for other purposes is the user responsibility not the programmer .

is a poc of windows keylogger that captures key storkes , active window name , send mail support utf-8 and hides console window 

To install on linux :

  	git clone https://github.com/ghost5egy/Gkeylogger.git
	cd Gkeylogger
	sudo chmod +x install.sh
	sudo ./install.sh
	sudo python3 Gkeylogger.py

on windows :

	download https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe and install it
	then 
	download https://github.com/mhammond/pywin32/releases/download/b227/pywin32-227.win32-py3.8.exe and install it
	then in command line :
	pip install pynput==1.6.8
	pip install pyinstaller
	finally :
	python.exe Gkeylogger.py
