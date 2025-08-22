export OBJ=sedan
export IMAGES=images_4
export ENVMAP=aerodynamics_workshop

# bash scripts/download_preprocess.sh
python scripts/generate_masks.py --image_dir data/sedan/images_4 --initial_prompt 400 400 800 400 1000 300