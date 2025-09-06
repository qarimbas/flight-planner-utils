from emergency_find import find_emergency
import datetime

def get_emergency_checklist(emergency_title, checklist_file_path):
    """
    Retrieve the full emergency checklist from the checklist file based on the emergency title.
    Handles main sections (e.g., 3.3) and subparts (e.g., 3.3.5, 3.3.6).
    """
    try:
        with open(checklist_file_path, 'r') as file:
            lines = file.readlines()
        
        # Normalize the emergency title for matching
        emergency_title = emergency_title.strip().lower()
        
        checklist = []
        found_title = False

        for line in lines:
            # Normalize the line for matching
            normalized_line = line.strip().lower()
            
            # Check if the line starts with the emergency title
            if normalized_line.startswith(emergency_title):
                found_title = True
                checklist.append(line.strip())  # Add the title to the checklist
                continue
            
            # If the title is found, collect lines until the next section or separator
            if found_title:
                if line.strip() == "---" or (line.strip().startswith("3.") and not line.strip().startswith(emergency_title)):
                    break  # Stop at the next section or separator
                checklist.append(line.strip())  # Add checklist items
        
        if checklist:
            return "\n".join(checklist)
        else:
            return f"No checklist found for the emergency: {emergency_title}"
    except FileNotFoundError:
        return f"The file {checklist_file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"

def find_next_emergency(aircraft_type, file_path, current_emergency):
    """
    Find the next emergency after the current emergency for the specified aircraft type.
    """
    try:
        with open(file_path, 'r') as file:
            emergencies = file.readlines()
        
        # Skip the header row and iterate through the data
        found_current = False
        for line in emergencies[1:]:  # Skip the header row
            columns = line.strip().split('\t')  # Split by tab
            if len(columns) < 4:
                continue  # Skip malformed rows
            
            day, c172s, da40, da42 = columns  # Unpack columns
            if aircraft_type.lower() == "da-40":
                if found_current:
                    return da40.strip()
                if da40.strip() == current_emergency:
                    found_current = True
        
        return "No next emergency found."
    except FileNotFoundError:
        return f"The file {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Step 1: Ask the user if they want today's or tomorrow's emergency
    choice = input("Do you want today's emergency or tomorrow's? (Enter 'today' or 'tomorrow'): ").strip().lower()
    
    if choice not in ['today', 'tomorrow']:
        print("Invalid choice. Please enter 'today' or 'tomorrow'.")
        return
    
    # Step 2: Find today's emergency
    emergency_file_path = './emergency_of_the_day/emergencies.txt'
    aircraft_type = "DA-40"
    today_emergency = find_emergency(aircraft_type, emergency_file_path)
    
    if choice == 'today':
        emergency = today_emergency
    elif choice == 'tomorrow':
        emergency = find_next_emergency(aircraft_type, emergency_file_path, today_emergency)
    
    print(f"{choice.capitalize()}'s emergency for {aircraft_type}: {emergency}")
    
    # Step 3: Extract the emergency title (before the slash '/')
    if '/' in emergency:
        emergency_title = emergency.split('/')[0].strip()
    else:
        emergency_title = emergency.strip()
    
    # Step 4: Find the checklist for the emergency title
    checklist_file_path = './emergency_of_the_day/da40_emergencies.txt'
    checklist = get_emergency_checklist(emergency_title, checklist_file_path)
    
    print("\nEmergency Checklist:")
    print(checklist)

if __name__ == "__main__":
    main()