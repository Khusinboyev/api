from requests import get
from bs4 import BeautifulSoup

url = "https://namozvaqti.uz/shahar/gazli"
resp = get(f"{url}")
soup = BeautifulSoup(resp.text, features="lxml")
bomdod = soup.find(id="bomdod").text
peshin = soup.find(id="peshin").text

print(bomdod, peshin)
