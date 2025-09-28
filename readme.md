# EuroPulse: Real-time Physical Threat Detection

Detect emerging physical threats and dangerous events in French and German-speaking social media in real-time. Designed for intelligence analysis and emergency response monitoring.

## 🚨 Project Focus

- **Threat Detection**: Shootings, explosions, vehicle attacks, riots, stabbings
- **Languages**: French & German content
- **Real-time** detection without sentiment reliance
- **Police/emergency response** relevance
- **Intelligence analysis** for fast-moving dangerous events

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
- Hugging Face Transformers (multilingual)
- HDBSCAN clustering for threat grouping
- Real-time streaming analysis
- Twitter/Reddit APIs for live data

## 🛡️ Use Cases

- **Law Enforcement**: Real-time threat awareness
- **Emergency Services**: Rapid incident detection
- **Security Teams**: Corporate and event security
- **Intelligence**: Pattern analysis and early warning

---

**Note**: This system is designed for legitimate security and public safety applications. Always comply with local laws and platform terms of service.