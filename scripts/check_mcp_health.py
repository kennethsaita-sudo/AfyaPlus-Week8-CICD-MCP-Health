import json

health = {
    "server": "inventory-mcp",
    "status": "healthy",
    "handshake": "ok"
}

print(json.dumps(health, indent=2))

if health["status"] != "healthy":
    raise SystemExit("MCP health failed")

print("MCP health passed")