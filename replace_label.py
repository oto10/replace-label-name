import os
import glob
import sys
from pathlib import Path

def replace_label_name():
    args = sys.argv
    if len(args) != 3:
        print('以下の形式で変更前のラベル名と変更後のラベル名を指定してください。')
        print('$ replace_label.py pre-label-name post-label-name')
        sys.exit(1)

    files = glob.glob('/path/to/folder/*.json') # パスの設定
    for file in files:
        read_path = Path(file)
        content = read_path.read_text()
        pre_label_name = f'\"label\": \"{args[1]}\"'
        post_label_name = f'\"label\": \"{args[2]}\"'
        content = content.replace(pre_label_name, post_label_name)
        read_path.write_text(content)
        
if __name__ == '__main__':
    replace_label_name()