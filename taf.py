import requests

station = input("Enter ICAO station code (e.g. LTBD): ").strip().upper()

url = f"https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/{station}.TXT"

response = requests.get(url)

if response.status_code == 200:
    lines = response.text.splitlines()
    # The TAF is usually starting from the second line and can be multiline
    if len(lines) >= 2:
        print(f"TAF for {station}:")
        for line in lines[1:]:
            print(line)
    else:
        print("No TAF data found.")
else:
    print(f"Failed to get data for {station}, status code: {response.status_code}")
