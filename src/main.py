from dotenv import load_dotenv
import os
from agents.planner_agent import plan_content
from agents.summarizer_agent import summarize_content
from agents.rewriter_agent import rewrite_content

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ Error: OPENAI_API_KEY not found in environment variables.")
    exit(1)
else:
    print("✅ Loaded API Key successfully.")

def main():
    print("\n🚀 AI Content Repurposer Agent starting...")

    # Step 0: Ask user for input
    topic = input("\n🧠 Enter the topic or content you want to repurpose: ").strip()
    if not topic:
        print("❌ No topic entered. Exiting...")
        return

    # Optional: Ask user for platforms
    platforms_input = input("\n💬 Enter platforms to rewrite for (comma separated, e.g., LinkedIn, Twitter, Blog): ").strip()
    platforms = [p.strip() for p in platforms_input.split(",") if p.strip()]
    if not platforms:
        platforms = ["LinkedIn", "Twitter"]  # default platforms

    # Step 1: Plan
    print(f"\n🧠 Step 1: Planning content for topic: {topic}")
    plan = plan_content(topic, api_key)

    # Step 2: Summarize
    print("\n✍️ Step 2: Summarizing content...")
    summary = summarize_content(plan, api_key)

    # Step 3: Rewrite for selected platforms
    print(f"\n🔁 Step 3: Rewriting content for {', '.join(platforms)}...")
    rewritten = rewrite_content(summary, api_key, platforms=platforms)

    # Save output
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/final_output.txt", "w", encoding="utf-8") as f:
        f.write("=== USER INPUT TOPIC ===\n" + topic + "\n\n")
        f.write("=== PLAN ===\n" + plan + "\n\n")
        f.write("=== SUMMARY ===\n" + summary + "\n\n")
        f.write("=== REWRITTEN POSTS ===\n" + rewritten)

    print("\n✅ Done! Check outputs/final_output.txt for results.")

if __name__ == "__main__":
    main()
