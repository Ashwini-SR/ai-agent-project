# test_composio.py

import os
from dotenv import load_dotenv
from composio import Composio  # Correct import for the client

# ==========================
# 1️⃣ Load environment variables
# ==========================
load_dotenv()  # Loads variables from .env file

COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY")

# Debug print to check if API key is loaded
print("🔑 COMPOSIO_API_KEY:", COMPOSIO_API_KEY)

if not COMPOSIO_API_KEY:
    raise ValueError("❌ COMPOSIO_API_KEY not set in your .env file!")

# ==========================
# 2️⃣ Initialize Composio client
# ==========================
cli = Composio(api_key=COMPOSIO_API_KEY)

# ==========================
# 3️⃣ Test the API connection
# ==========================
def main():
    print("🔧 Initializing Composio Integration Test...")

    if not cli:
        print("❌ Composio client not initialized!")
        return

    try:
        tools = cli.list_tools()
        print("✅ Tools fetched successfully:")
        print(tools)  # Print raw output for debugging
        for t in tools:
            print(f"- {t.get('name') if isinstance(t, dict) else t}")
    except Exception as e:
        print("❌ Error fetching tools:", e)

# ✅ Proper Python entry point
if __name__ == "_main_":
    main()