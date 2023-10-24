from api._utils.database import database_get, database_post, database_delete
from dotenv import load_dotenv

load_dotenv(".env")
print(database_get("messages"))