import requests
import re

def fetch_taf(icao_code):
    """
    Fetch TAF data for a given ICAO airport code.
    """
    url = f"https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/{icao_code}.TXT"
    try:
        response = requests.get(url)
        response.raise_for_status()
        taf_data = response.text.strip()
        return taf_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TAF data: {e}")
        return None

def parse_taf(taf_text):
    """
    Parse TAF data to extract detailed information.
    """
    # Preprocess TAF text to remove headers or metadata
    taf_text = taf_text.strip()
    taf_lines = taf_text.splitlines()
    for line in taf_lines:
        if line.startswith("TAF"):  # Find the line starting with "TAF"
            taf_text = line + " " + " ".join(taf_lines[taf_lines.index(line) + 1:]).strip()
            break

    parsed_data = {}

    # Extract station code
    station_match = re.match(r'^[A-Z]{4}', taf_text)
    parsed_data['station'] = station_match.group(0) if station_match else None

    # Extract issue time
    issue_time_match = re.search(r'\d{6}Z', taf_text)
    parsed_data['issue_time'] = issue_time_match.group(0) if issue_time_match else None

    # Extract validity period
    validity_match = re.search(r'\d{4}/\d{4}', taf_text)
    parsed_data['validity'] = validity_match.group(0) if validity_match else None

    # Extract detailed forecast segments
    forecast_pattern = re.compile(
        r'(FM\d{6}|BECMG|TEMPO|PROB\d{2}) .*?(?= FM\d{6}| BECMG| TEMPO| PROB\d{2}|$)', re.DOTALL
    )
    forecast_data = []
    for match in forecast_pattern.finditer(taf_text):
        segment = match.group(0).strip()
        forecast_details = {}

        # Extract type (FM, BECMG, TEMPO, PROB)
        type_match = re.search(r'FM\d{6}|BECMG|TEMPO|PROB\d{2}', segment)
        forecast_details['type'] = type_match.group(0) if type_match else None

        # Extract wind
        wind_match = re.search(r'\d{3}\d{2}KT|VRB\d{2}KT', segment)
        forecast_details['wind'] = wind_match.group(0) if wind_match else None

        # Extract visibility
        visibility_match = re.search(r'(CAVOK|\d{4}(?=\s))', segment)
        forecast_details['visibility'] = visibility_match.group(0) if visibility_match and visibility_match.group(0) != parsed_data['validity'] else None

        # Extract weather conditions
        weather_match = re.search(r'(TSRA|SHRA|RA|SN|FG|BR|HZ|FU|DU|SA|SQ|VC|MI|BC|PR|DR|BL|SH|FZ|DZ|PL|GR|GS|UP)', segment)
        forecast_details['weather'] = weather_match.group(0) if weather_match else None

        # Extract cloud coverage
        cloud_match = re.findall(r'(FEW\d{3}|SCT\d{3}|BKN\d{3}|OVC\d{3}|NSC)', segment)
        forecast_details['clouds'] = cloud_match if cloud_match else None

        forecast_data.append(forecast_details)

    parsed_data['forecast'] = forecast_data

    return parsed_data

if __name__ == "__main__":
    # Prompt user for ICAO code
    icao_code = input("Enter ICAO airport code: ").strip().upper()
    taf_data = fetch_taf(icao_code)
    
    if taf_data:
        print("\nRaw TAF Data:")
        print(taf_data)

        parsed_taf = parse_taf(taf_data)
        print("\nParsed TAF Data:")
        for key, value in parsed_taf.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve TAF data.")