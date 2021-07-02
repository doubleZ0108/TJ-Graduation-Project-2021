# Ubuntu Docker中进行无监督深度学习MVS

* [环境配置](#环境配置)
* [Training](#training)
   * [output文件结构](#output文件结构)
* [Testing](#testing)
   * [显示ply文件](#显示ply文件)

------

> [GitHub - tejaskhot/unsup_mvs: Code for paper: Learning Unsupervised Multi-View Stereopsis via Robust Photometric Consistency](https://github.com/tejaskhot/unsup_mvs)

## 环境配置
[Ubuntu Docker中无监督深度学习MVS环境配置](https://github.com/doubleZ0108/TJ-Graduation-Project-2021/blob/master/experiment/unsup_mvs/setup.md)

## Training
【报错：InternalError (see above for traceback): Blas GEMM launch failed :】
显存空间不足解决方案
- [keras 或 tensorflow 调用GPU报错：Blas GEMM launch failed_Leo_Xu06的博客-CSDN博客](https://blog.csdn.net/Leo_Xu06/article/details/82023330)
- [Internal Error： Blas GEMM launch failed 问题_feixiang7701的博客-CSDN博客](https://blog.csdn.net/feixiang7701/article/details/81515447)

【报错：cuBlas call failed status = 13】
[急cuBlas call failed status = 13是什么问题？ - 知乎](https://www.zhihu.com/question/424656505)

### output文件结构
- `depth_map_error`
- `depth_map_gt`
- `depth_map_output`
- `photo_map_out`
- `imgs_resized`
	- `imgs_resized_0`
	- `imgs_resized_1`
	- `imgs_resized_2`
	- `imgs_resized_3`
	- `imgs_resized_4`
	- `imgs_resized_5`
	- `imgs_resized_6`
- `mask`
	- `mask_0`
	- `mask_1`
	- `mask_2`
	- `mask_3`
	- `mask_4`
	- `mask_5`
- `warped_out`
	- `warped_out_0`
	- `warped_out_1` 
	- `warped_out_2`
	- `warped_out_3` 
	- `warped_out_4`
	- `warped_out_5` 


## Testing
【报错：I tensorflow/core/platform/cpu_feature_guard.cc:141 Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA】
**原因**： CPU 支持AVX2 FMA（加速CPU计算），但安装的 TensorFlow 版本不支持
**解决办法**：
推荐直接加上这两句
```python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```
如果需要更详细的方案可以参考：[I tensorflow/core/platform/cpu_feature_guard.cc:141 Your CPU supports instructions that this Tensor_yuantao18800的博客-CSDN博客](https://blog.csdn.net/yuantao18800/article/details/101651623)


### 显示ply文件
【报错：ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22’ not found】
[ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22’ not found](https://blog.csdn.net/qq_36396104/article/details/88774797)