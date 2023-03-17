from dotenv import load_dotenv
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)