try:
    import sklearn
    print(f"✅ sklearn version: {sklearn.__version__}")
    
    # Test specific components we'll need
    from sklearn.cluster import KMeans
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("✅ All sklearn components imported successfully!")
    
except ImportError as e:
    print(f"❌ Error: {e}")