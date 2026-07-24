with open('./mobile/shoucangben.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# We want to keep everything up to <!-- 提示信息 --> but before that, there's multiple <div class="source-tabs">...</div>
# Let's just find the header end.
header_end_idx = text.find('</header>') + len('</header>')
script_start_idx = text.find('<script>', header_end_idx)

# Inside cuotiben, extract from right after </header> up to <script>
with open('./mobile/cuotiben.html', 'r', encoding='utf-8') as f:
    c_text = f.read()
c_header_end = c_text.find('</header>') + len('</header>')
c_script_start = c_text.find('<script>', c_header_end)
# also remove the settings modal html which is after </header> but before source-tabs
c_middle = c_text[c_header_end:c_script_start]

# We need to remove 拍错题 tab
c_middle = re.sub(r'<div class="source-tab">拍错题</div>', '', c_middle)

# Let's replace the whole middle part
text = text[:header_end_idx] + '\n' + c_middle + '\n' + text[script_start_idx:]

with open('./mobile/shoucangben.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done fixing HTML")
