import re

with open('./mobile/shoucangben.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r"\s*\} else if \(text === '拍错题'\) \{\s*console\.log\('跳转到拍错题列表'\);\s*", ' ', text)

with open('./mobile/shoucangben.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed 拍错题 logic from mobile shoucangben")
