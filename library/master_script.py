import os
import subprocess

def list_scripts(scripts_path):
    """List all Python scripts in the specified directory except the master script"""
    scripts = [
        f for f in os.listdir(scripts_path) 
        if f.endswith(".py") and f != os.path.basename(__file__)
    ]
    return scripts

def display_menu(scripts):
    print("\n📜 Available Scripts:")
    for idx, script in enumerate(scripts, 1):
        print(f"  {idx}. {script}")
    print("  0. Exit")

def run_script(script_name, scripts_path):
    """Run the selected script using the specified path"""
    script_path = os.path.join(scripts_path, script_name)
    print(f"\n🚀 Running {script_name}...\n")
    subprocess.run(["python", script_path])

def master_scripts(scripts_path=r"C:\atari-monk\code\django\script"):
    print(f"🔍 Looking for scripts in: {os.path.abspath(scripts_path)}")
    
    while True:
        scripts = list_scripts(scripts_path)
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
                run_script(scripts[choice - 1], scripts_path)
            else:
                print("⚠️ Invalid choice. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")
