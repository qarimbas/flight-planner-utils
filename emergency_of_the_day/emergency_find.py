import datetime

def find_emergency(aircraft_type):
    try:
        with open('./emergency_of_the_day/emergencies.txt', 'r') as file:
            emergencies = file.readlines()
        
        # Get today's day number (1-based index)
        today = datetime.datetime.now().day

        # Skip the header row and iterate through the data
        for line in emergencies[1:]:  # Skip the header row
            columns = line.strip().split('\t')  # Split by tab
            if len(columns) < 4:
                continue  # Skip malformed rows
            
            # Unpack columns
            try:
                day = int(columns[0])  # Convert the first column (DAY) to an integer
            except ValueError:
                continue  # Skip rows where the day is not a valid integer
            
            c172s, da40, da42 = columns[1:]  # Extract the remaining columns
            if day == today:  # Match today's day
                if aircraft_type.lower() == "c172s":
                    return c172s.strip()
                elif aircraft_type.lower() == "da-40":
                    return da40.strip()
                elif aircraft_type.lower() == "da-42":
                    return da42.strip()
                else:
                    return "Invalid aircraft type. Please enter one of: C172S, DA-40, DA-42."
        
        return "No emergency found for today's date."
    except FileNotFoundError:
        return "The emergencies.txt file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    aircraft_type = input("Enter the aircraft type (C172S, DA-40, DA-42): ").strip()
    emergency = find_emergency(aircraft_type)
    print(f"Today's emergency: {emergency}")

if __name__ == "__main__":
    main()