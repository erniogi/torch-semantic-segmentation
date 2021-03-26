#!/bin/sh
docker run \
  -dit \
  --gpus '"device=1"' \
  -v ~/torch-semantic-segmentation:/workspace \
  -p 8501:8501 \
  --name intern_khoshi_semantic_segmentation\
  --rm \
  --shm-size=256m \
  intern_khoshi_segmentation:latest
