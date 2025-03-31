import os
import subprocess

def generate_model():
    """Automatically generate a model and run migrations."""
    project_path = input("📌 Enter the full path to your Django project: ").strip()
    
    if not os.path.exists(os.path.join(project_path, "manage.py")):
        print("❌ This is not a Django project (manage.py not found). Try again.")
        return
    
    app_name = input("📌 Enter your Django app name: ").strip()
    
    app_path = os.path.join(project_path, app_name)

    if not os.path.exists(app_path):
        print(f"❌ The app '{app_name}' does not exist in {project_path}. Run `python manage.py startapp {app_name}` first.")
        return

    model_name = "Employee"  # Fixed model name
    fields = [
        "name = models.CharField(max_length=100)",
        "age = models.IntegerField()",
        "department = models.CharField(max_length=50)"
    ]
    
    models_path = os.path.join(app_path, "models.py")

    # Write the model to models.py
    with open(models_path, "a") as f:
        f.write(f"\n\nclass {model_name}(models.Model):\n")
        f.writelines([f"    {field}\n" for field in fields])
        f.write(f"\n    def __str__(self):\n        return self.name\n")

    print(f"\n✅ Model '{model_name}' added to {app_name}/models.py")

    # Run migrations
    try:
        os.chdir(project_path)
        print("\n🚀 Running migrations...\n")
        subprocess.check_call(["python", "manage.py", "makemigrations", app_name])
        subprocess.check_call(["python", "manage.py", "migrate"])
        print("✅ Migrations applied successfully!")
    except subprocess.CalledProcessError:
        print("❌ An error occurred during migrations.")

if __name__ == "__main__":
    generate_model()
