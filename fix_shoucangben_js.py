import re

with open('./mobile/shoucangben.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('./mobile/cuotiben.html', 'r', encoding='utf-8') as f:
    c_text = f.read()

# Extract cuotiben script
c_script_match = re.search(r'(// DOM元素获取.*?)// 页面加载完成后执行', c_text, re.DOTALL)
if c_script_match:
    c_script = c_script_match.group(1)
    
    # We want to remove the logic for 'navTabs' (since we have our own in shoucangben) and 'settings-modal' (if it doesn't exist)
    c_script_lines = c_script.split('\n')
    filtered_script = []
    skip = False
    for line in c_script_lines:
        if 'const navTabs = document.querySelectorAll(\'.nav-tab\');' in line:
            skip = True
        if skip and '});' in line and 'navTabs.forEach' not in ''.join(filtered_script): # roughly
            pass # wait this is fragile.
            
# Let's just manually write the script we want to inject.
new_script = """        // DOM元素获取
        const navTabs = document.querySelectorAll('.nav-tab');
        const backBtn = document.querySelector('.back-btn');
        const sourceTabs = document.querySelectorAll('.source-tab');
        
        // 导航切换功能
        navTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                navTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                if (tab.textContent === '错题本') {
                    window.location.href = 'cuotiben.html';
                } else if (tab.textContent === '练习历史') {
                    window.location.href = 'lianxi_lishi.html';
                }
            });
        });

        // 错题来源切换功能
        sourceTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                sourceTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                
                const text = tab.textContent.trim();
                
                if (text === '题型分类') {
                    document.getElementById('by-type-section').style.display = 'grid';
                    document.getElementById('by-knowledge-section').style.display = 'none';
                    localStorage.setItem('shoucangben_active_tab', '题型分类');
                } else if (text === '知识点分类') {
                    document.getElementById('by-type-section').style.display = 'none';
                    document.getElementById('by-knowledge-section').style.display = 'block';
                    localStorage.setItem('shoucangben_active_tab', '知识点分类');
                }
            });
        });

        // 返回按钮功能
        backBtn.addEventListener('click', () => {
            window.location.href = 'tiku.html';
        });

        // 页面加载完成后执行
        window.addEventListener('load', () => {
            // 恢复上次选中的来源标签
            if (sourceTabs && sourceTabs.length > 0) {
                let savedTab = localStorage.getItem('shoucangben_active_tab') || '题型分类';
                const matchedTab = Array.from(sourceTabs).find(t => t.textContent.trim() === savedTab);
                if (matchedTab) {
                    matchedTab.click();
                }
            }
        });
        
        function toggleUnit(header) {
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
        
        function openSystemSelector() {
            showToast('正在打开知识点体系选择...');
        }
        
        function viewKnowledgeWrongQuestions(name, count) {
            if (count === 0) {
                showToast('该知识点目前没有收藏哦！');
                return;
            }
            window.location.href = 'cuotiben_shiti_chakan.html?type=' + encodeURIComponent(name);
        }
"""

text = re.sub(r'// DOM元素获取.*页面加载完成\');\s*\}\);', new_script, text, flags=re.DOTALL)

with open('./mobile/shoucangben.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done JS fix")
