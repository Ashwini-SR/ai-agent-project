# agents/rewriter_agent.py
from openai import OpenAI

def rewrite_content(summary, api_key, platforms=None):
    client = OpenAI(api_key=api_key)
    platforms = platforms or ["LinkedIn", "Twitter"]  # default

    rewritten_posts = ""
    for platform in platforms:
        # Example: prompt tailored for platform
        prompt = f"Rewrite the following content for {platform}:\n{summary}"
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        rewritten_posts += f"--- {platform} ---\n{response.choices[0].message.content}\n\n"
    
    return rewritten_posts
