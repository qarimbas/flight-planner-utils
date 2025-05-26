from datetime import datetime, timedelta

while True:
    # Input the Zulu time in HH:MM or HHMM format with error handling
    while True:
        zulu_input = input("Enter the Zulu time of the flight (HH:MM or HHMM): ")
        try:
            # Try parsing the input in HH:MM format
            zulu_time = datetime.strptime(zulu_input, "%H:%M")
            break
        except ValueError:
            try:
                # Try parsing the input in HHMM format
                zulu_time = datetime.strptime(zulu_input, "%H%M")
                break
            except ValueError:
                print("Invalid time format! Please use HH:MM (e.g., 13:45) or HHMM (e.g., 1345). Try again.")

    # Convert Zulu time to local time (+3 hours)
    local_time = zulu_time + timedelta(hours=3)

    # Calculate hotel exit time (local time - 1.5 hours)
    hotel_exit_time = local_time - timedelta(hours=1, minutes=30)

    # Calculate wake up time based on breakfast availability
    if hotel_exit_time - timedelta(minutes=45) < datetime.strptime("06:00", "%H:%M"):
        deducted_time = 15  # No breakfast
        wake_up_time = hotel_exit_time - timedelta(minutes=deducted_time)
    else:
        deducted_time = 45  # Breakfast available
        wake_up_time = hotel_exit_time - timedelta(minutes=deducted_time)

    # Format output
    print("\nFlight time conversions:")
    print(f"Zulu time (flight): {zulu_time.strftime('%H:%M')}")
    print(f"Local time (+3 hrs): {local_time.strftime('%H:%M')} (local)")
    print(f"Hotel exit time (-1.5 hrs): {hotel_exit_time.strftime('%H:%M')} (local)")
    print(f"Wake up time (-{deducted_time} mins): {wake_up_time.strftime('%H:%M')} (local)")

    # Ask the user if they want to enter another time
    while True:
        another = input("\nDo you want to enter another time? (yes/no): ").strip().lower()
        if another == "yes":
            break  # Continue the loop to enter another time
        elif another == "no":
            print("Have a safe flight!")
            exit()  # Exit the program
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
