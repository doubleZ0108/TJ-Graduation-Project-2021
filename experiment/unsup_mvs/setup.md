# Ubuntu Docker中进行无监督深度学习MVS

> [GitHub - tejaskhot/unsup_mvs: Code for paper: Learning Unsupervised Multi-View Stereopsis via Robust Photometric Consistency](https://github.com/tejaskhot/unsup_mvs)

## 环境配置
### 预环境安装
1. 查看Ubuntu体系架构
`uname -a`
[image:031CE4DF-85A2-43D8-83D9-BE52E56C8478-15416-000044AB49560936/23C8A44B-340B-4E98-9893-9EBEC2F1514C.png]
> 这里我的系统是x86_64架构

2. 获取CUDA 9.0, CUDNN 7.0环境
‼️这里记得换成doubleZ
`docker pull cmhi/cuda9.0-cudnn7`

3. 进入docker容器，拉取仓库
`git clone https://github.com/tejaskhot/unsup_mvs.git`

【错误：git无法安装】
执行`apt-get update`之后就可以安装git

【错误：apt-get update一直卡在 0%[Working]】
```bash
cd /usr/lib/apt/methods
ln -s http https
```

### 配置依赖环境
- opencv：可以直接参考我的另一篇文章 [[Ubuntu配置OpenCV终极解决方案]]
- python依赖：`pip install -r requirements.txt`
注意要把`requirement.txt`里这几个包的版本稍为调整如下⬇️
```
progressbar2==3.0.1
opencv-python==3.2.0.8
nvidia-ml-py==375.53
```

【pip报错：sys.stderr.write(f“ERROR: {exc}”)】
解决方案：
```bash
sudo apt-get remove python-pip
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python get-pip.py
hash -r
```

【报错：python setup.py egg_info Check the logs for full command output.】
解决方案：更新了pip之后还需要更新setuptools才能生效
```bash
sudo pip install --upgrade setuptools
```

【安装Pillow报错：ValueError: jpeg is required unless explicitly disabled using —disable-jpeg, aborting】
解决方案：执行下面的代码然后再次安装Pillow
```bash
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

【报错：ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory】
**原因**：tensorflow-gpu版本与cuda和cudnn不匹配
**解决方案**：查看 [Tensorflow GPU](https://tensorflow.google.cn/install/source_windows?hl=en#gpu) 或者 [2021最新：TensorFlow各个GPU版本CUDA和cuDNN对应版本整理(最简洁)_K1052176873的博客-CSDN博客](https://blog.csdn.net/K1052176873/article/details/114526086) 找到对应cuda和cudnn版本的tensorflow-gpu版本，并重新pip安装

> 查看CUDA版本：`nvcc -V`
> 查看cuDNN版本：
> ```bash
> whereis cudnn
> cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2
> ```
> [image:EA1AF4B4-20F6-4FFF-A5E3-3A7E0CEAEAC2-67305-00009F743FED61F2/906FA48F-701B-468C-BB54-B8D4D7737D40.png]


### 数据集下载
- DTU training data
- DTU testing data


## Training
【报错：InternalError (see above for traceback): Blas GEMM launch failed :】
显存空间不足解决方案
- [keras 或 tensorflow 调用GPU报错：Blas GEMM launch failed_Leo_Xu06的博客-CSDN博客](https://blog.csdn.net/Leo_Xu06/article/details/82023330)
- [Internal Error： Blas GEMM launch failed 问题_feixiang7701的博客-CSDN博客](https://blog.csdn.net/feixiang7701/article/details/81515447)

【报错：cuBlas call failed status = 13】
[急cuBlas call failed status = 13是什么问题？ - 知乎](https://www.zhihu.com/question/424656505)