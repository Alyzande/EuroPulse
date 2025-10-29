"""
Text preprocessing for social media posts
Cleans French and German text for threat detection
"""

import re
import os


class TextCleaner:
    """Cleans and normalizes social media text"""

    def __init__(self, language: str = 'fr'):
        self.language = language
        # Debug mode is enabled only if DEBUG_TEXTCLEANER=true in .env
        self.debug = os.getenv("DEBUG_TEXTCLEANER", "false").lower() == "true"
        if self.debug:
            print(f"🧹 Text cleaner initialized for {language} (debug mode)")

    def clean_text(self, text: str) -> str:
        """
        Clean social media text step by step.
        Debug prints only if DEBUG_TEXTCLEANER=true is set in .env
        """
        if not text:
            return ""

        if self.debug:
            print(f"   Original: {text}")

        # Step 1: Remove URLs
        text = self._remove_urls(text)
        if self.debug:
            print(f"   No URLs:  {text}")

        # Step 2: Remove mentions and hashtags
        text = self._remove_mentions_hashtags(text)
        if self.debug:
            print(f"   Cleaned:  {text}")

        # Step 3: Remove punctuation
        text = self._remove_punctuation(text)
        if self.debug:
            print(f"   Final:    {text}")

        return text.strip()

    def _remove_urls(self, text: str) -> str:
        """Remove URLs from text"""
        return re.sub(r'http\S+', '', text)

    def _remove_mentions_hashtags(self, text: str) -> str:
        """Remove @mentions and #hashtags"""
        text = re.sub(r'@\w+', '', text)  # Remove @mentions
        text = re.sub(r'#\w+', '', text)  # Remove #hashtags
        return text

    def _remove_punctuation(self, text: str) -> str:
        """Remove punctuation except for important threat indicators"""
        # Keep ! and ? which might indicate urgency
        return re.sub(r'[^\w\s!?]', '', text)
