 AI Content Repurposer
A full-featured AI Content Repurposer integrating Open AI, Composio, Google Trends, Twitter, WordPress, and Slack for automated content creation, summarization, rewriting, and publishing.
Table of Contents
1. Features
2. Technologies
3. Setup & Installation
4. Environment Variables
5. Project Structure
6. Usage
7. Workflow
8. Testing Composio Integration
9. Troubleshooting
10. Author & License
1 Features
•	Generate AI content for trending topics using OpenAI GPT-4o-mini.
•	Summarize and rewrite content using Composio tools.
•	Fetch trending keywords from Google Trends (pytrends).
•	Publish blog posts to WordPress automatically.
•	Post short content to Twitter.
•	Send Slack notifications for newly published content.
•	Multi-platform content repurposing with automated workflow.
2 Technologies
•	Python 3.13+
•	OpenAI SDK (openai)
•	Composio SDK (composio)
•	Slack SDK (slack_sdk)
•	WordPress XML-RPC (python-wordpress-xmlrpc)
•	Google Trends (pytrends)
•	Twitter API (tweepy)
•	Environment variable management (python-dotenv)
3 Setup & Installation
Clone the repository:
    git clone <your-repo-url>
    cd ai-agent-project
Create and activate a virtual environment:
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

    
Install dependencies:
    pip install -r requirements.txt
Example requirements.txt:
openai
langchain
python-dotenv
composio
slack_sdk
python-wordpress-xmlrpc
pytrends
tweepy
4 Environment Variables
Create a .env file in the project root with the following keys:
OPENAI_API_KEY=your_openai_api_key
COMPOSIO_API_KEY=your_composio_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret
WORDPRESS_URL=https://yourblog.com/xmlrpc.php
WORDPRESS_USERNAME=your_username
WORDPRESS_PASSWORD=your_password
SLACK_TOKEN=your_slack_token
SLACK_CHANNEL=#your-channel
5 Project Structure
•	ai-agent-project/
•	├─ src/
•	│  ├─ main.py                # Main AI Content Repurposer workflow
•	│  ├─ agents/
•	│  │  ├─ planner_agent.py    # OpenAI content planning agent
•	│  │  ├─ rewriter_agent.py   # OpenAI/Composio rewriting agent
•	│  │  └─ tool_router_agent.py # Composio integration agent
•	├─ test_composio.py           # Script to test Composio integration
•	├─ outputs/                   # Generated content saved here
•	├─ .env                       # Environment variables
•	├─ requirements.txt           # Python dependencies
•	└─ README.md                  # Project documentation
6 Usage
Run the AI Content Repurposer:
    python src/main.py
•	- Enter the topic you want to repurpose.
•	- Enter platforms (LinkedIn, Twitter, Blog) or leave default.
•	- Generates plan, summary, rewrites, and saves output in outputs/final_output.txt
Run Full Workflow with Integrations:
    python src/ai_member2_workflow.py
•	- Fetch trending topics via Google Trends.
•	- Generate content for each topic.
•	- Publish to Twitter, WordPress, and Slack automatically.
7 Workflow
•	Content Planning – OpenAI generates a 3-step content plan.
•	Content Summarization – Composio condenses text.
•	Content Rewriting – Composio adapts text for selected platforms.
•	Publishing & Notifications – Posts to WordPress, tweets, and sends Slack alerts.
8 Testing Composio Integration
•	python test_composio.py
•	- Checks if Composio API key is loaded.
•	- Lists available Composio tools (summarize, rewrite).
9 Troubleshooting
•	ModuleNotFoundError: Install missing package with pip install <package>.
•	API Key Not Found: Ensure .env contains valid keys.
•	Slack Posting Fails: Verify SLACK_TOKEN and SLACK_CHANNEL.
•	Google Trends TooManyRequestsError: Script retries with backoff; increase wait times if needed.
10 Author & License
•	Author: Ashwini SR(TEAM LEAD)
•	                R Sai Deepika(TEAM MEMBER)
•	                Vidya Shakthi(TEAM MEMBER)
•	                 Girish (TEAM MEMBER)
•	GitHub: https://github.com/vidyashakthi07
•	                https://github.com/girishgr0124
•	                https://github.com/deepika8-hub
•	                https://github.com/Ashwini-SR                
•	License: MIT License
