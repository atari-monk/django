def get_model_fields():
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

def generate_model_file():
    file_path = input("📌 Enter the file path to save the model (e.g., models.py): ").strip()

    model_name = input("📌 Enter your model name (e.g., Employee): ").strip()
    fields = get_model_fields()

    if not fields:
        print("⚠️ No fields defined. Exiting.")
        return

    with open(file_path, "a") as f:
        f.write(f"\n\nclass {model_name}(models.Model):\n")
        f.writelines([f"{field}\n" for field in fields])
        f.write(f"\n    def __str__(self):\n        return self.{fields[0].split()[0]}\n")

    print(f"\n✅ Model '{model_name}' has been written to {file_path}")
