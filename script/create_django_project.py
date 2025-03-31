import os
import subprocess

def create_django_project():
    project_name = input("📌 Enter your Django project name: ").strip()
    
    if not project_name:
        print("⚠️ Project name cannot be empty. Try again.")
        return

    # Move one folder up
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    os.chdir(parent_dir)  # Change working directory to parent
    
    if os.path.exists(project_name):
        print(f"⚠️ A folder named '{project_name}' already exists in {parent_dir}. Choose a different name.")
        return
    
    print(f"\n🚀 Creating Django project '{project_name}' in {parent_dir}...\n")

    try:
        # Create the project in the parent directory
        subprocess.check_call(["django-admin", "startproject", project_name])
        print(f"✅ Django project '{project_name}' created successfully!\n")

        # Navigate into the new project directory
        project_path = os.path.join(parent_dir, project_name)
        os.chdir(project_path)

        print("\n🚀 Starting the Django development server...\n")
        subprocess.check_call(["python", "manage.py", "runserver"])
        
        print("\n🌍 Visit http://127.0.0.1:8000/ to see your project running.")
    
    except subprocess.CalledProcessError:
        print("❌ An error occurred while setting up the project.")
    except FileNotFoundError:
        print("❌ Django is not installed. Run `pip install django` and try again.")

if __name__ == "__main__":
    create_django_project()
