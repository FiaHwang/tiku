import re

with open('./mobile/cuotiben.html', 'r', encoding='utf-8') as f:
    cuotiben = f.read()

with open('./mobile/shoucangben.html', 'r', encoding='utf-8') as f:
    shoucangben = f.read()

# Extract from <div class="source-tabs"> to the end of <div class="error-category-container">
content_match = re.search(r'(<div class="source-tabs">.*?</div>\s*<!-- 提示信息 -->.*?<div class="error-category-container">.*?</div>\s*</div>)', cuotiben, re.DOTALL)
if content_match:
    cuotiben_content = content_match.group(1)
    # Remove 拍错题 tab
    cuotiben_content = re.sub(r'<div class="source-tab">拍错题</div>', '', cuotiben_content)
    
    # Replace content in shoucangben
    # Currently shoucangben has double source-tabs, we'll replace from the first <div class="source-tabs"> up to the end of <div class="error-category-container">
    shoucangben = re.sub(r'<div class="source-tabs">.*?</div>\s*</div>', cuotiben_content, shoucangben, flags=re.DOTALL)
    
    # Also we need to inject the JS logic for tabs if it's not there.
    # The JS in cuotiben for sourceTabs is:
    # const sourceTabs = document.querySelectorAll('.source-tab');
    # ...
    # We will extract it from cuotiben
    js_match = re.search(r'(const sourceTabs = document.querySelectorAll\(\'.source-tab\'\);.*?)// 设置弹窗逻辑', cuotiben, re.DOTALL)
    if js_match:
        source_tabs_js = js_match.group(1)
        # Remove 拍错题 logic
        source_tabs_js = re.sub(r'\} else if \(text === \'拍错题\'\).*?\}', '}', source_tabs_js, flags=re.DOTALL)
        # Replace cuotiben_active_tab with shoucangben_active_tab
        source_tabs_js = source_tabs_js.replace('cuotiben_active_tab', 'shoucangben_active_tab')
        
        # Inject into shoucangben.html right before <div id="toast"
        # Wait, let's see if shoucangben already has it. It probably doesn't.
        if 'const sourceTabs = document.querySelectorAll(' not in shoucangben:
            # We can insert it inside the script tag, after window.addEventListener('load', ...
            shoucangben = shoucangben.replace("window.addEventListener('load', () => {", f"{source_tabs_js}\n        window.addEventListener('load', () => {{")

    with open('./mobile/shoucangben.html', 'w', encoding='utf-8') as f:
        f.write(shoucangben)
    print("Fixed shoucangben")
else:
    print("Could not find content in cuotiben")
