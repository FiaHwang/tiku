import re

with open('./mobile/cuotiben.html', 'r', encoding='utf-8') as f:
    cuotiben_html = f.read()

with open('./mobile/shoucangben.html', 'r', encoding='utf-8') as f:
    shoucangben_html = f.read()

# Extract CSS from cuotiben
css_match = re.search(r'<style>(.*?)</style>', cuotiben_html, re.DOTALL)
if css_match:
    cuotiben_css = css_match.group(1)
    shoucangben_html = re.sub(r'<style>.*?</style>', f'<style>{cuotiben_css}</style>', shoucangben_html, flags=re.DOTALL)

# Extract source-tabs and error-category-container from cuotiben
# We want from <div class="source-tabs"> up to the end of <div class="error-category-container">
content_match = re.search(r'(<div class="source-tabs">.*</div>\s*<!-- 提示信息 -->\s*<div class="tip">.*?</div>\s*<!-- 错题分类容器 -->\s*<div class="error-category-container">.*?</div>\s*</div>)', cuotiben_html, re.DOTALL)

if content_match:
    cuotiben_content = content_match.group(1)
    # Replace "错题" with "收藏", etc. (be careful)
    cuotiben_content = cuotiben_content.replace('错题本', '收藏本')
    cuotiben_content = cuotiben_content.replace('道错题', '道') # we already changed this, but just in case
    cuotiben_content = cuotiben_content.replace('拍错题', '拍错题') # wait, shoucangben might not need 拍错题. Let's see what the user asked.
    
    # Replace the container in shoucangben
    shoucangben_html = re.sub(r'<!-- 提示信息 -->\s*<div class="tip">.*?</div>\s*<!-- 错题分类容器 -->\s*<div class="error-category-container">.*?</div>', cuotiben_content, shoucangben_html, flags=re.DOTALL)

# Extract JS logic for tabs and modals
js_match = re.search(r'(// 导航切换功能.*?)</script>', cuotiben_html, re.DOTALL)
if js_match:
    cuotiben_js = js_match.group(1)
    
    # We need to preserve shoucangben's top nav tabs routing
    # Let's just do a manual replace or keep it simple.
    
with open('./mobile/shoucangben.html', 'w', encoding='utf-8') as f:
    f.write(shoucangben_html)

print("Done")
