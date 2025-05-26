import requests
from bs4 import BeautifulSoup

icao = input("Enter ICAO code (e.g. LTBD): ").strip().upper()
url = f"https://notaminfo.com/{icao}"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    notams = soup.find_all("div", class_="notam-text")
    if notams:
        print(f"NOTAMs for {icao}:")
        for notam in notams:
            print(notam.get_text(strip=True))
    else:
        print("No NOTAMs found or page format changed.")
else:
    print(f"Failed to fetch NOTAMs for {icao}.")
