"""
JSON Formatter – Take a JSON file and print it in a readable format.
"""


import json

with open("data.json") as f:
    data = json.load(f)

print(f"App: {data['app_name']} (v{data['version']})")
print(f"Debug: {'Enabled' if data['debug'] else 'Disabled'}")
print(f"Max Connections: {data['max_connections']}")
print(f"Primary Database: {data['databases']['primary']}")
if "replica" in data['databases']:
    print(f"Replica Database: {data['databases']['replica']}")

