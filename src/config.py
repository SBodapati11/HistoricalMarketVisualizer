import os
from dotenv import load_dotenv


load_dotenv()

DB_URI = 'postgresql+psycopg2://postgres:{0}@localhost:5432/historical-market-visualizer'.format(os.getenv('POSTGRES_PASSWORD'))