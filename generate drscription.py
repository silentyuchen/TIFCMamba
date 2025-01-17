import cv2
import numpy as np
import os
import json

def describe_polyp_position(image, mask):
    """
    根据图片和mask生成息肉位置的详细描述
    """
    # 获取mask中前景的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None, 0  # 如果没有检测到前景，返回空描述和0占比

    # 获取前景的边界框
    x, y, w, h = cv2.boundingRect(contours[0])

    # 获取图片的尺寸
    height, width = image.shape[:2]

    # 计算前景的中心点坐标
    center_x = x + w // 2
    center_y = y + h // 2

    # 更精准的位置描述
    def get_position_description(cx, cy, img_width, img_height):
        # 水平方向
        if cx < img_width / 3:
            horizontal = "left"
        elif cx < 2 * img_width / 3:
            horizontal = "center"
        else:
            horizontal = "right"
        # 垂直方向
        if cy < img_height / 3:
            vertical = "top"
        elif cy < 2 * img_height / 3:
            vertical = "middle"
        else:
            vertical = "bottom"
        return f"{vertical}-{horizontal}"

    position = get_position_description(center_x, center_y, width, height)

    # 计算前景区域占整个图片的比例
    mask_area = cv2.countNonZero(mask)
    image_area = height * width
    coverage_ratio = round((mask_area / image_area) * 100, 1)

    # 生成描述文本
    description = (
        f"The polyp is located in the {position} part of the image. "
        f"Its bounding box has coordinates (x={x}, y={y}, width={w}, height={h}), "
        f"and it covers approximately {coverage_ratio}% of the image."
    )
    return description, coverage_ratio

def process_folder(image_folder, mask_folder, output_file):
    """
    处理文件夹中的所有图片和mask，并生成描述，保存为JSON格式
    """
    # 获取图片文件夹中的所有文件
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    
    # 用于保存结果的列表
    results = []

    for idx, image_file in enumerate(image_files, start=1):
        # 构建图片和mask的路径
        image_path = os.path.join(image_folder, image_file)
        mask_path = os.path.join(mask_folder, image_file)  # 假设图片和mask文件名相同

        # 读取图片和mask
        image = cv2.imread(image_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # 检查图片和mask是否成功加载
        if image is None or mask is None:
            print(f"无法加载图片或mask：{image_file}，跳过处理。")
            continue

        # 生成息肉位置描述
        description, coverage_ratio = describe_polyp_position(image, mask)

        if description is None:
            print(f"未检测到息肉：{image_file}，跳过处理。")
            continue

        # 将结果添加到列表中
        results.append({
            "id": str(idx),
            "image": image_file,
            "description": description
        })

        print(f"已处理图片: {image_file}")

    # 将结果保存为JSON文件
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"处理完成！结果已保存到 {output_file}")


# 示例调用
image_folder = "D:\DataSet\ETIS-LaribPolypDB\images"  # 图片文件夹路径
mask_folder = "D:\DataSet\ETIS-LaribPolypDB\masks"    # mask文件夹路径
output_file = "D:\DataSet\ETIS-LaribPolypDB\ETIS-LaribPolypDB_chat.json"
process_folder(image_folder, mask_folder, output_file)