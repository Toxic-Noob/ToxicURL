#Coded By DarkSlad3
#A Product Of ToxicNoob

import os
import sys
import time
import gdshortener
import requests

s = gdshortener.ISGDShortener()

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def logo():
	print("\033[0;92m")
	os.system("clear")
	time.sleep(0.5)
	logopsb(" _____         _      _   _ ____  _     \n|_   _|____  _(_) ___| | | |  _ \| |    \n  | |/ _ \ \/ / |/ __| | | | |_) | |    \n  | | (_) >  <| | (__| |_| |  _ <| |___ \n  |_|\___/_/\_\_|\___|\___/|_| \_\_____|\n                                        ")
	logopsb("\033[3;90m			A Product Of ToxicNoob\033[0;92m")
	time.sleep(0.6)
	logopsb("\033[34m\n|****************************************************| \n|\033[3m Author   : DarkSlad3                               \033[0;34m|\n|\033[3m Tool     : ToxicURL	    	                     \033[0;34m|\n|\033[3m Version  : 1.0                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : DarkSlad3        		     	     \033[0;34m|\n******************************************************")
	time.sleep(0.8)

def choice():
	psb("\n[01] Mask A URL.")
	psb("[02] Short a URL (Using Cuttly).")
	psb("[03] Exit.")
	op = input("\n[*] Enter Your Choice:> 0")
	
	if op=="1":
		logo()
		mask()
	elif op=="2":
		logo()
		cuttly()
	elif op=="3":
		logo()
		exit()

def cuttly():
	api_key = "af8c6a9bebc3a7415ffe7d7f493c784f45718"
	url = input("\n\033[3;92m[*]Enter Your Long URL:> \033[34m")
	print("\033[92m")
	api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
	data = requests.get(api_url).json()["url"]
	if data["status"] == 7:
		shortened_url = data["shortLink"]
		print("\n[*] Your Shortened URL:", shortened_url)
	else:
		print("[!] Error Shortening URL:", data)

def mask():
	print("\n\033[03;92m")
	url = input("[*] Enter Your Real URL:> \033[34m")
	domain = input("\033[92m[*] Enter Your Domain Link (https://google.com, https://facebook.com):> \033[34m")
	txt = input("\033[92m[*] Enter Your Text (free-money, auto-like):> \033[34m")
	print("\033[92m")
	psb("[*] Please Wait....")
	time.sleep(1)

	if " " in txt:
		txt = txt.replace(" ", "-")
	if "/" in txt:
		txt = txt.replace("/", "-")
	if txt=="":
		txt = "auto-veriy"
	try:
		cmd = str(s.shorten(url))
	except:
		psb("[!] Something Went Wrong...")
		time.sleep(0.3)
		psb("[!] Please Check Your URL and try again later.")
		psb("[!] It is possible that, the URL you entered is in Blocklist of the server..")

	cmd = cmd.replace("(", "")
	cmd = cmd.replace(" ", "")
	cmd = cmd.replace(")", "")
	cmd = cmd.replace("none", "")
	cmd = cmd.replace("'", "")
	cmd = cmd.replace("None", "")
	cmd = cmd.replace(",", "")
	
	if txt in cmd:
		cmd = cmd.replace("https://", domain)
	
	else:
		cmd = cmd.replace("https://", domain+"-"+txt+"@")
	
	print("\n")
	psb("[!] Your Masked URL is::\n")
	time.sleep(0.5)
	print(cmd)

logo()
choice()

print("\n\033[0;37m")
