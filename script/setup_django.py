import subprocess
import sys

def install_django():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "django"])
        print("\n✅ Django installed successfully!")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to install Django. Please check your Python and pip installation.")

def verify_django():
    try:
        version = subprocess.check_output(["django-admin", "--version"], text=True).strip()
        print(f"\n✅ Django is installed. Version: {version}")
    except subprocess.CalledProcessError:
        print("\n❌ Django installation could not be verified. Try running 'django-admin --version' manually.")

if __name__ == "__main__":
    print("🚀 Setting up Django...\n")
    install_django()
    verify_django()
