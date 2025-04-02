To organize your Python project where you have a `script` folder for your main scripts and a `library` folder for your functions, and you want to use those functions in your scripts, you'll need to set up an `__init__.py` file to mark the `library` folder as a Python package and enable you to import from it.

Here’s a step-by-step guide:

### Project Structure:

```
project_root/
├── script/
│   └── your_script.py
└── library/
    ├── __init__.py
    └── some_function.py
```

1. **Creating `__init__.py` in the `library` folder:**
   - The `__init__.py` file tells Python that the folder should be treated as a package. You don’t necessarily need to put anything inside it if you just want to mark the folder as a package.
   
   You can leave it empty or initialize any required imports there.

   **Example of `__init__.py`:**
   ```python
   # library/__init__.py

   # This can be empty or you can import specific functions here
   from .some_function import some_function
   ```

   This allows you to import `some_function` directly from `library` in your script.

2. **Importing from `library` in your script:**

   In the `script` folder, you can now import the functions from `library` by doing the following:

   ```python
   # script/your_script.py
   from library import some_function

   # Use the imported function
   some_function()
   ```

3. **Running the script:**
   - When you run `your_script.py`, Python will look for the `library` package in the same directory as the script or in directories listed in the `PYTHONPATH`. If you're running the script from the project root, everything should work as expected.

4. **Optional: Setting up relative imports (if the script is in a submodule)**:
   If you want to use relative imports (for example, when your project becomes more complex), you can structure your project like this:

   ```
   project_root/
   ├── script/
   │   └── main.py
   └── library/
       ├── __init__.py
       └── some_function.py
   ```

   Then you can modify your `main.py` in the `script` folder to use relative imports:

   ```python
   # script/main.py
   from library.some_function import some_function
   some_function()
   ```

5. **Testing with module paths:**
   If you're running the script directly from `script/`, you might encounter issues if Python can't find the `library` module. In that case, you can adjust the `PYTHONPATH` or run the script from the root of the project:

   ```bash
   python -m script.your_script
   ```

This setup will allow you to easily import functions from the `library` folder into any script in the `script` folder.

Let me know if you have any further questions!