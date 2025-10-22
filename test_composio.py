# test_composio.py
import os
from dotenv import load_dotenv
from composio import client  # lowercase, latest SDK

# ==========================
# 1️⃣ Load environment variables
# ==========================
load_dotenv()
COMPOSIO_TOKEN = os.getenv("COMPOSIO_TOKEN")

if not COMPOSIO_TOKEN:
    raise ValueError("COMPOSIO_TOKEN not set in your .env file!")

# ==========================
# 2️⃣ Initialize Composio client
# ==========================
cli = client(COMPOSIO_TOKEN)  # positional argument

# ==========================
# 3️⃣ Test a simple API call
# ==========================
def main():
    print("🔧 Initializing Composio Integration Test...")

    # Example: fetch available tools (adjust based on SDK version)
    try:
        tools = cli.list_tools()  # method name may vary: list_tools() or get_tools()
    except Exception as e:
        print("❌ Error fetching tools:", e)
        return

    print("✅ Tools fetched successfully:")
    for t in tools:
        # Depending on SDK, t could be a dict or object
        name = t.get('name') if isinstance(t, dict) else get
