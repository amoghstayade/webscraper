import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

response = requests.get("https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html")
not_found = True
while (not_found):
    if ("#166" in response.text):
        not_found = False
        soup = BeautifulSoup(response.text, "html.parser")
        all_p = soup.findAll('p')
        report = all_p[12].text
        print("New report is available")
        for i in range(100):
            os.system('say "New report is available {}",'.format(report))
    # os.system('say "NADA",')
    time.sleep(60)
    