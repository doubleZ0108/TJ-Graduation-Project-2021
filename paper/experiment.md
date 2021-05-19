# 第五章 实验结果与评估


------

​		本章将主要介绍笔者进行的相关无监督多视点三维重建实验，包括实验环境、实验数据集等配置信息，在不同数据集上的重建效果，==消融实验==，以及对于实验的评估等内容，一些实现细节已在第4章之处，这里不在赘述。



## 5.1 实验环境与数据集简介

### 5.1.1 实验环境

​		本实验所使用的开发环境和主要依赖包参数分别如表5.1和表5.2所示。

​		需要说明的是由于本文进行多种方法的对比实验，因此通过Docker将不同方法打包成不同的镜像以互补影响，依赖包参数说明的仅为无监督学习方法的依赖环境。

表5.1 开发环境

|      类型      |    名称    |     版本 / 型号     |               说明               |
| :------------: | :--------: | :-----------------: | :------------------------------: |
|     服务器     |   Ubuntu   |     16.04.6 LTS     |          amd64体系架构           |
|      显卡      |   NVIDIA   | GeForce RTX 2080 Ti |                /                 |
|    开发语言    |   Python   |       V2.7.12       |                /                 |
|  深度学习框架  | Tensorflow |       V1.13.1       | 版本由cuda V10.0，cudnn V7.0决定 |
| 三维可视化平台 | MeshLab[4] |      V2020.12       |     开源的点云模型可视化软件     |
|      IDE       |   VSCode   |       V1.56.1       |        Python集成开发环境        |
|    容器技术    |   Docker   |      V20.10.5       |  将不同方法环境打包成独立的镜像  |
|      SFTP      | CyberDuck  |       V7.9.0        |      SFTP远程连接服务器软件      |
|    版本控制    |    Git     |       V2.24.3       |     开源的分布式版本控制工具     |

表5.2 主要依赖包参数

|      名称      |   版本   |                说明                |
| :------------: | :------: | :--------------------------------: |
| tensorflow-gpu | V1.13.1  |    Tensorflow在GPU下的依赖环境     |
|     numpy      |  V1.13   |       Python科学计算依赖环境       |
| opencv-python  | V3.2.0.8 | Python使用计算机视觉算法的依赖环境 |
|  scikit-learn  |  V0.18   |          Python机器学习库          |
|     scipy      |  V0.18   |          Python机器学习库          |
|   matplotlib   |   V1.5   |   Python绘图及数据可视化依赖环境   |
|     Pillow     |  V3.1.2  |          Python图像处理库          |
|  nvidia-ml-py  | V375.53  |       NVIDIA GPU管理依赖环境       |

### 5.1.2 实验数据集

​		本实验参照MVS相关问题的最佳实践，采用DTU数据集进行训练和测试，并在Tanks and Temples数据集上进行泛化能力测试，最后通过自采数据集验证该方法在真实实践中的可使用性。接下来笔者将分别介绍这三类数据集。

A. DTU数据集

​		DTU数据集\[1]\[2]是针对MVS问题而专门拍摄并处理的室内物体数据集，利用一个搭载可调节照明的ABB工业机械臂对物体进行多视点拍摄，如图5.1所示。所有物体拍摄的视角都经过严格控制，因此可以精准的获得每个视角下相机的内参和外参的精准值。

> 图5.1 拍摄DTU数据集所使用的ABB机械臂和拍摄环境

​		数据集中共由124个不同的物体或场景组成，如图5.2（a）所示。每个物体共拍摄49个不同的视角，每个视角共有7种不同的亮度，如图5.2（b）所示。每个物体或场景数据集中共有343张图片，每张图像分辨率为$1600 \times 1200$。

> 图5.2（a） DTU数据集中部分物体或场景
>
> 图5.2（b） DTU数据集scan34场景中的部分视角

B. Tanks and Temples数据集

​		Tanks and Temples数据集是Arno Knapitsch等人[3]提出的基准测试中所采集的大型室外场景数据集，数据的真值使用工业激光扫描仪获得，同时支持使用视频作为输入以提高重建保真度。但该数据集一般不作为训练使用，而是用于验证方法对光照变化大、存在动态目标的真实场景的泛化能力。其部分场景和视点图像如图5.3所示。

> 图5.3 Tanks and Temples数据集Family场景中的部分视角

C. 自采数据集

​		实验中还使用自采数据集进行真实实践的可用性测试，在进行自采图像收集时应注意以下四点：

（1）使用单反或专业数码相机进行数据采集，如果使用手机采集图像，要使用单摄像头手机或对其他摄像头进行遮挡后再进行采集

（2）选择纹理丰富的环境进行图像采集，尽量避免玻璃、瓷砖等强反光场景的影响

（3）选择光照充足且光照条件变换不剧烈的环境，最好选择室内环境且打开室内大灯进行灯光补偿

（4）围绕待重建物体或场景采集较多的图像，在采集过程中控制快门速度，避免模糊，如果使用视频进行抽帧操作得到图像序列，同样需要避免抽帧图像模糊

## 5.2 实验结果

### 5.2.1 DTU数据集上重建的效果



### 5.2.2 Tanks and Temples数据集上重建的泛化效果





## 5.3 消融实验





## 5.4 实验评估

### 5.4.1 实验评估方法

### 5.4.2 定型评估

### 5.4.3 定量评估

与传统Colmap方法对比

与有监督深度学习MVSNet方法对比





-----

```
[1] Rasmus Jensen, Anders Dahl, George Vogiatzis, Engin Tola, Henrik Aanaes, “Large Scale Multi-view Stereopsis Evaluation“, CVPR, 2014.
[2] Henrik Aanæs, Rasmus Jensen, George Vogiatzis, Engin Tola, Anders Dahl, “Large-Scale Data for Multiple-View Stereopsis“, International Journal of Computer Vision, 2016.

[3] Arno Knapitsch and Jaesik Park and Qian-Yi Zhou and Vladlen Koltun: Tanks and Temples: Benchmarking Large-Scale Scene Reconstruction, ACM Transactions on Graphics, 2017.

[4] Cignoni, Paolo and Callieri, Marco and Corsini, Massimiliano and Dellepiane, Matteo and Ganovelli, Fabio and Ranzuglia, Guido. MeshLab: an Open-Source Mesh Processing Tool. Eurographics Italian Chapter Conference, 2008, LocalChapterEvents:ItalChap:ItalianChapConf2008:129-136.
```

