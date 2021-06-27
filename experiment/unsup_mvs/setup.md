# Ubuntu Docker中无监督深度学习MVS环境配置

* [预环境安装](#预环境安装)
* [配置依赖环境](#配置依赖环境)
* [数据集下载](#数据集下载)
* [测试是否配置成功](#测试是否配置成功)

------

> [GitHub - tejaskhot/unsup_mvs: Code for paper: Learning Unsupervised Multi-View Stereopsis via Robust Photometric Consistency](https://github.com/tejaskhot/unsup_mvs)

## 预环境安装
1. 查看Ubuntu体系架构
`uname -a`

![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210430214551.png)

> 这里我的系统是x86_64架构

2. 获取CUDA, CUDNN docker环境
原repo中推荐的版本是CUDA9.0，CUDNN7.0
但是训练时GeForce RTX 2080Ti使用CUDA9.0的时候会报错，推荐使用CUDA10.0（如果是1080Ti使用原始推荐版本即可）
> 查看GPU型号：`lspci | grep -i nvidia`

在[DockerHub](https://hub.docker.com)中查找相应体系架构和版本的docker预环境，并安装

![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210430214604.png)

```bash
sudo docker pull cmhi/cuda9.0-cudnn7
```

3. 安装nvidia-docker，让docker中可以使用GPU：[[nvidia-docker安装]]
4. 启动docker
```bash
sudo docker run -it \
  --ipc=host \
  --privileged=true \
  --gpus all \
  unsup_mvs:v0 \
  /bin/bash
```

> 直接在dockerhub中pull的镜像推荐重新命名：
> `sudo docker tag f7d5 unsup_mvs:v0`
> 然后删除之前id对应的镜像
> `sudo docker rmi -f f7d5`

5. 下载仓库
`git clone https://github.com/tejaskhot/unsup_mvs.git`

【错误：git无法安装】
执行`apt-get update`之后就可以安装git

【错误：apt-get update一直卡在 0%[Working]】
```bash
cd /usr/lib/apt/methods
ln -s http https
```

---

## 配置依赖环境
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

‼️特别要注意tensorflow-gpu的版本
【报错：ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory】
**原因**：tensorflow-gpu版本与cuda和cudnn不匹配
**解决方案**：查看 [Tensorflow GPU](https://tensorflow.google.cn/install/source_windows?hl=en#gpu) 或者 [2021最新：TensorFlow各个GPU版本CUDA和cuDNN对应版本整理(最简洁)_K1052176873的博客-CSDN博客](https://blog.csdn.net/K1052176873/article/details/114526086) 找到对应cuda和cudnn版本的tensorflow-gpu版本，并重新pip安装

> 查看CUDA版本：`nvcc -V`
> 查看cuDNN版本：
> ```bash
> whereis cudnn
> cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2
> ```

![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210430214617.png)


## 数据集下载
- [DTU training data](https://drive.google.com/file/d/1eDjh-_bxKKnEuz5h-HXS7EDJn59clx6V/view)
- [DTU testing data](https://drive.google.com/file/d/135oKPefcPTsdtLRzoDAQtPpHuoIrpRI_/view)
> training data有19个G emmmmm，在google drive里是真的太顶了

下载完之后将两个解压的文件夹放到根目录`data/`目录下，目录结构如下：
```
.
|-- mvs_testing
|   `-- dtu
|       |-- scan1
|       |-- scan10
|       |-- scan11
|       |-- scan110
|       |-- scan114
|       |-- scan118
|       |-- scan12
|       |-- scan13
|       |-- scan15
|       |-- scan23
|       |-- scan24
|       |-- scan29
|       |-- scan32
|       |-- scan33
|       |-- scan34
|       |-- scan4
|       |-- scan48
|       |-- scan49
|       |-- scan62
|       |-- scan75
|       |-- scan77
|       `-- scan9
`-- mvs_training
    `-- dtu
        |-- Cameras
        |-- Depths
        `-- Rectified
```

## 测试是否配置成功
在项目根目录创建`checkpoint`文件夹，然后进入`code/unsup_mvs`目录，并执行训练
```bash
python train_dtu.py --dtu_data_root ../../data/mvs_training/dtu/ --save_dir ../../checkpoint/
```
如果能正确执行并输出训练过程则环境配置成功🎉