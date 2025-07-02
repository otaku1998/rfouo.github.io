import os
from bs4 import BeautifulSoup

# 获取当前路径
current_path = os.path.dirname(os.path.abspath(__file__))
print("脚本所在路径是：", current_path)



# 遍历当前路径下的所有文件
for filename in os.listdir(current_path):
    if filename.endswith(".html"):
        filepath = os.path.join(current_path, filename)

        # 读取 HTML 文件
        with open(filepath, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            # 查找所有 class 为 "display-7" 的元素并删除
            for element in soup.find_all(class_='display-7'):
                element.decompose()

        # 将修改后的 HTML 保存回文件
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("所有 class='display-7' 元素已删除。")
