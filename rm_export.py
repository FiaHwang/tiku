import re

for filename in ['./mobile/cuotiben.html', './mobile/shoucangben.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = re.sub(r'<button class="action-icon-btn"[^>]*><i class="fas fa-file-export"></i></button>\s*', '', text)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

print("Export buttons removed")
