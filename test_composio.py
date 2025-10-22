import os
from composio.client import Client
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🔧 Initializing Composio Integration Test...")

    composio_key = os.getenv("COMPOSIO_API_KEY")
    if not composio_key:
        print("❌ Missing COMPOSIO_API_KEY in your .env file!")
        return

    client = Client(api_key=composio_key)
    print("✅ Connected to Composio API.")

    # Simulate a workflow test
    workflow_input = {"topic": "AI in Marketing", "platforms": ["LinkedIn", "Twitter"]}

    try:
        response = client.run_workflow(
            workflow_name="content_repurpose_test",
            input_data=workflow_input
        )
        print("✅ Workflow executed successfully.")
    except Exception as e:
        response = None
        print(f"❌ Workflow execution failed: {e}")

    # Save result
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/composio_result.txt", "w", encoding="utf-8") as f:
        f.write("🎯 Composio Integration Test Result\n")
        f.write(f"Response: {response}\n")

    print("📝 Output saved to outputs/composio_result.txt")

if __name__ == "__main__":
    main()
