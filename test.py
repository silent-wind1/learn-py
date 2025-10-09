import requests
import random
from datetime import datetime

# 设置请求参数
url = "https://steps.hubp.de/api"
account = "xxx@qq.com"
password = "xxxx+"

# 获取当前星期几 (0=周一, 1=周二, ..., 6=周日)
weekday = datetime.today().weekday()

# 根据星期几生成步数范围
if weekday < 5:  # 周一到周五 (0-4)
    steps = random.randint(12869, 21040)
else:  # 周六和周日 (5-6)
    steps = random.randint(14646, 28398)

# 构建POST数据
data = {
    "account": account,
    "password": password,
    "steps": 28642
}

# 设置浏览器请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

# 发送POST请求
try:
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()  # 检查HTTP错误

    # 打印响应结果
    print("请求成功！")
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
    print(f"已提交步数: {steps}")

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
