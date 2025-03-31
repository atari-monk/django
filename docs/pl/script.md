# Skrypt  

1. **master_script.py**  
   - Skrypt wykrywający inne skrypty w folderze i umożliwiający ich uruchamianie z menu.  

2. **setup_django.py**  
   - Instaluje framework Django, wyświetla jego wersję oraz informacje o instalacji.  

3. **md_txt.py**  
   - Kopiuje zawartość pliku Markdown i konwertuje ją na zwykły tekst, aby ułatwić tłumaczenie w Google Translatorze.  

4. **create_django_project.py**  
   - Tworzy nowy projekt Django w folderze nadrzędnym (założenie: skrypty znajdują się w `repo_root/script`).  
   - Wykonuje migracje, aby utworzyć tabele w bazie danych:  
     ```sh
     python manage.py migrate
     ```  
   - Uruchamia serwer deweloperski:  
     ```sh
     python manage.py runserver
     ```  

5. **create_django_app.py**  
   - Tworzy nową aplikację Django w istniejącym projekcie.  
   - Nie zapomnij dodać aplikacji do pliku `settings.py`.