# supaConnection.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()  # Load environment variables from .env file

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

#create DB client
supabase = create_client(url, key)
#simple response query to test connection to supabase!
response = (
    supabase.table("test_data")
    .select("*")
    .execute()
)

names = [item['name'] for item in response.data]
print(names)