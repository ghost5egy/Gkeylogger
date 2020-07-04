sudo apt update
sudo apt upgrade -y
sudo apt install python
sudo apt install wine32 -y
rm -r -f ~/.wine
WINEARCH=win32 WINEPREFIX=~/.wine wine wineboot
wget https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
sudo wine python-3.8.2.exe
sudo wine python -m pip install --upgrade pip
wget https://github.com/mhammond/pywin32/releases/download/b227/pywin32-227.win32-py3.8.exe
sudo wine pywin32-227.win32-py3.8.exe
sudo wine /root/.wine/drive_c/users/root/Local\ Settings/Application\ Data/Programs/Python/Python38-32/python.exe -m pip install pynput==1.6.8
sudo wine /root/.wine/drive_c/users/root/Local\ Settings/Application\ Data/Programs/Python/Python38-32/python.exe -m pip install pyinstaller
