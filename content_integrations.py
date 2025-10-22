# ==========================================================
# 🤖 AI Content Repurposer - Member 1 Agent + Member 2 Integrations (Fixed Version)
# ==========================================================

import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from slack_sdk import WebClient
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError
from tweepy import OAuth1UserHandler, API

# ==========================================================
# 1️⃣ Load Environment Variables
# ==========================================================
load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Twitter
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# WordPress
WORDPRESS_URL = os.getenv("WORDPRESS_URL")
WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")
WORDPRESS_PASSWORD = os.getenv("WORDPRESS_PASSWORD")

# Slack
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

# ==========================================================
# 2️⃣ Integration Functions (Member 2) - Fixed
# ==========================================================
def fetch_trending_topics(keyword="AI", timeframe="now 1-d", geo="IN", top_n=5, max_retries=5):
    """Fetch top trending related queries from Google Trends with retry/backoff."""
    pytrends = TrendReq()
    for attempt in range(1, max_retries + 1):
        try:
            pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)
            trending = pytrends.related_queries()[keyword]['top']
            if trending is not None:
                time.sleep(1)  # short delay to reduce throttling
                return trending['query'].head(top_n).tolist()
            return [keyword]
        except TooManyRequestsError:
            wait_time = 5 * attempt
            print(f"⚠️ Too many requests for '{keyword}', retrying in {wait_time}s (Attempt {attempt}/{max_retries})")
            time.sleep(wait_time)
        except Exception as e:
            print(f"⚠️ Could not fetch trends for '{keyword}': {e}")
            return [keyword]
    print(f"⚠️ Failed to fetch trends for '{keyword}' after {max_retries} attempts. Using fallback keyword.")
    return [keyword]


def post_to_twitter(content):
    """Post short content to Twitter."""
    try:
        auth = OAuth1UserHandler(
            TWITTER_API_KEY, TWITTER_API_SECRET,
            TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
        )
        api = API(auth)
        if len(content) > 280:
            content = content[:277] + "..."
        api.update_status(content)
        print("✅ Twitter post successful")
    except Exception as e:
        print("❌ Twitter post failed:", e)


def post_to_wordpress(title, content):
    """Publish blog content to WordPress."""
    try:
        wp_client = Client(WORDPRESS_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD)
        post = WordPressPost()
        post.title = title
        post.content = content
        post.post_status = 'publish'
        wp_client.call(NewPost(post))
        print("✅ WordPress post successful")
    except Exception as e:
        print("❌ WordPress post failed:", e)


def send_slack_notification(message):
    """Send notification message to Slack."""
    if not SLACK_TOKEN or not SLACK_CHANNEL:
        print("⚠️ Slack configuration missing. Skipping notification.")
        return
    try:
        slack_client = WebClient(token=SLACK_TOKEN)
        slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        print("✅ Slack notification sent")
    except Exception as e:
        print("❌ Slack notification failed:", e)


# ==========================================================
# 3️⃣ AI Content Generation - Split Output
# ==========================================================
def generate_content_split(topic):
    """
    Generate AI-based content for a given topic.
    Returns dict: {title, summary, blog, tweet}
    """
    prompt = f"""
    Generate content for topic: '{topic}'.
    Return output in the following format:
    Title: <Catchy title>
    Summary: <2-line summary>
    Blog: <3-paragraph detailed blog>
    Tweet: <Under 280 characters>
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600
        )
        text = response.choices[0].message.content
    except Exception as e:
        print("❌ OpenAI API call failed:", e)
        return {"title": topic, "summary": "", "blog": "", "tweet": ""}

    # Parse AI output
    output = {"title": "", "summary": "", "blog": "", "tweet": ""}
    current_key = None

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("Title:"):
            current_key = "title"
            output[current_key] = line.replace("Title:", "").strip()
        elif line.startswith("Summary:"):
            current_key = "summary"
            output[current_key] = line.replace("Summary:", "").strip()
        elif line.startswith("Blog:"):
            current_key = "blog"
            output[current_key] = line.replace("Blog:", "").strip()
        elif line.startswith("Tweet:"):
            current_key = "tweet"
            output[current_key] = line.replace("Tweet:", "").strip()
        elif current_key:
            output[current_key] += " " + line
    return output


# ==========================================================
# 4️⃣ Full Workflow - Fixed
# ==========================================================
def run_agent_workflow():
    print("🔍 Fetching trending topics...")
    base_keywords = ["AI", "machine learning", "automation"]
    topics = []

    for kw in base_keywords:
        topics.extend(fetch_trending_topics(kw))
        time.sleep(2)  # small pause between different keywords to reduce throttling

    topics = list(set(topics))[:5]
    print(f"📈 Trending topics: {topics}")

    for topic in topics:
        print(f"\n🧠 Generating content for: {topic}")
        content = generate_content_split(topic)

        print("📢 Posting to Twitter...")
        post_to_twitter(content["tweet"])

        print("📰 Posting to WordPress...")
        post_to_wordpress(content["title"], content["blog"])

        print("💬 Sending Slack notification...")
        send_slack_notification(f"New post published: {content['title']}")
        time.sleep(1)  # small delay between posts to avoid API rate limits


# ==========================================================
# 5️⃣ Entry Point
# ==========================================================
if __name__ == "__main__":
    run_agent_workflow()
