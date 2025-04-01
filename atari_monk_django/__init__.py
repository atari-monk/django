from .library.master_script import master_scripts
from .library.remove_comments import remove_comments_from_file
from .library.markdown_to_text import markdown_to_text_using_clipboard
from .library.setup_django import install_django, check_django_installed
from .library.create_django_project import create_django_project
from .library.create_django_app import create_django_app
from .library.generate_model import apply_model
from .library.interactive_model import generate_model_file
from .library.setup_urls_and_views import setup_urls_and_views

__version__ = '0.1.0'