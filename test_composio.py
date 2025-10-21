import os
from composio import ComposioClient, ToolRouter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    print("🔧 Initializing Composio Integration Test...")

    # Load Composio API Key
    composio_key = os.getenv("COMPOSIO_API_KEY")
    if not composio_key:
        print("❌ Missing COMPOSIO_API_KEY in your .env file!")
        return

    # Initialize Composio client
    client = ComposioClient(api_key=composio_key)
    print("✅ Connected to Composio API.")

    # Initialize router for your agents
    router = ToolRouter()

    # Register tools or agents from your AI project
    tools = [
        "planner_agent",
        "summarizer_agent",
        "rewriter_agent"
    ]

    print("⚙ Registering and routing agents through Composio...")
    for tool in tools:
        router.add_tool(tool)
        print(f"➡ Registered {tool}")

    # Simulate a workflow test
    print("🚀 Running test workflow via Composio...")
    workflow_input = {
        "topic": "AI in Marketing",
        "platforms": ["LinkedIn", "Twitter"]
    }

    # Here we simulate calling a tool route
    response = client.run_workflow(
        name="content_repurpose_test",
        input_data=workflow_input
    )

    print("✅ Workflow executed successfully via Composio.")
    
    # Save result
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/composio_result.txt", "w") as f:
        f.write("🎯 Composio Integration Successful!\n")
        f.write(f"Response: {response}\n")

    print("📝 Output saved to outputs/composio_result.txt")

if _name_ == "_main_":
    main()