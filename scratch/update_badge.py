with open('templates.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Target sidebar menu item for Buyurtmalar
target1 = '"fa-solid fa-bag-shopping"></i> Buyurtmalar\\n                        </a>'
replacement1 = '"fa-solid fa-bag-shopping"></i> Buyurtmalar\\n                            <span class="unread-badge" id="ordersBadge" style="background:#ef4444;">0</span>\\n                        </a>'

if target1 in content:
    content = content.replace(target1, replacement1)
    print("1. Menu badge HTML inserted!")
else:
    print("1. target1 not found")

# Target renderOrders badge update JS logic
target2 = 'document.getElementById(\\\'statOrdersCount\\\').innerText = allOrders.length;'
replacement2 = '''document.getElementById(\\'statOrdersCount\\').innerText = allOrders.length;
                    const newOrdersCount = (allOrders || []).filter(o => o.status === \'Qabul qilindi\').length;
                    const obadge = document.getElementById(\'ordersBadge\');
                    if (obadge) {
                        if (newOrdersCount > 0) {
                            obadge.innerText = newOrdersCount;
                            obadge.style.display = \'inline-block\';
                        } else {
                            obadge.innerText = \'0\';
                            obadge.style.display = \'none\';
                        }
                    }'''

if target2 in content:
    content = content.replace(target2, replacement2)
    print("2. JS badge calculation logic inserted!")
else:
    print("2. target2 not found")

with open('templates.py', 'w', encoding='utf-8') as f:
    f.write(content)
