import cv2
import os
import glob

# 输入图片文件夹路径
img_folder = "/root/autodl-tmp/LightSwitch/data/sedan/images_4"
# 输出视频路径
output_video = "raw_data.mp4"

# 读取文件夹内所有图片，按文件名排序
img_files = sorted(glob.glob(os.path.join(img_folder, "*.jpg")))  # 或者 *.jpg

if not img_files:
    raise ValueError("❌ 没有找到图片，请检查路径和后缀名")

# 读取第一张图片，确定宽高
frame = cv2.imread(img_files[0])
h, w, _ = frame.shape

# 定义视频编码器和输出对象
fps = 15  # 帧率
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 也可以用 'XVID'
out = cv2.VideoWriter(output_video, fourcc, fps, (w, h))

# 写入所有帧
for i, file in enumerate(img_files):
    img = cv2.imread(file)
    if img is None:
        print(f"⚠️ 跳过无法读取的图片: {file}")
        continue
    img_resized = cv2.resize(img, (w, h))  # 保证所有图片大小一致
    out.write(img_resized)

out.release()
print(f"✅ 视频已保存: {output_video}")
