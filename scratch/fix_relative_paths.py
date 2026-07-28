with open('templates.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace API_BASE_URL definitions with dynamic function/expression that works anywhere
old_expr = "const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'\n            ? ''\n            : '';"

new_expr = "const API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.hostname.includes('ngrok') || /^\\d+\\.\\d+\\.\\d+\\.\\d+$/.test(window.location.hostname))\n            ? ''\n            : (window.__IQRO_API_URL || 'https://iqro.onrender.com');"

# Remove all API_BASE_URL prefix in fetches so it always uses standard relative URL
content = content.replace('${API_BASE_URL}/', '/')
content = content.replace('io(API_BASE_URL)', 'io()')

with open('templates.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated all API calls to relative paths!")
