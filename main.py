# ============================================
# University Course Registration System
# Main Program File
# ============================================
# Team Members:
# - Ahmed Amir Ibrahim (202507440)
# - Ahmed Hisham Saad (202506915)
# - Reda Mahmoud Ali (202507258)
# ============================================

# Import modules
from file_operations import *
from calculations import *
from interface import *

# ============================================
# Main Program
# ============================================

def main():
    """
    Main function - Entry point of the program
    """
    # Initialize data files
    initialize_files()
    
    # Welcome message
    print("="*50)
    print("   University Course Registration System")
    print("="*50)
    print()
    
    # Main loop
    while True:
        # Login
        user_type, user_id = login()
        
        if user_type == "admin":
            admin_menu()
        elif user_type == "student":
            student_menu(user_id)
        else:
            print("Invalid login. Try again.")
            continue
        
        # Ask to continue or exit
        choice = input("\nDo you want to login again? (y/n): ")
        if choice.lower() != 'y':
            print("\nThank you for using the system. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
