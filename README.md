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

And a Special Thanks to [TheSpeedX](https://github.coom/TheSpeedX) for optimising this script and naming it. LMAO.

## Installation

Just make sure apktool and apksigner are properly installed.

**NOTE FOR TERMUX**:- Wont work on termux even if you have apktool installed. Because on termux, the AndroidManifest.xml decompiled by apktool is not in proper encoding (I ran the latest version 2.4.0). But on using the`--force-manifest` option in apktool we can get the xml in proper encoding, but on compiling the target app the xml wont compile... And there is no other way to do it. Check [this issue on apktool's official repo.](https://github.com/iBotPeaches/Apktool/issues/1699)

## Usage

`python3 main.py path/to/payload.apk path/to/any/app.apk path/to/save/the/final/app/with/name.apk`

example:- `python3 main.py /sdcard/somepayload.apk /sdcard/Whatsapp.apk /sdcard/Whatsapp_Infected.apk`

## Contact

Telegram:- *@R37R0_GH057*

Discord:- *Ken Kaneki#2895*
