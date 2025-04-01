import os
import subprocess

def apply_model():
    project_path = input("📌 Enter the full path to your Django project: ").strip()
    
    if not os.path.exists(os.path.join(project_path, "manage.py")):
        print("❌ This is not a Django project (manage.py not found). Try again.")
        return
    
    app_name = input("📌 Enter your Django app name: ").strip()
    app_path = os.path.join(project_path, app_name)

    if not os.path.exists(app_path):
        print(f"❌ The app '{app_name}' does not exist in {project_path}. Run `python manage.py startapp {app_name}` first.")
        return

    model_file_path = input("📌 Enter the path to the model file: ").strip()

    if not os.path.exists(model_file_path):
        print("❌ Model file not found. Check the path and try again.")
        return

    models_path = os.path.join(app_path, "models.py")

    with open(model_file_path, "r") as model_file:
        model_content = model_file.read()

    with open(models_path, "a") as f:
        f.write(f"\n\n{model_content}\n")

    print(f"\n✅ Model from '{model_file_path}' added to {app_name}/models.py")

    try:
        os.chdir(project_path)
        print("\n🚀 Running migrations...\n")
        subprocess.check_call(["python", "manage.py", "makemigrations", app_name])
        subprocess.check_call(["python", "manage.py", "migrate"])
        print("✅ Migrations applied successfully!")
    except subprocess.CalledProcessError:
        print("❌ An error occurred during migrations.")

if __name__ == "__main__":
    apply_model()
