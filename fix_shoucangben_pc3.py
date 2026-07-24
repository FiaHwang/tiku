with open('./pc/shoucangben_pc.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

js_to_add = """
        // 错题来源切换事件
        document.querySelectorAll('.error-source-item').forEach(item => {
            item.addEventListener('click', () => {
                document.querySelectorAll('.error-source-item').forEach(i => i.classList.remove('active'));
                item.classList.add('active');
                
                const text = item.textContent.trim();
                
                if (text === '题型分类' || text === '知识点分类') {
                    localStorage.setItem('shoucangben_active_tab_pc', text);
                }
                
                if (text === '题型分类') {
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
                }
            });
        });
        
        // 页面加载完成后，恢复 tab
        window.addEventListener('load', () => {
            let savedTab = localStorage.getItem('shoucangben_active_tab_pc') || '题型分类';
            if (savedTab === '按题型') savedTab = '题型分类';
            if (savedTab === '按知识点') savedTab = '知识点分类';
            const items = document.querySelectorAll('.error-source-item');
            let matchedTab = null;
            items.forEach(item => {
                if (item.textContent.trim() === savedTab) {
                    matchedTab = item;
                }
            });
            if (matchedTab) {
                matchedTab.click();
            }
        });
        
        function toggleKnowledgeUnit(header) {
            const icon = header.querySelector('.fa-chevron-right') || header.querySelector('.fa-chevron-down');
            const content = header.parentElement.querySelector('.unit-content');
            
            if (content.style.display === 'none' || !content.style.display) {
                content.style.display = 'block';
                if (icon) {
                    icon.classList.remove('fa-chevron-right');
                    icon.classList.add('fa-chevron-down');
                }
            } else {
                content.style.display = 'none';
                if (icon) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-right');
                }
            }
        }

        function showKnowledgeCategory(name, count) {
            if (count === 0) {
                alert('该知识点目前没有收藏哦！');
                return;
            }
            window.location.href = 'cuotiben_shiti_chakan_pc.html?type=' + encodeURIComponent(name);
        }
"""

text = text.replace('// 题型标签点击事件', js_to_add + '        // 题型标签点击事件')

with open('./pc/shoucangben_pc.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done part 3 JS")
