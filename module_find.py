import re


with open('verilog/test.sv', encoding='utf-8') as f:
    contents = f.read()
    # print(contents)

# s = '((a + b) * (c - d)) + (e / (f + g))'
s = contents
pattern = r'(\w*)\s*#*(\w*)\s*\((?:[^)(]|\((?:[^)(]+|\([^)(]*\))*\))*\)'
matches = re.findall(pattern, s, re.DOTALL)
print(matches)