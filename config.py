import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    broker_url = os.environ.get('BROKER_URL')
    result_backend = os.environ.get('RESULT_BACKEND')
    MONGODB_URI = os.environ.get('MONGODB_URI')
