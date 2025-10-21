from dotenv import load_dotenv
import os
from agents.planner_agent import plan_content
from agents.tool_router_agent import ToolRouterAgent  # Composio agent

# Load API keys from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
composio_api_key = os.getenv("COMPOSIO_API_KEY")

if not openai_api_key:
    print("❌ Error: OPENAI_API_KEY not found in environment variables.")
    exit(1)
if not composio_api_key:
    print("❌ Error: COMPOSIO_API_KEY not found in environment variables.")
    exit(1)

print("✅ Loaded API Keys successfully.")

def main():
    print("\n🚀 AI Content Repurposer Agent starting...")

    # Step 0: Ask user for input
    topic = input("\n🧠 Enter the topic or content you want to repurpose: ").strip()
    if not topic:
        print("❌ No topic entered. Exiting...")
        return

    platforms_input = input(
        "\n💬 Enter platforms to rewrite for (comma separated, e.g., LinkedIn, Twitter, Blog): "
    ).strip()
    platforms = [p.strip() for p in platforms_input.split(",") if p.strip()]
    if not platforms:
        platforms = ["LinkedIn", "Twitter"]  # default platforms

    # Step 1: Plan content (still using OpenAI)
    print(f"\n🧠 Step 1: Planning content for topic: {topic}")
    plan = plan_content(topic, openai_api_key)
    print("\n=== PLAN ===")
    print(plan)

    # Step 2: Initialize Composio Tool Router
    print("\n🔌 Initializing Composio Tool Router...")
    router_agent = ToolRouterAgent()  # automatically uses COMPOSIO_API_KEY from .env
    print("✅ Connected to Composio tools successfully.\n")

    # Step 3: Summarize content using Composio
    print("✍️ Step 2: Summarizing content with Composio...")
    summary = router_agent.summarize(plan)
    print("\n=== SUMMARY ===")
    print(summary)

    # Step 4: Rewrite content for platforms using Composio
    print(f"\n🔁 Step 3: Rewriting content for {', '.join(platforms)}...")
    rewritten_posts = router_agent.rewrite_for_platforms(summary, platforms)
    for platform, text in rewritten_posts.items():
        print(f"\n--- {platform.strip()} ---")
        print(text)

    # Step 5: Save output to file
    os.makedirs("outputs", exist_ok=True)
    output_file = "outputs/final_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=== USER INPUT TOPIC ===\n" + topic + "\n\n")
        f.write("=== PLAN ===\n" + plan + "\n\n")
        f.write("=== SUMMARY ===\n" + summary + "\n\n")
        f.write("=== REWRITTEN POSTS ===\n")
        for platform, text in rewritten_posts.items():
            f.write(f"{platform.strip()}:\n{text}\n\n")

    print(f"\n✅ Done! Check {output_file} for results.")

if __name__ == "__main__":
    main()
