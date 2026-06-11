import requests
import json

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTgwNDQ4YjY0ZWM3MjgzYjNmZDhiNDUiLCJpYXQiOjE3ODAyOTQ1NjF9.OaFZc6bUKQJhvZgn0c1vFhioIOp5FNAKujqc3kh8r0I"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Accept-Language": "az",
    "Origin": "https://platform.mylift.az",
    "Referer": "https://platform.mylift.az/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

resp = requests.get(
    "https://api.mylift.az/lifts",
    headers=HEADERS,
    params={"limit": 2, "page": 1, "status": "rn_onreview_government", "sort": "createdAt", "order": "desc"}
)
print("Status:", resp.status_code)
data = resp.json()

# Bütün açarları göstər
print("Top-level keys:", list(data.keys()))
print("total:", data.get("total"))

# İlk elementi tap
items = data.get("data") or data.get("lifts") or data.get("items") or []
print("items tipi:", type(items))
print("items uzunluğu:", len(items))

if items:
    first = items[0]
    print("İlk elementin tipi:", type(first))
    print("İlk element:")
    print(json.dumps(first, ensure_ascii=False, indent=2) if isinstance(first, dict) else repr(first))