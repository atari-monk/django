import os
import subprocess

def generate_app(project_name=None, app_name=None, base_path=r"C:\atari-monk\code\django"):
    if base_path is None:
        base_path = os.path.expanduser("~")
    
    if project_name is None:
        project_name = input("📌 Enter your Django project name: ").strip()
    
    if not project_name:
        print("⚠️ Project name cannot be empty. Try again.")
        return
    
    project_path = os.path.join(base_path, project_name)
    
    if not os.path.exists(os.path.join(project_path, "manage.py")):
        print(f"❌ Django project not found at {project_path} (manage.py not found). Try again.")
        return
    
    if app_name is None:
        app_name = input("📌 Enter your Django app name: ").strip()
    
    if not app_name:
        print("⚠️ App name cannot be empty. Try again.")
        return

    app_path = os.path.join(project_path, app_name)

    if os.path.exists(app_path):
        print(f"⚠️ The app '{app_name}' already exists in {project_path}. Choose a different name.")
        return

    print(f"\n🚀 Creating Django app '{app_name}' in {project_path}...\n")

    try:
        os.chdir(project_path)

        subprocess.check_call(["python", "manage.py", "startapp", app_name])
        print(f"✅ Django app '{app_name}' created successfully!\n")

        print("\n📌 Next Step: Register your app in settings.py")
        print("Add the following line in the INSTALLED_APPS list:\n")
        print(f"    '{app_name}',  # Register your app\n")

    except subprocess.CalledProcessError:
        print("❌ An error occurred while creating the app.")
    except FileNotFoundError:
        print("❌ Python or Django is not installed. Make sure you have Django set up correctly.")