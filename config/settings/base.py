from pathlib import Path
import environ
from .apps import *
from .authentication import *
from .email import *
from .internationalization import *
from .middleware import *
from .static import *
from .templates import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()

environ.Env.read_env(BASE_DIR / '.env')

# Import database and security settings after `env` is initialized to avoid circular import
from .database import *
from .security import *

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'