#loading packages
from sys import argv
import sys

# 输入文件名
input_file = argv[1] # 更改为您的FA文件名
replace_file = argv[2] # 更改为您的替换文件名
output_file = argv[3] # 更改为新的输出文件名

# 读取fasta文件
with open(input_file, 'r') as f:
    fasta_lines = f.readlines()

# 读取替换文件
replacements = {}
with open(replace_file, 'r') as f:
    for line in f:
        (old_str, new_str) = line.strip().split('\t')
        replacements[old_str] = new_str

# 对fasta文件进行替换并保存
with open(output_file, 'w') as f:
    for line in fasta_lines:
        # 判断当前行是否以>开头
        if line.startswith('>'):
            # 处理注释行并进行替换
            seq_id = line.split('>')[1].strip() # 获取序列ID
            if seq_id in replacements: # 如果序列ID存在于替换文件中
                new_seq_id = replacements[seq_id]
                line = line.replace(seq_id, new_seq_id)
                f.write(line)
            else:
                # 当seq_id不在replacements中时输出日志并退出程序
                print(seq_id + '不在替换集中，程序退出运行，请检查您的替换集')
                sys.exit()
        else:
            # 不以>开头的行不做修改
            f.write(line)