from library import install_django, check_django_installed

if __name__ == "__main__":
    print("🚀 Setting up Django...\n")
    install_django()
    check_django_installed(verbose=True)
