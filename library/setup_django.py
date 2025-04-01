import subprocess
import sys

def install_django():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "django"])
        print("\n✅ Django installed successfully!")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to install Django. Please check your Python and pip installation.")

def check_django_installed(verbose=False):
    
    try:
        version = subprocess.check_output(["django-admin", "--version"], 
            text=True, 
            stderr=subprocess.PIPE).strip()
        if verbose:
            print(f"\n✅ Django is installed. Version: {version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        if verbose:
            print("\n❌ Django is not installed or could not be verified.")
        return False