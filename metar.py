import requests

station = input("Enter ICAO station code (e.g. LTBD): ").strip().upper()

url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{station}.TXT"

response = requests.get(url)

if response.status_code == 200:
    lines = response.text.splitlines()
    # The METAR is usually the second line
    if len(lines) >= 2:
        print(f"METAR for {station}:\n{lines[1]}")
    else:
        print("No METAR data found.")
else:
    print(f"Failed to get data for {station}, status code: {response.status_code}")
