import os
import subprocess

def terminal_interface():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bin_dir = os.path.join(script_dir, "bin")  # Path to the bin directory
    
    while True:
        print("Terminal Interface")
        print("1. NOR (Execute \\bin\\nor.py)")
        print("2. Terminal (Execute \\bin\\terminal.py)")
        print("3. Exit")
        
        choice = input("Select an option (1, 2, or 3): ")

        if choice == "1":
            nor_path = os.path.join(bin_dir, "nor.py")
            if os.path.exists(nor_path):
                print(f"Executing {nor_path}...")
                subprocess.run(["python", nor_path], check=True)
            else:
                print(f"File not found: {nor_path}")
        elif choice == "2":
            terminal_path = os.path.join(bin_dir, "terminal.py")
            if os.path.exists(terminal_path):
                print(f"Executing {terminal_path}...")
                subprocess.run(["python", terminal_path], check=True)
            else:
                print(f"File not found: {terminal_path}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    terminal_interface()
