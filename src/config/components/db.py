from config.env import env

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {"default": env.db(var="DB_URL")}
