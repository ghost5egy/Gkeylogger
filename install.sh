apt update ; apt upgrade -y
apt install python 
apt install wine -y 
wget https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
wine python-3.8.2.exe
wine /root/.wine/drive_c/Python27/python.exe -m pip install pynput==1.6.8
wine /root/.wine/drive_c/Python27/python.exe -m pip install win32gui==221.6
wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
