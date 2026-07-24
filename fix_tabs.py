import re

with open('./pc/shoucangben_pc.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace block for '题型分类'
old_tab_1 = """                if (text === '题型分类') {
                    document.querySelector('.question-bank-content').style.display = 'block';
                    if (document.querySelector('.knowledge-point-content')) {
                        document.querySelector('.knowledge-point-content').style.display = 'none';
                    }
                    document.querySelector('.question-type-tabs').style.display = 'flex';
                } else if (text === '知识点分类') {
                    document.querySelector('.question-bank-content').style.display = 'none';
                    if (document.querySelector('.knowledge-point-content')) {
                        document.querySelector('.knowledge-point-content').style.display = 'block';
                    }
                    document.querySelector('.question-type-tabs').style.display = 'none';
                }"""

new_tab_1 = """                if (text === '题型分类') {
                    document.querySelector('.question-bank-content').style.display = 'block';
                    if (document.querySelector('.knowledge-point-content')) {
                        document.querySelector('.knowledge-point-content').style.display = 'none';
                    }
                    document.querySelector('.question-type-tabs').style.display = 'flex';
                    if (document.querySelector('.right-sidebar')) document.querySelector('.right-sidebar').style.display = 'block';
                } else if (text === '知识点分类') {
                    document.querySelector('.question-bank-content').style.display = 'none';
                    if (document.querySelector('.knowledge-point-content')) {
                        document.querySelector('.knowledge-point-content').style.display = 'block';
                    }
                    document.querySelector('.question-type-tabs').style.display = 'none';
                    if (document.querySelector('.right-sidebar')) document.querySelector('.right-sidebar').style.display = 'none';
                }"""

text = text.replace(old_tab_1, new_tab_1)

with open('./pc/shoucangben_pc.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Tabs updated")
