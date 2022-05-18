#!/bin/bash
#SBATCH --array=0-3
#SBATCH -n 1
#SBATCH -c 2
#SBATCH --job-name=robustness
#SBATCH --mem=9GB
#SBATCH -t 0:60:00
#SBATCH -D /om/user/aunell/NetNoise/slurm/
#SBATCH --partition=normal
#SBATCH --gres=gpu:1
#SBATCH --constraint=any-gpu

#cd /om/user/aunell/NetNoise

hostname
echo 'this is a test'
echo $CUDA_VISIBLE_DEVICES
echo $CUDA_DEVICE_ORDER


singularity exec -B /om:/om -B /om2:/om2 -B /scratch/user/xboix:/vast --nv /om2/user/xboix/singularity/xboix-tensorflow2.5.0.simg \
python3 /om/user/aunell/NetNoise/main.py \
--experiment_type=testing \
--experiment_id=${SLURM_ARRAY_TASK_ID} \
#--filesystem=om \
#--gpu_id=0
