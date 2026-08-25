"""Minimal npm package search API call — one typed row per package.

Docs & schema: https://quanticdata.io/collectors/npm-registry-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/npm_packages/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "react state management",
        "max_results": 20
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("name"), row.get("version"), row.get("description"))
print(f"{len(data['results'])} packages, cost ${data['cost']}")
