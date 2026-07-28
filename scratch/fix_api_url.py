with open('templates.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace strict url logic
old_str = "API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'\n            ? window.location.origin\n            : 'https://iqro.onrender.com';"

new_str = "API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.hostname.includes('ngrok') || /^\\d+\\.\\d+\\.\\d+\\.\\d+$/.test(window.location.hostname))\n            ? ''\n            : (window.__IQRO_API_URL || 'https://iqro.onrender.com');"

content = content.replace("window.location.origin", "''")
content = content.replace("https://iqro.onrender.com", "")

with open('templates.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated API_BASE_URL to relative path successfully!")
