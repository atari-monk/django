import os
import subprocess

def get_model_fields():
    """Ask user for model fields and return a list of field definitions."""
    fields = []
    print("\n📌 Define your model fields (type 'done' when finished).")

    while True:
        field_name = input("🔹 Field name: ").strip()
        if field_name.lower() == "done":
            break

        print("  🔹 Choose field type:")
        print("    1. CharField (Text)")
        print("    2. IntegerField (Number)")
        print("    3. FloatField (Decimal)")
        print("    4. BooleanField (True/False)")
        print("    5. DateTimeField (Date & Time)")
        field_type_choice = input("  🔸 Enter field type number: ").strip()

        field_type_map = {
            "1": "models.CharField",
            "2": "models.IntegerField",
            "3": "models.FloatField",
            "4": "models.BooleanField",
            "5": "models.DateTimeField"
        }

        if field_type_choice in field_type_map:
            field_type = field_type_map[field_type_choice]

            if field_type == "models.CharField":
                max_length = input("  ✏️ Enter max length: ").strip()
                fields.append(f"    {field_name} = {field_type}(max_length={max_length})")
            else:
                fields.append(f"    {field_name} = {field_type}()")
        else:
            print("⚠️ Invalid choice. Try again.")

    return fields

def setup_custom_model():
    """Setup a custom model based on user input."""
    project_path = input("📌 Enter the full path to your Django project: ").strip()
    
    if not os.path.exists(os.path.join(project_path, "manage.py")):
        print("❌ This is not a Django project (manage.py not found). Try again.")
        return
    
    app_name = input("📌 Enter your Django app name: ").strip()
    
    app_path = os.path.join(project_path, app_name)

    if not os.path.exists(app_path):
        print(f"❌ The app '{app_name}' does not exist in {project_path}. Run `python manage.py startapp {app_name}` first.")
        return

    model_name = input("📌 Enter your model name (e.g., Employee): ").strip()
    fields = get_model_fields()

    if not fields:
        print("⚠️ No fields defined. Exiting.")
        return

    models_path = os.path.join(app_path, "models.py")

    # Add model to models.py
    with open(models_path, "a") as f:
        f.write(f"\n\nclass {model_name}(models.Model):\n")
        f.writelines([f"{field}\n" for field in fields])
        f.write(f"\n    def __str__(self):\n        return self.{fields[0].split()[0]}\n")

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
    setup_custom_model()
