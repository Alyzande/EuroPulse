#!/usr/bin/env python3
"""
EuroPulse Real-Time Threat Dashboard
Supports multiple collector modes:
simulation | reddit | mastodon | bluesky | aggregate
"""

import sys
import os
import time
from pathlib import Path
from flask import Flask, render_template, jsonify, request

# ---------------------------------------------------------
# Path Setup
# ---------------------------------------------------------
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# ---------------------------------------------------------
# Flask Setup
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
print("🧭 TEMPLATE PATH:", BASE_DIR / "templates")

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

# ---------------------------------------------------------
# Global State
# ---------------------------------------------------------
current_mode = os.getenv("COLLECTOR_TYPE", "simulation").lower()
simulation_mode = (current_mode == "simulation")

# ---------------------------------------------------------
# Mode Helper
# ---------------------------------------------------------
def build_collectors(mode: str):
    """Return initialized collectors for French and German."""
    mode = mode.lower()
    print(f"📡 Initializing collectors for mode: {mode}")

    if mode == "simulation":
        from src.data.collectors.threat_collector import ThreatCollector
        return ThreatCollector("fr"), ThreatCollector("de")

    elif mode == "reddit":
        from src.data.collectors.reddit_collector import RedditCollector
        return RedditCollector("fr"), RedditCollector("de")

    elif mode == "mastodon":
        from src.data.collectors.mastodon_collector import MastodonCollector
        return MastodonCollector("fr"), MastodonCollector("de")

    elif mode == "bluesky":
        from src.data.collectors.bluesky_collector import BlueskyCollector
        return BlueskyCollector("fr"), BlueskyCollector("de")

    elif mode == "aggregate":
        from src.data.collectors.aggregated_collector import AggregatedCollector
        return AggregatedCollector("fr"), AggregatedCollector("de")

    else:
        print(f"⚠️ Unknown mode '{mode}', falling back to simulation.")
        from src.data.collectors.threat_collector import ThreatCollector
        return ThreatCollector("fr"), ThreatCollector("de")


# ---------------------------------------------------------
# Flask Routes
# ---------------------------------------------------------
@app.route("/")
def index():
    """Main dashboard page"""
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates", "index.html"))
    print("🧩 Rendering index.html from:", path)
    return render_template("index.html", time=time)

# --- Mode Management ---------------------------------------------------------
@app.route("/api/mode", methods=["POST"])
def set_mode():
    """Switch between data modes"""
    global current_mode, simulation_mode
    data = request.json or {}
    new_mode = data.get("mode", "simulation").lower()

    valid_modes = ["simulation", "reddit", "mastodon", "bluesky", "aggregate"]
    if new_mode not in valid_modes:
        return jsonify({"error": f"Invalid mode: {new_mode}", "success": False}), 400

    os.environ["COLLECTOR_TYPE"] = new_mode
    current_mode = new_mode
    simulation_mode = (new_mode == "simulation")

    print(f"🔄 Switched data mode → {new_mode.upper()}")
    return jsonify({"success": True, "mode": new_mode})

@app.route("/api/mode/status", methods=["GET"])
def get_mode_status():
    """Return current mode"""
    return jsonify({"mode": current_mode, "simulation_mode": simulation_mode})

# --- Threat Data -------------------------------------------------------------
@app.route("/api/threats")
def get_threats():
    """Return collected threat posts for current mode"""
    global current_mode
    print(f"📡 Fetching threats for mode: {current_mode}")

    fr_collector, de_collector = build_collectors(current_mode)
    fr_posts = fr_collector.collect_recent_posts(limit=8)
    de_posts = de_collector.collect_recent_posts(limit=8)
    threats = fr_posts + de_posts

    return jsonify({
        "threats": threats,
        "total_threats": len(threats),
        "timestamp": time.time(),
    })

@app.route("/api/stats")
def get_stats():
    """Return summary threat statistics"""
    try:
        from src.processing.threat_classifier import ThreatClassifier
        from src.processing.location_extractor import LocationExtractor
        from src.processing.text_cleaner import TextCleaner

        fr_collector, de_collector = build_collectors(current_mode)
        posts = fr_collector.collect_recent_posts(limit=8) + de_collector.collect_recent_posts(limit=8)

        threat_classifier = ThreatClassifier("fr")  # language doesn’t matter for summary
        threat_types = {}
        risk_levels = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        countries = {}
        languages = {"fr": 0, "de": 0}

        for post in posts:
            classification = post.get("threat_classification", {})
            threat_type = classification.get("primary_threat", "unknown")
            risk_level = classification.get("risk_level", "low")
            threat_types[threat_type] = threat_types.get(threat_type, 0) + 1
            risk_levels[risk_level] = risk_levels.get(risk_level, 0) + 1
            languages[post.get("language", "unknown")] = languages.get(post.get("language", "unknown"), 0) + 1
            for loc in post.get("locations", []):
                country = loc.get("country", "unknown")
                countries[country] = countries.get(country, 0) + 1

        return jsonify({
            "total_threats": len(posts),
            "threat_types": threat_types,
            "risk_levels": risk_levels,
            "countries": countries,
            "languages": languages,
        })
    except Exception as e:
        print(f"⚠️ Stats computation failed: {e}")
        return jsonify({
            "total_threats": 0,
            "threat_types": {},
            "risk_levels": {},
            "countries": {},
            "languages": {},
        })

@app.route("/api/health")
def health_check():
    return jsonify({"status": "healthy", "timestamp": time.time()})

# ---------------------------------------------------------
# Run Flask App
# ---------------------------------------------------------
if __name__ == "__main__":
    print("🚀 EuroPulse Dashboard Starting...")
    print("📍 Access at: http://localhost:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
