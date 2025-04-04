import pymysql
import requests
import os

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'my_yefeng',
    'charset': 'utf8mb4'
}


# 下载图片并保存的函数
def download_image(image_url, save_path):
    try:
        # 发送GET请求下载图片
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # 如果请求失败，会抛出异常

        # 保存图片
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"图片保存成功: {save_path}")
    except Exception as e:
        print(f"下载图片失败: {image_url}, 错误信息: {e}")


# 从数据库查询图片地址的函数
def get_image_urls_from_db():
    try:
        # 连接数据库
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # 查询图片URL
        query = "select card_name, front_img, backend_img from xcx_member;"
        cursor.execute(query)

        # 获取所有图片地址
        image_urls = cursor.fetchall()
        return image_urls  # 提取出每行的第一个元素（图片地址）

    except Exception as e:
        print(f"查询数据库失败: {e}")
    finally:
        if connection:
            connection.close()


# 主函数
def main():
    # 获取图片地址
    image_urls = get_image_urls_from_db()

    if image_urls:
        # 创建文件保存的目录
        save_dir = "downloaded_images"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 下载每一张图片
        for card_name, card_code, front_image_url, back_image_url in image_urls:
            file_name_front = os.path.join(save_dir, f"{card_name}-身份证前.jpg")
            download_image(front_image_url, file_name_front)
            file_name_back = os.path.join(save_dir, f"{card_name}-身份证后.jpg")
            download_image(back_image_url, file_name_back)
    else:
        print("没有找到图片URL")


if __name__ == "__main__":
    main()
