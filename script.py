import requests
from bs4 import BeautifulSoup
import time
import sendemail
import sys

email = str(input("Wat is je Gmail account? "))
wachtwoord = str(input("Wat is je wachtwoord? "))


url = "https://www.rijksoverheid.nl/onderwerpen/coronavirus-vaccinatie/prikuitnodiging-en-afspraak"
interval = 30

jaar1 = str("1991")
jaar2 = str("1992")
jaar3 = str("2000")


def coronachecker():
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    lijst = soup.find_all("strong")

    letters = []
    for a in lijst:
        text = a.get_text()
        letters.append(text)

    if any(jaar1 in s for s in letters) or any(jaar2 in s for s in letters) or any(jaar3 in s for s in letters):
        notify()
    else:
        return False


def notify():
    try:
        sendemail.emailuser(email, wachtwoord)
        sys.exit()
    except:
        print("Je email of wachtwoord is verkeerd ingesteld. Start het programma opnieuw met correcte gegevens.")


if __name__ == "__main__":
    while True:
        try:
            coronachecker()
            time.sleep(interval)
        except:
            time.sleep(60)
