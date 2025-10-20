# src/main.py

from dotenv import load_dotenv
import os
from agents.planner_agent import plan_content
from agents.summarizer_agent import summarize_content
from agents.rewriter_agent import rewrite_content

# Load environment variables from .env in project root
load_dotenv()

# Retrieve OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found! Make sure you have a .env file in the project root "
        "with the line: OPENAI_API_KEY=sk-your_actual_key"
    )

print("✅ Loaded API Key successfully.")

def main():
    print("🚀 AI Content Repurposer Agent starting...")

    # Step 1: Plan content
    topic = "AI in Marketing"
    print(f"\n🧠 Step 1: Planning content for topic: {topic}")
    plan = plan_content(topic, api_key)

    # Step 2: Summarize content
    print("\n✍️ Step 2: Summarizing content...")
    summary = summarize_content(plan, api_key)

    # Step 3: Rewrite for different platforms
    print("\n🔁 Step 3: Rewriting content for LinkedIn and Twitter...")
    rewritten = rewrite_content(summary, api_key)

    # Save outputs
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/final_output.txt", "w", encoding="utf-8") as f:
        f.write("=== PLAN ===\n" + plan + "\n\n")
        f.write("=== SUMMARY ===\n" + summary + "\n\n")
        f.write("=== REWRITTEN POSTS ===\n" + rewritten)

    print("\n✅ Done! Check outputs/final_output.txt for results.")

if __name__ == "__main__":
    main()
