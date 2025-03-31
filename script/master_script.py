import os
import subprocess

def list_scripts():
    scripts = [f for f in os.listdir() if f.endswith(".py") and f != "master_script.py"]
    return scripts

def display_menu(scripts):
    print("\n📜 Available Scripts:")
    for idx, script in enumerate(scripts, 1):
        print(f"  {idx}. {script}")
    print("  0. Exit")

def run_script(script_name):
    print(f"\n🚀 Running {script_name}...\n")
    subprocess.run(["python", script_name])

def main():
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
