#!/usr/bin/python
# -*- coding: utf-8 -*

import requests,re,time,random ,os, sys, socket
from multiprocessing.dummy import Pool
from colorama import Fore

try:
    raw_input = input
except NameError:
    pass
os.system('cls')

print('''
    [1] From - > 'usings.ru'

    [2] From - > 'bitverzo.com'
    
    [3] From - > 'macrobyte.net'

    [4] From - > 'viewsforcash.com'
''')
maxishmidt = raw_input("\n\t[>] Choose which 'Api' / Number - > : ")

def getthatip1():
	FIRSTP = raw_input('\n\t[>] Frist Page : ')
	LASTP = raw_input('\n\t[>] Last Page : ')
	try:
		for page in range(int(FIRSTP), int(LASTP)):
			urls = 'http://usings.ru/bots.php?bot=&page='+str(page)
			DRZXQGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
			if 'IP' in DRZXQGET:
				REGEX = re.findall("[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}",DRZXQGET)
				for DRZXQ in REGEX:
					print('Grabbed IP - > ' + DRZXQ)
					open('../../../GrabbedIPs.txt','a').write(DRZXQ+'\n')
				else:
					print('[ Loading ... ]')
	except:
		pass

def getthatip2():
	FIRSTP = raw_input('\n\t[>] Frist Page : ')
	LASTP = raw_input('\n\t[>] Last Page : ')
	try:
		for page in range(int(FIRSTP), int(LASTP)):
			urls = 'http://bitverzo.com/recent_ip?p='+str(page)
			DRZXQGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
			if 'Recent IP reviews' in DRZXQGET:
				REGEX = re.findall('<a href="http://bitverzo.com/ip/(.*?)">',DRZXQGET)
				for DRZXQ in REGEX:
					print('Grabbed IP - > ' + DRZXQ)
					open('../../../GrabbedIPs.txt','a').write(DRZXQ+'\n')
				else:
					print('[ Loading ... ]')
	except:
		pass

def getthatip3():
	try:
		FIRSTP = raw_input('\n\t[>] Frist Page : ')
		LASTP = raw_input('\n\t[>] Last Page : ')
		ua = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
		}
		for page in range(int(FIRSTP), int(LASTP)):
			urls = "http://macrobyte.net/recent_ip?p="+str(page)
			DRZXQGET = requests.post(urls,headers=ua, timeout=10).text
			if 'Recent IP reviews' in DRZXQGET:
				REGEX = re.findall('<a href="http://macrobyte.net/ip/(.*?)">',DRZXQGET)
				for DRZXQ in REGEX:
					print('Grabbed IP - > ' + DRZXQ)
					open('../../../GrabbedIPs.txt','a').write(DRZXQ+'\n')
				else:
					print('[ Loading ... ]')
	except:
		pass

def getthatip4():
	try:
		FIRSTP = raw_input('\n\t[>] Frist Page : ')
		LASTP = raw_input('\n\t[>] Last Page : ')
		ua = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
		}
		for page in range(int(FIRSTP), int(LASTP)):
			urls = "http://viewsforcash.com/recent_ip?p="+str(page)
			DRZXQGET = requests.post(urls,headers=ua, timeout=10).text
			if 'Recent IP reviews' in DRZXQGET:
				REGEX = re.findall('<a href="http://viewsforcash.com/ip/(.*?)">',DRZXQGET)
				for DRZXQ in REGEX:
					print('Grabbed IP - > ' + DRZXQ)
					open('../../../GrabbedIPs.txt','a').write(DRZXQ+'\n')
				else:
					print('[ Loading ... ]')
	except:
		pass

def DELETE_DUPLICATE():
	with open('../../../GrabbedIPs.txt', 'r') as FIRSTPX:
		FIRSTPXX = list(dict.fromkeys(FIRSTPX.read().splitlines()))
		with open('../../../GrabbedIPs.txt.tmp','a') as new:
			new.write('\n'.join(FIRSTPXX))
			new.close()
		FIRSTPX.close()
	os.remove('../../../GrabbedIPs.txt')
	os.rename('../../../GrabbedIPs.txt.tmp','../../../GrabbedIPs.txt')

def Main():
	try:
		if maxishmidt == '1':
			getthatip1()
		elif maxishmidt == '2':
			getthatip2()
		elif maxishmidt == '3':
			getthatip3()
		elif maxishmidt == '4':
			getthatip4()
	except:
		pass

if __name__ == '__main__':
	Main()
	DELETE_DUPLICATE()