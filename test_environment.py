#!/usr/bin/env python3
"""
EuroPulse - Fixed Environment Test Script
"""

import sys
import platform

def check_package(package_name):
    """Check if a package is installed and return version"""
    try:
        if package_name == 'scikit-learn':
            import sklearn
            return True, sklearn.__version__
        elif package_name == 'python-dotenv':
            import dotenv
            return True, dotenv.__version__
        else:
            module = __import__(package_name)
            if hasattr(module, '__version__'):
                return True, module.__version__
            else:
                return True, "version unknown"
    except ImportError as e:
        return False, f"Import error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def check_environment():
    print("🔧 EuroPulse - Fixed Environment Check")
    print("=" * 50)
    
    # Python version
    python_version = platform.python_version()
    print(f"✅ Python Version: {python_version}")
    
    # Check critical packages
    required_packages = {
        'pandas': 'Data analysis',
        'numpy': 'Numerical computing', 
        'requests': 'API calls',
        'dotenv': 'Environment variables',  # Note: import name is dotenv
        'sklearn': 'Machine learning'       # Note: import name is sklearn
    }
    
    all_ok = True
    for package, description in required_packages.items():
        installed, version = check_package(package)
        if installed:
            print(f"✅ {package:15} {str(version):15} - {description}")
        else:
            print(f"❌ {package:15} {'MISSING':15} - {description}")
            all_ok = False
    
    print("\n" + "=" * 50)
    if all_ok:
        print("🎉 All dependencies installed! Ready to build EuroPulse.")
    else:
        print("⚠️  There might be import issues. Let's debug...")
    
    return all_ok

if __name__ == "__main__":
    check_environment()