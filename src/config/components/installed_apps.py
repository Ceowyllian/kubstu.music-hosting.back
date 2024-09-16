# Application definition

LOCAL_APPS = [
    "db.users.apps.UsersConfig",
    "db.music.apps.MusicConfig",
    "db.person.apps.PersonConfig",
    "db.social.apps.SocialConfig",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "django_filters",
    "drf_spectacular",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]
