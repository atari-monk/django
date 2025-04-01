import argparse
from .generate_project import generate_project
from .generate_app import generate_app

def master_script():
    parser = argparse.ArgumentParser(description='Generate Django project and apps')
    
    parser.add_argument('--project-name', type=str, help='Name of the Django project')
    parser.add_argument('--skip-migrations', action='store_true', 
                       help='Skip creating migrations for the project')
    parser.add_argument('--skip-runserver', action='store_true', 
                       help='Skip running the development server')
    
    parser.add_argument('--app-names', type=str, nargs='+',
                       help='Names of the Django apps to create (space-separated)')
    
    args = parser.parse_args()
    
    project_path = None
    
    if args.project_name:
        project_path = generate_project(
            project_name=args.project_name,
            skip_migrations=args.skip_migrations,
            skip_runserver=args.skip_runserver
        )
    
    if args.app_names:
        if not project_path and not args.project_name:
            print("\nError: Cannot generate apps without a project. Please provide --project-name")
            return
        
        if not project_path and args.project_name:
            project_path = f"./{args.project_name}"
        
        print(f"\nGenerating {len(args.app_names)} apps:")
        for app_name in args.app_names:
            generate_app(
                project_path=project_path,
                app_name=app_name
            )
