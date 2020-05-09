import os
import logging
import shrub
import tflite2onnx as t2o

shrub.util.formatLogging(logging.DEBUG)


OP_LIST = (
        # 'abs.float32',
        # 'softmax.float32',
        # 'add.float32',
        # 'transpose.float32',
        'avgpooling.float32',
        # 'conv.float32',
        )


def test_ops():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    tflm_dir = os.path.abspath(cur_dir + '/../assets/tests')
    for op in OP_LIST:
        tflm_name = op + '.tflite'
        tflm_path = os.path.join(tflm_dir, tflm_name)
        t2o.convert(tflm_path, op + '.onnx')

        m = shrub.tflite.parse(tflm_path)
        m.genInput()

        onnx_ret = shrub.onnx.run(op + '.onnx', m.inputs)
        tflite_ret = shrub.tflite.run(tflm_path, m.inputs)
        assert(shrub.network.cmpTensors(onnx_ret, tflite_ret))


if __name__ == '__main__':
    test_ops()
