from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access them
db_host = os.getenv("DB_HOST")
db_pass = os.getenv("DB_PASS")

print(f"Connecting to {db_host} with password {db_pass}")

# # Load a specific .env file
# from dotenv import load_dotenv
# load_dotenv(dotenv_path="/path/to/.env")

# # Use dotenv_values (returns a dict)
# from dotenv import dotenv_values
# config = dotenv_values(".env")

# print(config["DB_USER"])

# # Override existing system variables
# from dotenv import load_dotenv
# import os

# load_dotenv(override=True)

# print(os.getenv("DB_USER"))