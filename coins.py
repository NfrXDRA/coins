import os

os.system('clear')
name ='''\033[1;36m  _____   _____   _   __   _   _____  
/  ___| /  _  \ | | |  \ | | /  ___/ 
| |     | | | | | | |   \| | | |___  
| |     | | | | | | | |\   | \___  \ 
| |___  | |_| | | | | | \  |  ___| | 
\_____| \_____/ |_| |_|  \_| /_____/ 



 __   _   _____   _____   
|  \ | | |  ___| |  _  \  
|   \| | | |__   | |_| |  
| |\   | |  __|  |  _  /  
| | \  | | |     | | \ \  
|_|  \_| |_|     |_|  \_\ 
insta:   x_nikename     Telegram:   @virusmain
'''
print (name)

import getpass
import amino
e=input('\033[1;34m Enter Email:  ')
p=getpass.getpass('\033[1;37m Enter Password:   ')
clint=amino.Client()
clint.login(email=e,password=p)
transactionId=clint.get_wallet_history(start=0,size=1).transanctionId
print ('\033[1;31m transactionId:      ',transactionId)
url=input('\033[1;32m Enter chat url:     ')
infurl=amino.Client().get_from_code(url)
chatId=infurl.objectId
comId=infurl.path[1:infurl.path.index("/")]
subclint=amino.SubClient(comId=comId,profile=clint.profile)
t = input ('\033[1;32m Enter transId:   ')
co = input ('\033[1;32m number coins: Donate   ')
while True:
	subclint.send_coins(transactionId=t,coins=co,chatId=chatId)
	print("\033[1;32m \n \n \n Finished \n \n \n \n \n \n \n \n \n")
