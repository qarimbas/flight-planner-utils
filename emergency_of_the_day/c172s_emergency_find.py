from emergency_find import find_emergency

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

def main():
    # Step 1: Find today's emergency for C172S
    emergency_file_path = './emergency_of_the_day/emergencies.txt'
    aircraft_type = "C172S"
    emergency = find_emergency(aircraft_type, emergency_file_path)
    
    print(f"Today's emergency for {aircraft_type}: {emergency}")
    
    # Step 2: Extract the emergency title (before the slash '/')
    if '/' in emergency:
        emergency_title = emergency.split('/')[0].strip()
    else:
        emergency_title = emergency.strip()
    
    # Step 3: Find the checklist for the emergency title
    checklist_file_path = './emergency_of_the_day/c172s_emergencies.txt'
    checklist = get_emergency_checklist(emergency_title, checklist_file_path)
    
    print("\nEmergency Checklist:")
    print(checklist)

if __name__ == "__main__":
    main()