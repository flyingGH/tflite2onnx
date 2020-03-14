import logging
from abc import ABC

class BaseABC(ABC):
    """Holding objects of TFLite and ONNX"""
    name = "Unintialized"
    tflite = None
    onnx = None


logger = logging.getLogger('tflite2onnx')
