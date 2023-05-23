import subprocess

cmd = "CUDA_VISIBLE_DEVICES=0 python launch.py --config-name=mipnerf_dyn \
    dataset=zju \
    dataset.subject_id=313 \
    pos_enc=snarf \
    loss_bone_w_mult=1.0 \
    loss_bone_offset_mult=0.1"

subprocess.call(cmd, shell=True)

