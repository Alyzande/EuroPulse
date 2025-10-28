# EuroPulse: Real-Time Physical Threat Detection

EuroPulse detects emerging **physical threats and dangerous events** in French- and German-language social media in real time.  
It is designed for **intelligence analysis**, **emergency response monitoring**, and **early warning of violent or disruptive incidents**.

---

## 🚨 Project Focus

- **Weak-Signal Detection** – identifies small clusters of early posts before official reports appear  
- **Threat Categories** – shootings, explosions, stabbings, riots, vehicle attacks  
- **Languages** – French 🇫🇷 and German 🇩🇪  
- **Real-Time Analysis** – updates every few seconds  
- **Operational Context** – police, emergency services, and intelligence analysis

---

## 🧠 Operating Modes

EuroPulse can switch between live data sources directly from the dashboard.

| Mode | Source | Description |
|------|---------|-------------|
| 🧠 **Simulation** | Mock data generator | Safe demo / offline mode with synthetic incidents |
| 🧵 **Reddit** | Reddit API | Monitors French and German posts mentioning threat indicators |
| 🐘 **Mastodon** | Public Mastodon timelines | Uses Weak Signal Detector to flag early posts about physical events |
| 💬 **Bluesky** | (in development) | Will track early public safety signals from Bluesky |
| 🌍 **Aggregate** | Combined | Merges Reddit + Mastodon (+ Bluesky) for maximum coverage |

Switch modes instantly via the dashboard buttons, or set the default mode in your `.env`:

```bash
# Operation mode
COLLECTOR_TYPE=simulation


## 🎯 Target Threats

- **Active violence**: shootings, stabbings, attacks
- **Explosives**: bombs, suspicious packages, detonations
- **Vehicle attacks**: cars/trucks used as weapons
- **Public transport incidents**: subway, train, bus attacks
- **Urban violence**: riots, large fights, mass casualties

## 🌍 Coverage Areas

### 🇫🇷 French-Speaking Regions:
**Europe**: France, Belgium (Wallonia/Brussels), Switzerland (Romandy), Luxembourg, Monaco  
**Americas**: Canada (Quebec)  
**Africa**: DR Congo, Ivory Coast, Cameroon, Senegal, Mali, Burkina Faso, Niger, Chad

### 🇩🇪 German-Speaking Regions:
**Europe**: Germany, Austria, Switzerland (German cantons), Belgium (German community), Luxembourg, Liechtenstein  
**Communities**: Italy (South Tyrol), Namibia, Brazil

### 🎯 High-Priority Monitoring:
- **Major cities**: Paris, Berlin, Brussels, Vienna, Geneva
- **Transport hubs**: airports, train stations, metro systems
- **Conflict zones**: Sahel region, urban crisis areas

## 🚀 Quick Start

```bash
# Test environment
python test_environment.py

# Install dependencies
pip install -r requirements.txt

# Test threat detection
python test_threat_collector.py
```

## 📁 Project Structure

- `src/data/collectors/` - Social media threat data collection
- `src/processing/detectors/` - Threat analysis and clustering
- `src/visualization/dashboard/` - Real-time threat dashboard

## 🔧 Tech Stack

- Python 3.8+
- Flask dashboard (real-time web UI)
- Hugging Face Transformers for multilingual NLP
- Weak Signal Detector (custom algorithm)
- HDBSCAN clustering for threat grouping
- Reddit / Mastodon / Bluesky APIs for live collection

## 🛡️ Use Cases

- **Law Enforcement**: Real-time threat awareness
- **Emergency Services**: Rapid incident detection
- **Security Teams**: Corporate and event security
- **Intelligence**: Pattern analysis and early warning

---

**Note**: This system is designed for legitimate security and public safety applications. Always comply with local laws and platform terms of service.