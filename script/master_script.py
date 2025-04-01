import os
import subprocess

SCRIPTS_PATH = r"C:\atari-monk\code\django\script" 

def list_scripts():
    
    scripts = [
        f for f in os.listdir(SCRIPTS_PATH) 
        if f.endswith(".py") and f != os.path.basename(__file__)
    ]
    return scripts

def display_menu(scripts):
    print("\n📜 Available Scripts:")
    for idx, script in enumerate(scripts, 1):
        print(f"  {idx}. {script}")
    print("  0. Exit")

def run_script(script_name):
    
    script_path = os.path.join(SCRIPTS_PATH, script_name)
    print(f"\n🚀 Running {script_name}...\n")
    subprocess.run(["python", script_path])

def main():
    print(f"🔍 Looking for scripts in: {os.path.abspath(SCRIPTS_PATH)}")
    
    while True:
        scripts = list_scripts()
        if not scripts:
            print("❌ No scripts found in the folder.")
            break

        display_menu(scripts)

        try:
            choice = int(input("\n🔢 Enter the script number to run (0 to exit): "))
            if choice == 0:
                print("👋 Exiting...")
                break
            elif 1 <= choice <= len(scripts):
                run_script(scripts[choice - 1])
            else:
                print("⚠️ Invalid choice. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()