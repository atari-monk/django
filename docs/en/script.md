# Script

1. master_script.py
- script that detects scripts in folder and allows menu to run them
2. setup_django.py
- install framework, print version and installation info
3. md_txt.py
- copy markdown, run this script to get text to google translator
3. create_django_project.py
- generates django project in parent folder (assumption that scripts are in repo_root/script folder)  
    Apply Migrations, This will set up your database tables.
    ```sh
        python manage.py migrate
    ```
    To run server 
    ```sh
        python manage.py runserver
    ```
4. create_django_app.py
- generates django app in project, dont forget to add app in settings file