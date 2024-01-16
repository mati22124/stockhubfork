from bs4 import BeautifulSoup
import requests
from openai import OpenAI
import re 
import os



def cnnScrapper(url):

  response = requests.get(url)
  
  soup = BeautifulSoup(response.text, 'html.parser')
  results = soup.find_all('p')
  title = soup.find_all('h1')
  
  title = re.sub("<.*?>", "", title[0].text)
  
  
  text = [i.text for i in results]
  
  article = ' '.join(text) #loops through each element in text and makes it into one string

  return title, article


def bbcScrapper(url):

  response = requests.get(url)
  
  soup = BeautifulSoup(response.text, 'html.parser')
  results = soup.find_all('p')
  title = soup.find_all('h1')
  
  title = re.sub("<.*?>", "", title[0].text)
  
  
  text = [i.text for i in results]
  
  article = ' '.join(text) #loops through each element in text and makes it into one string
  
  return title, article


