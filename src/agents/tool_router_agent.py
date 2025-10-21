import os
from composio.sdk import Composio

class ToolRouterAgent:
    def __init__(self):
        api_key = os.getenv("COMPOSIO_API_KEY")
        if not api_key:
            raise ValueError("COMPOSIO_API_KEY not found in environment variables.")
        # Initialize Composio instance with API key
        self.client = Composio(provider={"api_key": api_key})

    def summarize(self, text):
        # Use the Composio instance to call a summarization task
        result = self.client.run("summarize", input_text=text)
        return result

    def rewrite_for_platforms(self, text, platforms):
        results = {}
        for platform in platforms:
            results[platform] = self.client.run("rewrite", input_text=text, platform=platform)
        return results
