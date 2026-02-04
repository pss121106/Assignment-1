import time

# --- 1. INITIALIZE DATABASE ---
def init_database():
    """Returns 4 lists pre-populated with at least 5 Star Trek characters."""
    names = ["Jean-Luc Picard", "William Riker", "Data", "Worf", "Geordi La Forge"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divs  = ["Command", "Command", "Operations", "Security", "Engineering"]
    ids   = ["101", "102", "103", "104", "105"]
    return names, ranks, divs, ids

# --- 2. DISPLAY MENU ---
def display_menu():
    """Prints options and returns the user's choice."""
    print("\n--- FLEET COMMAND MENU ---")
    print("1. View Roster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count High Officers")
    print("9. Exit")
    return input("Select option: ")

# --- 3. ADD MEMBER ---
def add_member(names, ranks, divs, ids):
    print("\n--- ADD CREW MEMBER ---")
    new_id = input("Enter new ID: ")
    
    # Validate ID is unique
    if new_id in ids:
        print("Error: ID already exists.")
        return

    new_rank = input("Enter Rank (Captain, Commander, Lieutenant, Ensign): ")
    valid_ranks = ["Captain", "Commander", "Lieutenant", "Ensign", "Lt. Commander"]
    
    # Validate Rank
    if new_rank not in valid_ranks:
        print("Error: Invalid Rank.")
        return

    new_name = input("Enter Name: ")
    new_div = input("Enter Division: ")

    # Append to all 4 lists to keep them parallel
    ids.append(new_id)
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    print("Crew member added successfully.")

# --- 4. REMOVE MEMBER ---
def remove_member(names, ranks, divs, ids):
    print("\n--- REMOVE CREW MEMBER ---")
    target_id = input("Enter ID to remove: ")

    # Check existence to prevent ValueError crash
    if target_id in ids:
        idx = ids.index(target_id)
        
        # Remove from all lists using the same index
        removed_name = names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print(f"{removed_name} (ID: {target_id}) removed.")
    else:
        print("Error: ID not found.")

# --- 5. UPDATE RANK ---
def update_rank(names, ranks, ids):
    print("\n--- UPDATE RANK ---")
    target_id = input("Enter ID to update: ")

    if target_id in ids:
        idx = ids.index(target_id)
        current_rank = ranks[idx]
        print(f"Current rank for {names[idx]}: {current_rank}")
        
        new_rank = input("Enter new rank: ")
        ranks[idx] = new_rank # Update only the rank list at that index
        print("Rank updated.")
    else:
        print("Error: ID not found.")

# --- 6. DISPLAY ROSTER ---
def display_roster(names, ranks, divs, ids):
    print("\n--- CURRENT ROSTER ---")
    print(f"{'ID':<10} {'Name':<20} {'Rank':<15} {'Division':<15}")
    print("-" * 60)
    
    # Iterate through the lists using range(len())
    for i in range(len(names)):
        print(f"{ids[i]:<10} {names[i]:<20} {ranks[i]:<15} {divs[i]:<15}")

# --- 7. SEARCH CREW ---
def search_crew(names, ranks, divs, ids):
    query = input("Enter name to search: ").lower()
    found = False
    
    print("\nSearch Results:")
    for i in range(len(names)):
        if query in names[i].lower():
            print(f"Found: {names[i]} - {ranks[i]} - {divs[i]} (ID: {ids[i]})")
            found = True
            
    if not found:
        print("No matches found.")

# --- 8. FILTER BY DIVISION ---
def filter_by_division(names, divs):
    target_div = input("Enter Division to filter (Command, Operations, Sciences): ")
    print(f"\n--- {target_div.upper()} DIVISION ---")
    
    found_any = False
    for i in range(len(names)):
        if divs[i].lower() == target_div.lower():
            print(f"{names[i]}")
            found_any = True
            
    if not found_any:
        print("No crew found in this division.")

# --- 9. CALCULATE PAYROLL ---
def calculate_payroll(ranks):
    total_cost = 0
    # Assign values to ranks
    pay_scale = {
        "Captain": 1000,
        "Commander": 800,
        "Lt. Commander": 700,
        "Lieutenant": 500,
        "Ensign": 200
    }
    
    for rank in ranks:
        # get(rank, 0) returns 0 if the rank isn't in the dictionary
        total_cost += pay_scale.get(rank, 0)
        
    return total_cost

# --- 10. COUNT OFFICERS ---
def count_officers(ranks):
    count = 0
    for rank in ranks:
        # The logic fix from our previous chat
        if rank == "Captain" or rank == "Commander":
            count += 1
    return count

# --- MAIN SYSTEM LOOP ---
def run_system_monolith():
    print("BOOTING SYSTEM...")
    time.sleep(1)
    print("WELCOME TO FLEET COMMAND")
    
    # 1. Initialize the parallel lists
    names, ranks, divs, ids = init_database()
    
    while True:
        # 2. Display menu and get choice
        choice = display_menu()
        
        # Route the choice to the correct function
        if choice == "1":
            display_roster(names, ranks, divs, ids)
        elif choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "4":
            update_rank(names, ranks, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            cost = calculate_payroll(ranks)
            print(f"Total Monthly Payroll: {cost} credits")
        elif choice == "8":
            officers = count_officers(ranks)
            # Fix: Ensure we convert int to str for printing
            print("High ranking officers: " + str(officers))
        elif choice == "9":
            print("Shutting down...")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    run_system_monolith()
