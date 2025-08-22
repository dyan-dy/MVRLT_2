export OBJ=sedan
export IMAGES=images_4
export ENVMAP=aerodynamics_workshop

echo "OBJ=$OBJ"
echo "IMAGES=$IMAGES"
echo "ENVMAP=$ENVMAP"

python gaussian-splatting/train.py -s data/${OBJ} \
      -m gs_outputs/${OBJ} \
      --images ${IMAGES} \
      --resolution 2 \
      --checkpoint_iterations 30000
python gaussian-splatting/render.py -m gs_outputs/${OBJ}