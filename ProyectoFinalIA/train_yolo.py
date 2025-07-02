import torch
from yolov5 import train

# Puedes usar train.run() o train.main(), depende de la versión.
train.run(
    imgsz=224,             # Tamaño de imagen
    batch=16,              # Batch size
    epochs=50,             # Número de epochs
    data='ProyectoFinalIA/dataset/data.yaml',  # Ruta a tu archivo de configuración
    weights='yolov5s.pt'   # Pesos preentrenados de inicio
)
