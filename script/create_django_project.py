import os
import subprocess

def create_django_project():
    project_name = input("📌 Enter your Django project name: ").strip()
    
    if not project_name:
        print("⚠️ Project name cannot be empty. Try again.")
        return


    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    os.chdir(parent_dir)

    if os.path.exists(project_name):
        print(f"⚠️ A folder named '{project_name}' already exists in {parent_dir}. Choose a different name.")
        return
    
    print(f"\n🚀 Creating Django project '{project_name}' in {parent_dir}...\n")

    try:
        subprocess.check_call(["django-admin", "startproject", project_name])
        print(f"✅ Django project '{project_name}' created successfully!\n")

        project_path = os.path.join(parent_dir, project_name)
        os.chdir(project_path)

        print("\n🔄 Applying migrations...\n")
        subprocess.check_call(["python", "manage.py", "migrate"])
        print("✅ Migrations applied successfully!")

        print("\n🚀 Opening a new terminal for the Django server...\n")

        if os.name == "nt":
            subprocess.Popen(["start", "cmd", "/k", "python manage.py runserver"], shell=True)
        else:
            subprocess.Popen(["x-terminal-emulator", "-e", "python manage.py runserver"])

        print("\n🌍 Server started in a new terminal. Close that window or press CTRL + BREAK to stop the server.")

    except subprocess.CalledProcessError:
        print("❌ An error occurred while setting up the project.")
    except FileNotFoundError:
        print("❌ Django is not installed. Run `pip install django` and try again.")

if __name__ == "__main__":
    create_django_project()