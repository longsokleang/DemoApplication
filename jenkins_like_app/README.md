# Jenkins-like NiceGUI App

This is a Jenkins-inspired (not identical) dashboard built with NiceGUI.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Open http://127.0.0.1:8080 in your browser.

## Structure
- `main.py`: app entry, routes, theme include
- `components/`: layout and header/sidebar
- `pages/`: dashboard, nodes, builds, console
- `state.py`: in-memory data models and state
- `data.py`: background simulation
- `assets/theme.css`: Jenkins-inspired theme

## Notes
All data is simulated for demo purposes.