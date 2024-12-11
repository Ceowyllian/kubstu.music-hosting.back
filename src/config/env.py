import os

import environ

env = environ.FileAwareEnv()

BASE_DIR = environ.Path(__file__) - 2
env.read_env(os.path.join(BASE_DIR, ".env"))
env.read_env(env.str("ENV_PATH", ".env"))
