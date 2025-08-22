import numpy as np
import cv2
from scipy.spatial.transform import Rotation as R

# 假设你已有训练好的 Gaussian 3D 表示，并有函数 render_gaussians(camera)
# camera = {'position': np.array([x, y, z]), 'rotation': R instance}

def slerp(rot1, rot2, t):
    """四元数插值"""
    return R.slerp([0, 1], [rot1, rot2])([t])[0]

def interpolate_camera(cam_start, cam_end, num_frames):
    positions = np.linspace(cam_start['position'], cam_end['position'], num_frames)
    rotations = []
    for i in range(num_frames):
        t = i / (num_frames - 1)
        rotations.append(slerp(cam_start['rotation'], cam_end['rotation'], t))
    cameras = [{'position': pos, 'rotation': rot} for pos, rot in zip(positions, rotations)]
    return cameras

# 定义关键相机
cam0 = {'position': np.array([0, 0, 0]), 'rotation': R.from_euler('xyz', [0, 0, 0], degrees=True)}
cam1 = {'position': np.array([1, 0, 0]), 'rotation': R.from_euler('xyz', [0, 30, 0], degrees=True)}

# 插值生成连续相机列表
num_frames = 60
camera_list = interpolate_camera(cam0, cam1, num_frames)

# 渲染每帧
frame_list = []
for i, cam in enumerate(camera_list):
    # 这里用你的 Gaussian 渲染函数替代
    frame = render_gaussians(cam)  # frame 应该是 np.array(H, W, 3), dtype=np.uint8
    frame_list.append(frame)
    print(f"Rendered frame {i+1}/{num_frames}")

# 保存视频
height, width, _ = frame_list[0].shape
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
for frame in frame_list:
    out.write(frame)
out.release()
print("Video saved as output.mp4")
