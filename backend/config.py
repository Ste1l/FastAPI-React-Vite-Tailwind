from dotenv import load_dotenv
import os
load_dotenv()
DB_HOST=os.environ.get("POSTGRES_HOST")
DB_PORT=os.environ.get("POSTGRES_PORT")
DB_NAME=os.environ.get("POSTGRES_DB")
DB_USER=os.environ.get("POSTGRES_USER")
DB_PASS=os.environ.get("POSTGRES_PASSWORD")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

SECRET = os.getenv("SECRET", "YOUR_SECRET_KEY")