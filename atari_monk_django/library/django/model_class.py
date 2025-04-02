import json
from typing import Dict, Any

def generate_model_code(metadata: Dict[str, Any]) -> str:

    lines = []

    lines.append("from django.db import models")
    lines.append("\n")

    class_def = f"class {metadata['model_name']}(models.Model):"
    lines.append(class_def)

    for field in metadata['fields']:
        field_parts = [f"models.{field['type']}"]

        if field['params']:
            params = ", ".join(f"{k}={repr(v)}" for k, v in field['params'].items())
            field_parts.append(params)

        field_line = f"    {field['name']} = {'('.join(field_parts)})"
        lines.append(field_line)

    if metadata['fields']:
        first_field = metadata['fields'][0]['name']
        lines.append("\n    def __str__(self):")
        lines.append(f"        return str(self.{first_field})")

    return "\n".join(lines)

def save_model_code(model_code: str, metadata: Dict[str, Any]) -> str:

    filename = f"{metadata['model_name'].lower()}_model.py"
    with open(filename, 'w') as f:
        f.write(model_code)
    return filename

def main():
    metadata_file = input("📌 Enter path to metadata JSON file: ").strip()
    with open(metadata_file) as f:
        metadata = json.load(f)

    model_code = generate_model_code(metadata)
    print("\nGenerated Model Code:\n")
    print(model_code)

    filename = save_model_code(model_code, metadata)
    print(f"\n✅ Model code saved to {filename}")

if __name__ == "__main__":
    main()