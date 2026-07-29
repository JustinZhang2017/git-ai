# Website API and pre-push hook

This directory provides:

- A simple Flask API to receive push payloads at POST /api/push and store them under website/received/.
- A local scanner script (scan_ai.py) that searches the repo for likely AI-generated code (by keywords) and POSTs results to the API.
- A pre-push hook wrapper and installer that runs the scanner before git push.

See usage below.
