import requests
import re

def fetch_metar(icao_code):
    """
    Fetch METAR data for a given ICAO airport code.
    """
    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{icao_code}.TXT"
    try:
        response = requests.get(url)
        response.raise_for_status()
        metar_data = response.text.strip()
        return metar_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching METAR data: {e}")
        return None

def parse_metar(metar):
    """
    Parse METAR data to extract useful information.
    """
    metar_pattern = re.compile(
        r"(?P<station>[A-Z]{4})\s"  # ICAO station code
        r"(?P<datetime>\d{6}Z)\s"  # Date and time
        r"(?P<wind>(VRB\d{2}KT|\d{3}\d{2}KT|\d{3}\d{2}KT\s\d{3}V\d{3})?)\s?"  # Wind (including variable wind and directional variations)
        r"(?P<visibility>\d{4}|CAVOK)?\s?"  # Visibility or CAVOK
        r"(?P<clouds>(FEW\d{3}|SCT\d{3}|BKN\d{3}|OVC\d{3}|NSC)?)\s?"  # Cloud coverage
        r"(?P<temperature>\d{2}/\d{2})?\s?"  # Temperature and dew point
        r"(?P<pressure>Q\d{4})?\s?"  # Pressure (QNH)
        r"(?P<remarks>.+)?"  # Remaining remarks (e.g., NOSIG)
    )
    match = metar_pattern.search(metar)
    if match:
        return match.groupdict()
    else:
        print("Failed to parse METAR data.")
        return None

if __name__ == "__main__":
    icao_code = input("Enter ICAO airport code: ").strip().upper()
    metar_data = fetch_metar(icao_code)
    if metar_data:
        print("Raw METAR Data:")
        print(metar_data)
        parsed_data = parse_metar(metar_data)
        if parsed_data:
            print("\nParsed METAR Data:")
            for key, value in parsed_data.items():
                print(f"{key}: {value}")