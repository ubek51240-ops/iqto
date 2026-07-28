import os
from flask import render_template_string

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

with open('admin.html', 'r', encoding='utf-8') as f:
    adm = f.read()

# Add badge HTML to admin.html menu item
adm = adm.replace(
    '<i class="fa-solid fa-bag-shopping"></i> Buyurtmalar\n                        </a>',
    '<i class="fa-solid fa-bag-shopping"></i> Buyurtmalar\n                            <span class="unread-badge" id="ordersBadge" style="background:#ef4444;">0</span>\n                        </a>'
)

# Add badge JS logic to admin.html renderOrders
target_js = "document.getElementById('statOrdersCount').innerText = allOrders.length;"
replacement_js = """document.getElementById('statOrdersCount').innerText = allOrders.length;
                    const newOrdersCount = (allOrders || []).filter(o => o.status === 'Qabul qilindi').length;
                    const obadge = document.getElementById('ordersBadge');
                    if (obadge) {
                        if (newOrdersCount > 0) {
                            obadge.innerText = newOrdersCount;
                            obadge.style.display = 'inline-block';
                        } else {
                            obadge.innerText = '0';
                            obadge.style.display = 'none';
                        }
                    }"""

adm = adm.replace(target_js, replacement_js)

with open('templates.py', 'w', encoding='utf-8') as f:
    f.write('from flask import render_template_string\n\n')
    f.write('INDEX_TEMPLATE = ' + repr(idx) + '\n\n')
    f.write('ADMIN_TEMPLATE = ' + repr(adm) + '\n\n')
    f.write('def get_index_page():\n    return render_template_string(INDEX_TEMPLATE)\n\n')
    f.write('def get_admin_page():\n    return render_template_string(ADMIN_TEMPLATE)\n')

print("templates.py successfully regenerated with orders badge!")
