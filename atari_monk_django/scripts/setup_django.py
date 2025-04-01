from atari_monk_django.library.setup_django import install_django, check_django_installed

def main():
    print("🚀 Setting up Django...\n")
    install_django()
    check_django_installed(verbose=True)
