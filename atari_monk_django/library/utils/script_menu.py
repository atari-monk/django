import os
import platform
from atari_monk_django.library.django.generate_project import generate_project
from atari_monk_django.library.django.generate_app import generate_app
from atari_monk_django.library.django.meta_model import save_meta_model
from atari_monk_django.library.django.model_class import save_model_class
from atari_monk_django.library.django.generate_model import apply_model
from atari_monk_django.library.django.setup_urls_and_views import setup_urls_and_views
from atari_monk_django.library.utils.remove_comments import remove_comments_from_file
from atari_monk_django.library.utils.markdown_to_text import markdown_to_text_using_clipboard
from atari_monk_django.library.django.setup_django import install_django, check_django_installed

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

SCRIPTS = [
    {"name": "Generate django Project", "func": generate_project},
    {"name": "Generate django App", "func": generate_app},
    {"name": "Generate django Meta Model", "func": save_meta_model},
    {"name": "Generate django Model Class", "func": save_model_class},
    {"name": "Apply django Model", "func": apply_model},
    {"name": "Setup django urls and Views", "func": setup_urls_and_views},
    {"name": "Remove comments from file", "func": remove_comments_from_file},
    {"name": "Markdown to text", "func": markdown_to_text_using_clipboard},
    {"name": "Setup django", "func": lambda: (
        print("🚀 Setting up Django...\n"),
        install_django(),
        check_django_installed(verbose=True)
    )},
    {"name": "Clear screen", "func": clear_screen},
]

def display_menu():
    print("\n📜 Available Scripts:")
    for idx, script in enumerate(SCRIPTS, 1):
        print(f"  {idx}. {script['name']}")
    print("  0. Exit")

def script_menu():
    while True:
        display_menu()

        try:
            choice = int(input("\n🔢 Enter the script number to run (0 to exit): "))
            if choice == 0:
                clear_screen()
                break
            elif 1 <= choice <= len(SCRIPTS):
                print(f"\n🚀 Running {SCRIPTS[choice-1]['name']}...\n")
                SCRIPTS[choice-1]["func"]()
                if SCRIPTS[choice-1]["name"] != "Clear screen":
                    input("\nPress Enter to continue...")
                clear_screen()
            else:
                print("⚠️ Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
                clear_screen()
        except ValueError:
            print("⚠️ Please enter a valid number.")
            input("\nPress Enter to continue...")
            clear_screen()

if __name__ == "__main__":
    clear_screen()
    script_menu()