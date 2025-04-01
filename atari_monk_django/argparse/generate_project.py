import argparse
from atari_monk_django.library.django.generate_project  import generate_project

def generate_project_args():
    parser = argparse.ArgumentParser(
        description="Create a new Django project with optional configurations",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "project_name", 
        nargs="?", 
        default=None,
        help="Name of the Django project to create"
    )
    
    parser.add_argument(
        "--skip-migrations", 
        action="store_true",
        help="Skip applying initial migrations"
    )
    
    parser.add_argument(
        "--skip-runserver", 
        action="store_true",
        help="Skip starting the development server"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0",
        help="Show version and exit"
    )
    
    args = parser.parse_args()
    
    generate_project(
        project_name=args.project_name,
        skip_migrations=args.skip_migrations,
        skip_runserver=args.skip_runserver
    )

if __name__ == "__main__":
    generate_project_args()
