✈️ Flight Planner Utils
A collection of simple Python scripts to help you prepare for flights.
Quickly convert Zulu (UTC) times to local time (+3 hrs), calculate go-out time, and determine wake-up times for your flights.
Additionally, fetch current METAR and TAF weather reports for any airport.

📦 Features
Convert Zulu (UTC) flight time to local time (+3 hrs)

Calculate go-out time (local time - 1.5 hrs)

Calculate wake-up time (go-out time - 45 mins)

Fetch METAR weather reports for any ICAO airport code

Fetch TAF weather forecasts for any ICAO airport code

Simple command-line interface – just enter your inputs and get your results instantly!

🚀 Usage
1️⃣ Clone this repository:

bash
Copy
Edit
git clone https://github.com/YOURUSERNAME/flight-planner-utils.git
cd flight-planner-utils
2️⃣ Run the main script:

nginx
Copy
Edit
python flight_time_calc.py
3️⃣ Follow the prompts to:

Enter your flight’s Zulu time (HH:MM) for time calculations

Optionally fetch METAR or TAF reports by entering the ICAO code

🛠 Example Output
sql
Copy
Edit
Enter the Zulu time of the flight (HH:MM): 10:00

Flight time calculations:
Zulu time: 10:00
Local time (+3 hrs): 13:00
Go out time (-1.5 hrs): 11:30
Wake up time (-45 mins): 10:45

Do you want to fetch weather reports? (yes/no): yes
Enter ICAO airport code (e.g. LTBD): LTBD

Fetching METAR...
Raw METAR: LTBD 262051Z 26015KT 10SM FEW050 SCT100 BKN250 29/17 A2992 RMK AO2 SLP134 T02940167

Fetching TAF...
Raw TAF:
LTBD 262320Z 2624/2724 26015G25KT P6SM BKN050 
FM270000 24012KT P6SM SCT040 
FM270600 22010KT P6SM SCT025 
FM271200 22008KT P6SM SCT020
📜 License
MIT License — see LICENSE file.

📝 Author
Created by [qarimbas] ✈️

