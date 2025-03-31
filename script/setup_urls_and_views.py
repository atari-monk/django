import os

def setup_urls_and_views():
    project_path = input("📌 Enter the full path to your Django project: ").strip()
    
    if not os.path.exists(os.path.join(project_path, "manage.py")):
        print("❌ This does not seem to be a Django project (manage.py not found). Try again.")
        return
    
    app_name = input("📌 Enter your Django app name: ").strip()
    
    app_path = os.path.join(project_path, app_name)

    if not os.path.exists(app_path):
        print(f"❌ The app '{app_name}' does not exist in {project_path}. Run `python manage.py startapp {app_name}` first.")
        return

    urls_path = os.path.join(app_path, "urls.py")
    views_path = os.path.join(app_path, "views.py")
    project_urls_path = os.path.join(project_path, project_path.split(os.sep)[-1], "urls.py")

    if not os.path.exists(urls_path):
        print(f"📝 Creating {app_name}/urls.py...")
        with open(urls_path, "w") as f:
            f.write("""from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
""")
    else:
        print(f"✅ {app_name}/urls.py already exists.")

    with open(views_path, "r+") as f:
        content = f.read()
        if "def home(request):" not in content:
            print(f"📝 Adding 'home' view to {app_name}/views.py...")
            f.write("\nfrom django.http import HttpResponse\n\ndef home(request):\n    return HttpResponse(\"Hello, Django!\")\n")
        else:
            print(f"✅ 'home' view already exists in {app_name}/views.py.")

    with open(project_urls_path, "r+") as f:
        content = f.read()
        if f"include('{app_name}.urls')" not in content:
            print(f"📝 Adding {app_name}'s URLs to project urls.py...")
            content = content.replace("urlpatterns = [", f"urlpatterns = [\n    path('', include('{app_name}.urls')),\n")
            f.seek(0)
            f.write("from django.urls import include\n" + content)
        else:
            print(f"✅ {app_name} is already included in project urls.py.")

    print("\n🚀 Setup complete! Restart your server and visit http://127.0.0.1:8000/ to see 'Hello, Django!'\n")

if __name__ == "__main__":
    setup_urls_and_views()
