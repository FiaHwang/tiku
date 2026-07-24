#!/bin/bash
# Insert CSS
sed -i 's/<\/style>/        .header-right-actions { position: absolute; right: 16px; top: 50%; transform: translateY(-50%); display: flex; align-items: center; gap: 12px; }\n        .action-icon-btn { border: none; background: transparent; font-size: 18px; color: #333; cursor: pointer; padding: 4px; }\n<\/style>/' ./mobile/shoucangben.html

# Insert Header HTML
sed -i 's/<div class="nav-tabs">/<div class="header-right-actions">\n            <button class="action-icon-btn" onclick="showToast('\''导出成功'\'')"><i class="fas fa-file-export"><\/i><\/button>\n        <\/div>\n        <div class="nav-tabs">/' ./mobile/shoucangben.html

# Insert Toast HTML & JS
sed -i '/<\/body>/i \    <div id="toast" style="display: none; position: fixed; bottom: 100px; left: 50%; transform: translateX(-50%); background: rgba(0,0,0,0.7); color: white; padding: 10px 20px; border-radius: 20px; z-index: 2000; font-size: 14px; white-space: nowrap;"><\/div>\n    <script>\n        function showToast(msg) {\n            const toast = document.getElementById('\''toast'\'');\n            toast.textContent = msg;\n            toast.style.display = '\''block'\'';\n            setTimeout(() => { toast.style.display = '\''none'\''; }, 2000);\n        }\n    <\/script>' ./mobile/shoucangben.html
