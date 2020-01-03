#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords

while(1):
    print("\n Enter the website: ")
    site=str(input())
    response=urllib.request.urlopen(site)
    html=response.read()
    soup=BeautifulSoup(html,'html5lib')
    text=soup.get_text(strip=True)
    tokens=[t for t in text.split()]
    clean_tokens=tokens[:]
    sr=stopwords.words('English')
    for token in tokens:
        if token in sr:
            clean_tokens.remove(token)
    freq=nltk.FreqDist(clean_tokens)
    maxv=0
    max2=0
    for k,v in freq.items():
        if(v>maxv):
            maxv=v
            reqkey=k
        elif(v>max2):
            max2=v
            reqkey2=k
    print("Is this Website About "+str(k)+'? \n Press 1 for yes\n 2 for no')
    ans=int(input())
    if(ans==2):
        print("\n Then it must be "+ str(max2))
    print('\n Do you wish to continue? (y or n): ')
    ch=str(input())
    if(ch=='n'):
        break

