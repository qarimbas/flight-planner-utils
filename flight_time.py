from datetime import datetime, timedelta

# Input the Zulu time in HH:MM format
zulu_input = input("Enter the Zulu time of the flight (HH:MM): ")

# Parse the Zulu time
try:
    zulu_time = datetime.strptime(zulu_input, "%H:%M")
except ValueError:
    print("Invalid time format! Use HH:MM (e.g., 13:45)")
    #exit()
    zulu_time = datetime.strptime(zulu_input, "%H:%M")

# Convert Zulu time to local time (+3 hours)
local_time = zulu_time + timedelta(hours=3)

# Calculate go out time (local time - 1.5 hours)
go_out_time = local_time - timedelta(hours=1, minutes=30)

# Calculate wake up time based on breakfast availability
if go_out_time - timedelta(minutes=45) < datetime.strptime("06:00", "%H:%M"):
    deducted_time = 15  # No breakfast
    wake_up_time = go_out_time - timedelta(minutes=deducted_time)
else:
    deducted_time = 45  # Breakfast available
    wake_up_time = go_out_time - timedelta(minutes=deducted_time)

# Format output
print("\nFlight time conversions:")
print(f"Zulu time (flight): {zulu_time.strftime('%H:%M')}")
print(f"Local time (+3 hrs): {local_time.strftime('%H:%M')}")
print(f"Go out time (-1.5 hrs): {go_out_time.strftime('%H:%M')}")
print(f"Wake up time (-{deducted_time} mins): {wake_up_time.strftime('%H:%M')}")
