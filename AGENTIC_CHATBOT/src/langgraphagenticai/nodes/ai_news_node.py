import os
from typing_extensions import TypedDict

class AINewsNode:
    """
    Node for fetching and summarizing AI news based on selected time frame.
    """
    def __init__(self, llm):
        self.llm = llm

    def fetch_news(self, state: dict) -> dict:
        """
        Fetches AI news articles based on the selected time frame.
        Expects state['messages'] to contain the time frame: 'Daily', 'Weekly', or 'Monthly'.
        """
        msg = state["messages"][0] if isinstance(state["messages"], list) else state["messages"]
        if hasattr(msg, "content"):
            time_frame = str(msg.content).lower()
        else:
            time_frame = str(msg).lower()
        # Simulate fetching news (replace with actual API call if available)
        news_content = f"Fetched {time_frame} AI news articles."
        return {"messages": [news_content, time_frame]}

    def summarize_news(self, state: dict) -> dict:
        """
        Summarizes the fetched AI news articles.
        """
        news_content = state["messages"][0] if state["messages"] else ""
        # Simulate summarization (replace with actual LLM call if available)
        summary = f"Summary of {news_content}"
        # Pass time_frame along for saving
        time_frame = state["messages"][1] if len(state["messages"]) > 1 else "daily"
        return {"messages": [summary, time_frame]}

    def save_result(self, state: dict) -> dict:
        """
        Saves the summarized news to a markdown file and returns the file path.
        """
        summary = state["messages"][0] if state["messages"] else ""
        time_frame = state["messages"][1] if len(state["messages"]) > 1 else "daily"
        filename = f"./AINews/{time_frame}_summary.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(summary))
        return {"messages": [f"News summary saved to {filename}"]}