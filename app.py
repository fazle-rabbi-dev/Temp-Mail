# Author: Fazle Rabbi
# Date: 28 November, 2022
# WARNING: Changing Credit don't made you a coder.So, don't change my Credit! You can take some knowledge from this code.
# The code of this project is open source because I want another learner to learn a little by looking at this code.

# Dependencies:
from time import sleep
import requests,json,os,sys

# Global Variables:
address_url='https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1'
inbox_url='https://www.1secmail.com/api/v1/?action=getMessages&login=demo&domain=1secmail.com'

# Clear Terminal:
def clear():
   os.system('clear')

clear()

# Colors:
rd='\033[1;91m'
gr='\033[1;92m'
yl='\033[1;93m'
bl='\033[1;94m'
pr='\033[1;95m'
cy='\033[1;96m'
wh='\033[1;97m'

# Banner:
def banner():
   print(f"""
   
   {rd}╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭━╮╭━╮╱╱╱╭╮
   {gr}┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╰╯┃┃╱╱╱┃┃
   {rd}╰╯┃┃┣┻━┳╮╭┳━━╮╱╱┃╭╮╭╮┣━━┳┫┃
   {cy}╱╱┃┃┃┃━┫╰╯┃╭╮┣━━┫┃┃┃┃┃╭╮┣┫┃
   {yl}╱╱┃┃┃┃━┫┃┃┃╰╯┣━━┫┃┃┃┃┃╭╮┃┃╰╮
   {rd}╱╱╰╯╰━━┻┻┻┫╭━╯╱╱╰╯╰╯╰┻╯╰┻┻━╯
   {gr}╱╱╱╱╱╱╱╱╱╱┃┃
   {pr}╱╱╱╱╱╱╱╱╱╱╰╯
   
   {wh}>> {bl}Coded By {rd}Fazle Rabbi
   {wh}>> {bl}https://github.com/fh-rabbi
   """)

# Menu:
def menu():
   clear()
   banner()
   try:
      file = open('mail.txt')
      mail = file.read()
      print(f"   {wh}>> {cy}Current Email: {yl}{mail}{yl}")
   except:
      pass
   print(f"""
   {yl}[{rd}1{yl}]{wh} {gr}Generate New Address
   {yl}[{rd}2{yl}]{wh} {gr}View Inbox
   {yl}[{rd}3{yl}]{wh} {gr}View Message
   {yl}[{rd}4{yl}]{wh} {gr}View Inbox {rd}Specific
   {yl}[{rd}5{yl}]{wh} {gr}View Message {rd}Specific
   {yl}[{rd}0{yl}]{wh} {gr}Exit
   """)
   
   option = input(f"   {wh}[*] {cy}Choose An Option:")
   if option == '1':
      generateAddress()
   elif option == '2':
      clear()
      ViewInbox()
   elif option == '3':
      clear()
      ViewMessage()
   elif option == '4':
      clear()
      ViewInboxSpecific()
   elif option == '5':
      clear()
      ViewMessageSpecific()
   elif option == '0':
      clear()
      print(f"{rd}[*] Quiting..")
      sleep(1)
      clear()
      os.system('exit 0')
   else:
      print(f"   {rd}[*] Invalid Option!")
      sleep(1)
      menu()
   
# Generate New Address:
def generateAddress():
   clear()
   print(f'{wh}[*] {cy}Generating Address..{wh}')
   try:
      res = requests.get(address_url)
      address = json.loads(res.text)
      address = address[0]
      # Save Email In A File:
      file = open("mail.txt", "w")
      file.write(address)
      file.close()
      print(f"[*] {cy}Your Temp-Mail: {gr}{address}{wh}")
      print(f'{gr}NOTE: {rd}Copy This Email Address!{wh}')
      opt = input(f'[*] {gr}Press Any Key For Main Menu:')
      if opt == 'M' or opt == 'm':
         sleep(1)
         clear()
         menu()
      else:
         sleep(1)
         clear()
         menu()
   except:
      print(f"{rd}[!] Something Went Wrong!{wh}")
      sleep(1)
      menu()

# Inbox For Current Address:
def ViewInbox():
   # mail = input(f"{wh}[*] {gr}Enter Your Email:")
   try:
      file = open('mail.txt')
      mail = file.read()
   except:
      print(f"[*] Email Address Not Found!")
      sleep(1)
      input(f"{wh}[*] {gr}Enter Your Email:")
   text = f'{yl}[*] Loading Your Inbox..'
   for char in text:
      sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
   print('')
   # print(mail)
   if '@' in mail:
      index = mail.index('@')
      name = mail[0:index]
      domain = mail[index+1:]
      # print("Name:"+name)
      # print("Domain:"+domain)
      try:
         res = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}")
         inbox_data = json.loads(res.text)
         if len(inbox_data) > 0:
            clear()
            print(f"""
   {wh}|======================|{wh}
   {wh}|        {rd}INBOX{wh} ({len(inbox_data)})     |{wh}
   {wh}|======================|{wh}
            """)
            # print(json.dumps(inbox_data,indent=4))
            
            # Print The Inbox Data:
            for data in inbox_data:
               # print('ok')
               # print(data['id'])
               print(f"""
{wh}>> EMAIL:
{gr}>> {pr}id:{gr}{data['id']}
{gr}>> {pr}from:{gr}{data['from']}
{gr}>> {pr}subject:{gr}{data['subject']}
{gr}>> {pr}date:{gr}{data['date']}
               """)
            
            # Read From User:
            opt =input(f'{bl}[*] Press Any Key For Main Menu:{wh}')
            if opt:
               menu()
            else:
               menu()
         else:
            clear()
            print(f"""
   {wh}|======================|{wh}
   {wh}|        {rd}INBOX{wh}         |{wh}
   {wh}|======================|{wh}

{bl}>> Current Email Address:{gr} {mail}
{cy}>> You have not any incomming email!
            """)
            opt =input(f'{pr}[*] Press Any Key For Main Menu:{wh}')
            if opt:
               menu()
            else:
               menu()
      except:
         # print('')
         print(f"{rd}[!] Internet Connection Error!")
         sleep(1)
         menu()
   else:
      # print('')
      print(f"{wh}[*] {rd}Invalid Email Address!")
      sleep(1)
      menu()

# View Messages Of Current Email Address:
def ViewMessage():
   clear()
   sleep(1)
   # mail = input(f"{pr}[*] Enter Your Email Address:{wh}")
   try:
      file = open('mail.txt','r')
      mail = file.read()
   except:
      print(f"{rd}[!] Email Address Not Found!")
      sleep(1)
      print(f"{bl}[*] Please Enter Email Address Manually")
      mail = input(f"{pr}[*] Enter Your Email Address:{wh}")
   if '@' in mail:
      index = mail.index('@')
      name = mail[0:index]
      domain = mail[index+1:]
      mail_id = input(f"{pr}[*] Enter A Message Id:{wh}")
      # print(name,domain,mail_id)
      try:
         res = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={name}&domain={domain}&id={mail_id}')
         # res = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={name}&domain={domain}&id={ID}')
         mail_data = json.loads(res.text)
         print('\n')
         print(f"{rd}>> {yl}From:{gr}{mail_data['from']}")
         print(f"{rd}>> {yl}Subject:{gr}{mail_data['subject']}")
         print(f"{rd}>> {yl}Date:{gr}{mail_data['date']}")
         print(f"{rd}>> {yl}Message:{gr}{mail_data['textBody']}{wh}")
         # print(json.dumps(mail_data,indent=4))
         opt = input(f"[*] Press Any Key For Menu:")
         if not opt:
            clear()
            menu()
      except:
         print(f"{rd}[*] Something Went Wrong!{wh}")
         sleep(1)
         menu()
   else:
      print(f"{rd}[*] Invalid Email!{wh}")
      sleep(1)
      clear()
      menu()
   
# Inbox For A Specific Address:
def ViewInboxSpecific():
   mail = input(f"{wh}[*] {gr}Enter Your Email:")
   text = f'{yl}[*] Loading Your Inbox..'
   for char in text:
      sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
   print('')
   # print(mail)
   if '@' in mail:
      index = mail.index('@')
      name = mail[0:index]
      domain = mail[index+1:]
      # print("Name:"+name)
      # print("Domain:"+domain)
      try:
         res = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}")
         inbox_data = json.loads(res.text)
         if len(inbox_data) > 0:
            clear()
            print(f"""
   {wh}|======================|{wh}
   {wh}|        {rd}INBOX{wh} ({len(inbox_data)})     |{wh}
   {wh}|======================|{wh}
            """)
            # print(json.dumps(inbox_data,indent=4))
            
            # Print The Inbox Data:
            for data in inbox_data:
               # print('ok')
               # print(data['id'])
               print(f"""
{wh}>> EMAIL:
{gr}>> {pr}id:{gr}{data['id']}
{gr}>> {pr}from:{gr}{data['from']}
{gr}>> {pr}subject:{gr}{data['subject']}
{gr}>> {pr}date:{gr}{data['date']}
               """)
            
            # Read From User:
            opt =input(f'{bl}[*] Press Any Key For Main Menu:{wh}')
            if opt:
               menu()
            else:
               menu()
         else:
            clear()
            print(f"""
   {wh}|======================|{wh}
   {wh}|        {rd}INBOX{wh}         |{wh}
   {wh}|======================|{wh}

{cy}>> You have not any incomming email!
            """)
            opt =input(f'{pr}[*] Press Any Key For Main Menu:{wh}')
            if opt:
               menu()
            else:
               menu()
      except:
         # print('')
         print(f"{rd}[!] Internet Connection Error!")
         sleep(1)
         menu()
   else:
      # print('')
      print(f"{wh}[*] {rd}Invalid Email Address!")
      sleep(1)
      menu()
   
# Read Message For A Specific Address:
def ViewMessageSpecific():
   clear()
   sleep(1)
   mail = input(f"{pr}[*] Enter Your Email Address:{wh}")
   if '@' in mail:
      index = mail.index('@')
      name = mail[0:index]
      domain = mail[index+1:]
      mail_id = input(f"{pr}[*] Enter A Message Id:{wh}")
      # print(name,domain,mail_id)
      try:
         res = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={name}&domain={domain}&id={mail_id}')
         # res = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={name}&domain={domain}&id={ID}')
         mail_data = json.loads(res.text)
         print('\n')
         print(f"{rd}>> {yl}From:{gr}{mail_data['from']}")
         print(f"{rd}>> {yl}Subject:{gr}{mail_data['subject']}")
         print(f"{rd}>> {yl}Date:{gr}{mail_data['date']}")
         print(f"{rd}>> {yl}Message:{gr}{mail_data['textBody']}{wh}")
         # print(json.dumps(mail_data,indent=4))
         opt = input(f"[*] Press Any Key For Menu:")
         if not opt:
            clear()
            menu()
      except:
         print(f"{rd}[*] Something Went Wrong!{wh}")
         sleep(1)
         menu()
   else:
      print(f"{rd}[*] Invalid Email!{wh}")
      sleep(1)
      clear()
      menu()

menu()
