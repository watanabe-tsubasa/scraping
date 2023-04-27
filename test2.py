import re

text = """
# title

content

## title_2_1

content

### title_3_1

content

### title_3_2

content

## title_2_2

content

### title_3_1

content

### title_3_2

```python

# テスト関数
def func():
    pass
```

```

# テスト関数
def func():
    pass
```

"""

# コードブロックのパターンを定義する
pattern_code_block = r"```[\w\s]*\n([\s\S]*?)\n```"

# コードブロックを除去する
text_without_code_blocks = re.sub(pattern_code_block, "", text, flags=re.DOTALL)

# 各段落の # の数をリストに格納する
pattern_heading = r"^(#+)(?!#)(.*)$"
headings = []
for line in text_without_code_blocks.split("\n"):
    match = re.match(pattern_heading, line)
    if match:
    # コードブロック中の # を除外するため、# の前後にスペースを付与する
        heading = match.group(1).strip()
        headings.append(len(heading))

print(headings)