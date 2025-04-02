from .library.utils.markdown_to_text import markdown_to_text_using_clipboard
from .library.utils.remove_comments import remove_comments_from_file
from .library.utils.script_menu import script_menu

from .library.django.generate_app import generate_app
from .library.django.generate_model import apply_model
from .library.django.generate_project import generate_project
from .library.django.master_script import master_script
from .library.django.meta_model import save_meta_model
from .library.django.setup_django import install_django, check_django_installed
from .library.django.setup_urls_and_views import setup_urls_and_views

__version__ = '0.1.0'