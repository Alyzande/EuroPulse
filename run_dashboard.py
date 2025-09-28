#!/usr/bin/env python3
"""
Simple runner for EuroPulse Dashboard
"""

import sys
import os

# Add current directory to path so imports work
sys.path.append(os.path.dirname(__file__))

from src.visualization.dashboard.app import app

if __name__ == '__main__':
    print("🚀 EuroPulse Dashboard Starting...")
    print("📍 Access at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop")
    app.run(debug=True, host='0.0.0.0', port=5000)