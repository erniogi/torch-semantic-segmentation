# torch-semantic-segmentation

This is a Pytorch implementation of Semantic Segmentation
 
This repository includes:
* Training and Evaluation Codes
* Streamlit Semantic Segmentation Application

**Streamlit Semantic Segmentation Application** 
 
<insert image>

## Instlation
1. Install Docker 
 * FYI : See [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/). 

2. Install torch-classifier 
```bash
git clone https://https://github.com/erniogi/torch-semantic-segmentation.git
```
 
3. Build Docker image 
```bash
cd torch-semantic-segmentation/docker
sh build.sh

```
4. Run Docker Container
```bash
sh run.sh
```
 
5. Exec Docker Container

```bash
docker exec -it intern_khoshi_semantic_segmentation bash
```

6. Setup
```bash
python3 setup.py
```

