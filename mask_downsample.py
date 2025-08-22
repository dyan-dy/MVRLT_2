import os
from PIL import Image

# 输入路径
root_dir = "/root/autodl-tmp/LightSwitch/relighting_outputs/rm_3_3/sedan/aerodynamics_workshop"
mask_dir = "/root/autodl-tmp/LightSwitch/relighting_outputs/rm_3_3/sedan/aerodynamics_workshop/_masks"

# 创建下采样后的子目录
downsampled_dir = os.path.join(root_dir, "masks")
os.makedirs(downsampled_dir, exist_ok=True)

# 遍历文件夹中的所有图片
for filename in os.listdir(mask_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif')):
        mask_path = os.path.join(mask_dir, filename)
        
        # 打开图片
        img = Image.open(mask_path)
        
        # 计算缩小后的尺寸
        new_size = (img.width // 2, img.height // 2)
        
        # 缩小图片
        img_resized = img.resize(new_size, Image.NEAREST)  # NEAREST 保持 mask 边界
        
        # 保存到下采样目录
        save_path = os.path.join(downsampled_dir, filename)
        img_resized.save(save_path)

print(f"All masks have been downsampled by 1/2 and saved to {downsampled_dir}")
