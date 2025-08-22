# optimize a gaussian splat and verify
python gaussian-splatting/train.py -s data/${OBJ} \
      -m gs_outputs/${OBJ} \
      --images ${IMAGES} \
      --resolution 2 \
      --checkpoint_iterations 30000
python gaussian-splatting/render.py -m gs_outputs/${OBJ}

# fix the splat positions and continue optimizing only the appearance using the relit images
python gaussian-splatting/train.py -s relighting_outputs/rm_3_3/${OBJ}/${ENVMAP} \
      --start_checkpoint gs_outputs/${OBJ}/chkpnt30000.pth \
      --iterations 40000 \
      -m gs_outputs/relit_gs/${OBJ}/${ENVMAP} \
      --images ${IMAGES} \
      --position_lr_init 0.0 \
      --position_lr_final 0.0 \
      --opacity_lr 0.0 \
      --scaling_lr 0.0 \
      --rotation_lr 0.0
python gaussian-splatting/render.py -m gs_outputs/relit_gs/${OBJ}/${ENVMAP}