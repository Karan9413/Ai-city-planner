import os
from dotenv import load_dotenv

# Load the .env file from the current directory
load_dotenv()

# Fetch the key
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("SUCCESS: API_KEY found.")
    # Print the first few characters to verify it's the right key (for security, don't print the whole thing)
    print(f"Key preview: {api_key[:5]}********")
else:
    print("ERROR: API_KEY not found. Check your .env file path and contents.")