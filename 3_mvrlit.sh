# diffusionpipeline下载失败
export HF_ENDPOINT=https://hf-mirror.com

accelerate launch produce_gs_relightings.py \
      --scene_dir data/sedan \
      --image_dir_name images_4 \
      --envmap_path data/light_probes/aerodynamics_workshop.hdr \
      --downsample 2