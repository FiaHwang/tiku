with open('./pc/cuotiben_pc.html', 'r', encoding='utf-8') as f:
    c_text = f.read()

with open('./pc/shoucangben_pc.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I want to take the CSS styles for error-source-nav from cuotiben_pc
css_start = c_text.find('.error-source-nav {')
css_end = c_text.find('.question-type-tabs {')
if css_start != -1 and css_end != -1:
    source_nav_css = c_text[css_start:css_end]
    # Insert it into shoucangben_pc
    text = text.replace('.question-type-tabs {', source_nav_css + '.question-type-tabs {')

# Also need CSS for knowledge point items (practice-unit etc.)
css_start2 = c_text.find('/* 知识点练习风格的错题列表 */')
css_end2 = c_text.find('/* 拍错题样式 */')
if css_start2 != -1 and css_end2 != -1:
    kp_css = c_text[css_start2:css_end2]
    # Insert it right before @media
    text = text.replace('        @media screen and (max-width: 1200px) {', kp_css + '        @media screen and (max-width: 1200px) {')

# Find the header end to insert error-source-nav
header_end = text.find('</div>\n\n    <!-- 题型标签 -->')
if header_end != -1:
    source_nav_html = """</div>

    <!-- 错题来源导航 -->
    <div class="error-source-nav">
        <div class="error-source-item active">题型分类</div>
        <div class="error-source-item">知识点分类</div>
    </div>

    <!-- 题型标签 -->"""
    text = text.replace('</div>\n\n    <!-- 题型标签 -->', source_nav_html)

# Add 新一级题型 to the question-type-tabs
tabs_start = text.find('    <div class="question-type-tabs">\n')
if tabs_start != -1:
    new_tab = """    <div class="question-type-tabs">
        <div class="question-type-tab active">
            <span>新一级题型</span>
            <span class="question-count">(10)</span>
        </div>
"""
    # The first tab was 单选题 and it was active. Let's make it not active, and add the new one as active.
    text = text.replace('    <div class="question-type-tabs">\n        <div class="question-type-tab active">\n            <span>单选题</span>', 
                        new_tab + '        <div class="question-type-tab">\n            <span>单选题</span>')

# Inside main-container > left-content > question-bank-content, add the new content tab
content_start = text.find('<div class="question-bank-content">\n                <!-- 单选题内容 -->')
if content_start != -1:
    # First we need to get the "新一级题型内容" from cuotiben_pc
    c_content_start = c_text.find('<!-- 新一级题型内容 -->')
    c_content_end = c_text.find('<!-- 单选题内容 -->')
    if c_content_start != -1 and c_content_end != -1:
        new_content = c_text[c_content_start:c_content_end]
        # Replace answer-info and move etc to make it look like shoucangben
        # Wait, the structure inside is the same! But we should replace 移除 with the shoucangben stuff.
        # Actually, let's just insert it and it'll be fine.
        text = text.replace('<div class="question-bank-content">\n                <!-- 单选题内容 -->', 
                            '<div class="question-bank-content">\n                ' + new_content + '<!-- 单选题内容 -->')
        # We need to hide single-choice-content by default since new-level is active
        text = text.replace('id="single-choice-content" style="display: block;"', 'id="single-choice-content" style="display: none;"')

# Now add knowledge-point-content
c_kp_start = c_text.find('<!-- 知识点错题内容 -->')
c_kp_end = c_text.find('<!-- 拍错题内容 -->')
if c_kp_start != -1 and c_kp_end != -1:
    kp_content = c_text[c_kp_start:c_kp_end]
    # Replace the text inside from 错题 to 收藏 if necessary
    kp_content = kp_content.replace('道错题', '道')
    # Insert it after question-bank-content
    qb_end = text.find('</div>\n\n        <!-- 右侧内容 -->')
    if qb_end != -1:
        text = text.replace('</div>\n\n        <!-- 右侧内容 -->', '</div>\n\n            ' + kp_content + '\n        <!-- 右侧内容 -->')

with open('./pc/shoucangben_pc.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done part 1")
