# test.py

import os
from dotenv import load_dotenv
load_dotenv()

api = os.environ.get('API')
print(api)
