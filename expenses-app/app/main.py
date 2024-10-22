from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"\
               f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
