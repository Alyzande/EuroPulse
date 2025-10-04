#!/usr/bin/env python3
"""
Test our text cleaner
"""

import sys
sys.path.append('src')

from processing.text_cleaner import TextCleaner

def test_cleaner():
    print("🧪 Testing Text Cleaner")
    print("=" * 40)
    
    # Test French cleaning
    print("\n🇫🇷 French text cleaning:")
    fr_cleaner = TextCleaner('fr')
    
    dirty_text = "Fusillade @gare_du_nord! http://example.com #urgence"
    clean_text = fr_cleaner.clean_text(dirty_text)
    
    print(f"✅ Cleaned: '{clean_text}'")
    
    # Test German cleaning
    print("\n🇩🇪 German text cleaning:")
    de_cleaner = TextCleaner('de')
    
    dirty_text = "Schießerei @Hbf! http://test.com #Notfall"
    clean_text = de_cleaner.clean_text(dirty_text)
    
    print(f"✅ Cleaned: '{clean_text}'")

if __name__ == "__main__":
    test_cleaner()