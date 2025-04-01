import os
import importlib
import sys
from pathlib import Path

def get_scripts_path():
    """Dynamically locate the scripts directory"""
    package_dir = Path(__file__).parent.parent  # atari_monk_django directory
    return package_dir / "scripts"

def list_scripts(scripts_path):
    return [
        f.stem for f in scripts_path.glob("*.py") 
        if f.is_file() and f.name != Path(__file__).name
    ]

def display_menu(scripts):
    print("\n📜 Available Scripts:")
    for idx, script in enumerate(scripts, 1):
        print(f"  {idx}. {script}")
    print("  0. Exit")

def run_script(script_name):
    """Run script by importing its main function"""
    module_name = f"atari_monk_django.scripts.{script_name}"
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, 'main'):
            print(f"\n🚀 Running {script_name}...\n")
            module.main()
        else:
            print(f"❌ {script_name} has no 'main' function")
    except ImportError as e:
        print(f"❌ Failed to import {script_name}: {str(e)}")

def master_scripts():
    scripts_path = get_scripts_path()
    print(f"🔍 Looking for scripts in: {scripts_path}")
    
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
                run_script(scripts[choice - 1])
            else:
                print("⚠️ Invalid choice. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    master_scripts()