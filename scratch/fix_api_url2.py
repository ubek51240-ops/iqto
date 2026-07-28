with open('templates.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = "    const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'\n            ? ''\n            : '';"

replacement = "    const API_BASE_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.hostname.includes('ngrok') || /^\\d+\\.\\d+\\.\\d+\\.\\d+$/.test(window.location.hostname)) ? '' : (window.__IQRO_API_URL || 'https://iqro.onrender.com');"

if target in content:
    content = content.replace(target, replacement)
    with open('templates.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("API_BASE_URL successfully updated in templates.py!")
else:
    print("target not found")
