from atari_monk_django.library.django.generate_project  import generate_project
from atari_monk_django.library.django.generate_app  import generate_app
from atari_monk_django.library.django.interactive_model  import generate_model_file
from atari_monk_django.library.django.generate_model  import apply_model
from atari_monk_django.library.django.setup_urls_and_views import setup_urls_and_views
from atari_monk_django.library.utils.remove_comments import remove_comments_from_file
from atari_monk_django.library.utils.markdown_to_text import markdown_to_text_using_clipboard
from atari_monk_django.library.django.setup_django import install_django, check_django_installed

def script_1():
    generate_project()

def script_2():
    generate_app()

def script_3():
    generate_model_file()

def script_4():
    apply_model()

def script_5():
    setup_urls_and_views()

def script_6():
    remove_comments_from_file()

def script_7():
    markdown_to_text_using_clipboard()

def script_8():
    print("🚀 Setting up Django...\n")
    install_django()
    check_django_installed(verbose=True)

SCRIPTS = [
    {"name": "Generate django Project", "func": script_1},
    {"name": "Generate django App", "func": script_2},
    {"name": "Generate django Model", "func": script_3},
    {"name": "Apply django Model", "func": script_4},
    {"name": "Setup django urls and Views", "func": script_5},
    {"name": "Remove comments form file", "func": script_6},
    {"name": "Markdown to text", "func": script_7},
    {"name": "Setup django", "func": script_8},
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
                print("👋 Exiting...")
                break
            elif 1 <= choice <= len(SCRIPTS):
                print(f"\n🚀 Running {SCRIPTS[choice-1]['name']}...\n")
                SCRIPTS[choice-1]["func"]()
            else:
                print("⚠️ Invalid choice. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")
