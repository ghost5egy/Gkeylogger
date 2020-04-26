sudo apt update 
sudo apt upgrade -y
sudo apt install python 
sudo apt install wine -y 
wget https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
sudo wine python-3.8.2.exe
sudo wine /root/.wine/drive_c/users/root/Local\ Settings/Application\ Data/Programs/Python/Python38-32/python.exe -m pip install pynput==1.6.8
sudo wine /root/.wine/drive_c/users/root/Local\ Settings/Application\ Data/Programs/Python/Python38-32/python.exe -m pip install win32gui
sudo wine /root/.wine/drive_c/users/root/Local\ Settings/Application\ Data/Programs/Python/Python38-32/python.exe -m pip install pyinstaller
