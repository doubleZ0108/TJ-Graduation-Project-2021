# 在Ubuntu Docker中安装Colmap

* [使用Dockerfile直接安装](#使用dockerfile直接安装)
* [在本机或在docker中一步一步安装](#在本机或在docker中一步一步安装)
* [运行Colmap的Docker镜像](#运行colmap的docker镜像)
* [Resources](#resources)

------


## 使用Dockerfile直接安装
使用Dockerfile在docker中安装Colmap之前首先要在本机上安装前置环境
[nvidia-docker安装](https://zhuanlan.zhihu.com/p/361934132)

1. 使用`nvcc —version`确认你的`cuda`版本
2. 在DockerHub上查看nvidia/cuda可用的版本 [Docker Hub Nvidia cuda](https://hub.docker.com/r/nvidia/cuda/)
	- 推荐选择devel版本
	- ubuntu系统版本推荐选择18.04，具体原因在分步安装中详述
3. 修改第一行的版本，例如我的cuda版本为11.2，第一行改写成
```docker
FROM nvidia/cuda:11.2-devel-ubuntu18.04
```
4. 然后生成镜像并等待安装即可
```bash
sudo docker build -t colmap:v0
```
> 安装过程中需要下载大量依赖，网速你懂的，推荐找寻自己合适的方式，注意一定一定要有耐心，其中很多步骤是真的很慢，之前好几次中途我以为死了就中断了，其实木有问题的！
5. 测试是否正确安装
```bash
colmap help
```
如能正确输出信息则代表colmap已经安装成功

可以使用该命令打开gui窗口，看到这个画面就完事大吉了，如果打开是全黑的窗口且命令行里报错，可能是显示的问题，可以看下面两个报错解决方案寻找灵感！！！但不影响通过cli使用！！！ （如果是远程开发，可能无法使用gui，可以直接跳过下面的问题详述）
```bash
colmap gui
```
![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210420175643.png)

【报错：
libGL error: No matching fbConfigs or visuals found  
libGL error: failed to load driver: swrast】
![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210420175656.png)
**解决方法**：https://askubuntu.com/questions/834254/steam-libgl-error-no-matching-fbconfigs-or-visuals-found-libgl-error-failed-t

1. 在主机上查看NVIDIA-SMI版本：`nvidia-smi`
![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210420175707.png)
2. 下载对应的包 `apt get install lib nvidia-gl-460`
> 我还按照论坛里删除了下`libGL.so.1`文件，不知道有没有影响
> ![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210420175721.png)
>
> ```bash
> sudo ldconfig -p | grep -i gl.so
> # 然后根据输出信息的提示删除这个文件
> sudo rm /usr/lib/x86_64-linux-gnu/libGL.so.1
> ```


【报错：QOpenGLWidget: Failed to create context】
**解决方案**：
按照这个issue[Help - QOpenGLWidget: failed to create context · Issue #749 · colmap/colmap · GitHub](https://github.com/colmap/colmap/issues/749)还是没有解决
![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210420175730.png)
```bash
apt-get install qt5-default
export QT_SELECTION=path/to/qmake
```
后来查到另一个issue https://github.com/colmap/colmap/issues/884 说是X-Display的问题，推荐还是使用命令行模式，也可能是因为我在docker中起的GUI，可能会产生莫名其妙的问题
最后安装了`nvidia-drivers`得以解
**安装步骤简要介绍如下**：
在docker容器中安装
```bash
sudo apt-get install ubuntu-drivers-common
sudo ubuntu-drivers autoinstall
```
在宿主机上
```bash
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```
然后在启动docker images中加入`--gpus all`参数



## 在本机或在docker中一步一步安装
1. 安装依赖项
```bash
apt-get update && apt-get install -y \
    git \
    cmake \
    build-essential \
    vim
```
```bash
apt-get update && apt-get install -y \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-regex-dev \
    libboost-system-dev \
    libboost-test-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev
```
```bash
apt-get update && apt-get install -y \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev \
    libcgal-qt5-dev
```
2. 编译安装`ceres-solver`
```bash
apt-get update && apt-get install -y libatlas-base-dev libsuitesparse-dev
git clone https://gitee.com/coolke/ceres-solver.git
git checkout $(git describe --tags)
cd ceres-solver
mkdir build && cd build
cmake .. -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF		# 这步会卡特别长时间，要有耐心～
make -j4 && make install
```
ubuntu系统版本要注意⚠️ 我最开始选择的是16.04，在安装`ceres-solver`过程中一直【卡死：— Detected Ceres being used as a git submodule, adding commit hook for Gerrit to: /ceres-solver/.git】，网上的问题少之又少，花了三个多小时反复安装还是一直卡死；后来将ubuntu版本更换成18.04后在这步卡了十几分钟之后成功编译。但这里也可能是幸存者偏差问题了，酌情参考
3. 编译安装colmap
```bash
git clone https://github.com/colmap/colmap.git
git checkout dev
mkdir build && cd build
cmake ..
make -j2		# 这步同样会卡特别特别特别长时间，一定要有充足的耐心和勇气！！ 学长说是线程开的太多，用到swap进行处理，一点一点搬运太慢，推荐直接不要开多线程
make install
```
4. 测试是否正确安装
```bash
colmap help
```

## 运行Colmap的Docker镜像
最终运行有Colmap的Docker镜像的指令如下（吐槽下配置的参数是真的多，踩的坑是真滴真滴太多太多了）
```bash
xhost +

sudo docker run -itd \
  -p 6789:22 \
  -v /etc/localtime:/etc/localtime:ro \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=unix$DISPLAY \
  -e GDK_SCALE \
  -e GDK_DPI_SCALE \
  --ipc=host \
  --privileged=true \
  --gpus all \
  colmap:v0 \
  /bin/bash
```
- `-v -e`：让docker使用本机的显示，以运行GUI窗口
- `--ipc=host`: 为了增加主机和容器共享内存，如果报错，可以用`—shm-size 5120m \`代替
- `--privileged=true`：在本机上开放特殊权限


**注**：由于国内安装依赖的网速，我将教程中的安装换了源
- 原始链接
	- https://ceres-solver.googlesource.com/ceres-solver
	- https://github.com/colmap/colmap.git
- 更换后的链接
	- https://gitee.com/coolke/ceres-solver.git
	- https://gitee.com/liang-hao/colmap.git
> 每当这个时候就会由衷感谢Gitee


## Resources
* https://colmap.github.io/install.html
*  [GitHub - Kai-46/colmap_in_docker: install colmap in a docker](https://github.com/Kai-46/colmap_in_docker)
* [三维重建_COLMAP安装、使用和参数说明（翻译自官方文档）_一步一脚印-CSDN博客](https://blog.csdn.net/X_kh_2001/article/details/82591978)
* http://www.ceres-solver.org/installation.html#linux
还有一些环境报错的解决方案
- [【Docker】在docker中安装显卡驱动、CUDA、CUDNN等_奔跑的战神-CSDN博客_docker安装nvidia驱动](https://blog.csdn.net/qq_33547243/article/details/107433616)
- [初探Docker调用GPU - 知乎](https://zhuanlan.zhihu.com/p/109477627)