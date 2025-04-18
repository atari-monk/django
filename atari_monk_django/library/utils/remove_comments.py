import re

def remove_comments(code):
    def remove_inline_comments(line):
        stripped_line = line.lstrip()
        if stripped_line.startswith("#"):
            return None

        in_string = False
        string_char = None
        result = []

        i = 0
        n = len(line)
        while i < n:
            char = line[i]

            if char in ('"', "'"):
                if not in_string:
                    in_string = True
                    string_char = char
                elif string_char == char:
                    if i > 0 and line[i-1] != '\\':
                        in_string = False
                        string_char = None

            if not in_string and char == '#':
                break

            result.append(char)
            i += 1

        return ''.join(result).rstrip()

    def remove_multiline_comments(code):
        pattern = re.compile(r'("""|\'\'\')(?:.|\n)*?\1', re.MULTILINE)
        return re.sub(pattern, '', code)

    code = remove_multiline_comments(code)
    lines = []
    for line in code.splitlines():
        processed_line = remove_inline_comments(line)
        if processed_line is not None:
            lines.append(processed_line)
    return '\n'.join(lines)

def remove_comments_from_file():
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