# Linder

## About

This simple Python3 script will bind a Metasploit generated android payload with any other apk.

It just automates the following:-

  [+] Copying payload smali files into target app.
  
  [+] Finding target app's MainActivity smali files.
  
  [+] Finding Hookpoint and adding hook there.
  
  [+] Writing permissions in the Androidmanifest.xml
  
  [+] Compile the infected app.
  
  [+] Signing.

There are some apps like FacebookLite which are a little protected by this method. The MainActivity smali file specified in the Manifest is not present. I'll come up with something in the next update.

And a Special Thanks to [TheSpeedX](https://github.coom/TheSpeedX) for optimising this script.

## Installation

Just make sure apktool and apksigner are properly installed.

NOTE:- If you are using APKTOOL on Termux then it may not work. I mean it works but it fails to output the Manifest in proper encoding. And because of it the script throws an UnicodeDecodeError, which is fixable if opened as ISO-8859-1 but it throws another error.(I think it is also fixable, I'll try to fix it in the next update :p)

## Usage

`python3 main.py path/to/payload.apk path/to/any/app.apk path/to/save/the/final/app/with/name.apk`

example:- `python3 main.py /sdcard/somepayload.apk /sdcard/Whatsapp.apk /sdcard/Whatsapp_Infected.apk`

## Contact

Telegram:- *@R37R0_GH057*

Discord:- *Ken Kaneki#2895*
