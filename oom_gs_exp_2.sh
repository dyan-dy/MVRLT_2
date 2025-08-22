export OBJ=sedan
export IMAGES=images_4
export ENVMAP=aerodynamics_workshop

echo "OBJ=$OBJ"
echo "IMAGES=$IMAGES"
echo "ENVMAP=$ENVMAP"

# --start_checkpoint gs_outputs/${OBJ}/chkpnt30000.pth \
python gaussian-splatting/train.py -s relighting_outputs/rm_3_3/${OBJ}/${ENVMAP} \
      --iterations 40000 \
      --start_checkpoint gs_outputs/${OBJ}/chkpnt30000.pth \
      -m gs_outputs/relit_gs_dino/${OBJ}/${ENVMAP} \
      --images ${IMAGES} \
      --position_lr_init 0.0 \
      --position_lr_final 0.0 \
      --opacity_lr 0.0 \
      --scaling_lr 0.0 \
      --rotation_lr 0.0 \
      --disable_viewer
python gaussian-splatting/render.py -m gs_outputs/relit_gs_dino/${OBJ}/${ENVMAP}