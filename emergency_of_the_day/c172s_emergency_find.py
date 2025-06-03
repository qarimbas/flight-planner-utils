from emergency_find import find_emergency
import datetime

def get_emergency_checklist(emergency_title, checklist_file_path):
    """
    Retrieve the full emergency checklist from the checklist file based on the emergency title.
    """
    try:
        with open(checklist_file_path, 'r') as file:
            lines = file.readlines()
        
        # Search for the emergency title in the checklist file
        checklist = []
        found_title = False
        for line in lines:
            if line.strip() == emergency_title:  # Match the exact title
                found_title = True
                checklist.append(line.strip())  # Add the title to the checklist
                continue
            
            if found_title:
                if line.strip() == "---":  # Stop when the separator is encountered
                    break
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
            if aircraft_type.lower() == "c172s":
                if found_current:
                    return c172s.strip()
                if c172s.strip() == current_emergency:
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
    aircraft_type = "C172S"
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
    checklist_file_path = './emergency_of_the_day/c172s_emergencies.txt'
    checklist = get_emergency_checklist(emergency_title, checklist_file_path)
    
    print("\nEmergency Checklist:")
    print(checklist)

if __name__ == "__main__":
    main()