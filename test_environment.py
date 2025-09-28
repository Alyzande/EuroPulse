#!/usr/bin/env python3
"""
EuroPulse - Environment Test Script
Validates that Python and basic dependencies are working
"""

import sys
import platform

def check_environment():
    print("🔧 EuroPulse - Environment Check")
    print("=" * 40)
    
    # Python version check
    python_version = platform.python_version()
    print(f"✅ Python Version: {python_version}")
    
    # Check critical packages
    required_packages = ['requests', 'numpy', 'pandas']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package:15} - OK")
        except ImportError:
            print(f"❌ {package:15} - MISSING")
    
    print("\n🎯 Next steps:")
    print("1. Run: git init")
    print("2. Create requirements.txt")
    print("3. Initial commit & GitHub setup")

if __name__ == "__main__":
    check_environment()