import os
from composio.sdk import Composio

class ToolRouterAgent:
    def __init__(self):
        api_key = os.getenv("COMPOSIO_API_KEY")
        if not api_key:
            raise ValueError("COMPOSIO_API_KEY not found in environment variables.")

        # Initialize Composio client
        self.client = Composio(api_key=api_key)

        # Initialize tools safely
        try:
            # Use get() to access tools safely
            self.summarize_tool = self.client.tools.get("summarize")
            self.rewrite_tool = self.client.tools.get("rewrite")

            if self.summarize_tool is None:
                raise RuntimeError("Summarize tool not found in Composio account.")
            if self.rewrite_tool is None:
                raise RuntimeError("Rewrite tool not found in Composio account.")

        except Exception as e:
            raise RuntimeError(f"Failed to initialize Composio tools: {e}")

    def summarize(self, text):
        """
        Summarize text using Composio's summarize tool
        """
        try:
            response = self.summarize_tool.run(input_text=text)
            # Some SDK versions return an object with output_text
            return getattr(response, "output_text", str(response))
        except Exception as e:
            raise RuntimeError(f"Error during summarization: {e}")

    def rewrite_for_platforms(self, text, platforms):
        """
        Rewrite text for each platform using Composio's rewrite tool
        """
        results = {}
        for platform in platforms:
            try:
                response = self.rewrite_tool.run(input_text=text, platform=platform)
                results[platform] = getattr(response, "output_text", str(response))
            except Exception as e:
                results[platform] = f"❌ Error rewriting for {platform}: {e}"
        return results
