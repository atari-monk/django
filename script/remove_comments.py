import re

def remove_comments(code):
    def remove_inline_comments(line):
        stripped_line = line.lstrip()
        if stripped_line.startswith("#"):
            return ""
        return re.sub(r"(?<!['\"])\s*#.*", "", line)

    def remove_multiline_comments(code):
        pattern = re.compile(r'("""|\'\'\')(?:.|\n)*?\1', re.MULTILINE)
        return re.sub(pattern, '', code)

    code = remove_multiline_comments(code)
    return "\n".join(remove_inline_comments(line) for line in code.splitlines())

if __name__ == "__main__":
    file_path = input("Enter the path to the Python file: ").strip()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()

        cleaned_code = remove_comments(code)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(cleaned_code)

        print(f"Comments removed and saved to: {file_path}")

    except Exception as e:
        print(f"Error: {e}")
