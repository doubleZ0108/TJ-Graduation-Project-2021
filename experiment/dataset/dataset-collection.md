# 多视角三维重建(MVS)的数据采集

* [开源数据集](#开源数据集)
* [自采数据集](#自采数据集)
* [Resources](#resources)

------

## 开源数据集
1. **DTU数据集**：针对MVS而专门拍摄并处理的室内数据集
	利用一个搭载可调节亮度灯的工业机器臂对一个物体进行多视角的拍摄，每个物体所拍的视角都经过严格控制，所以可以获取每个视角的相机内、外参数。
	**数据集组成**：124个不同的物体或场景，每个物体共拍摄49个视角，每个视角共有7种不同的亮度。每个物体或场景文件夹内部共有343个图片。每张影像的分辨率为1600×1200。（该数据集还包含带有深度图真值的训练影像集，可用于训练神经网络）
	![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210427225417.png)
	![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210427225424.png)

[MVS Data Set – 2014 | DTU Robot Image Data Sets](http://roboimagedata.compute.dtu.dk/?page_id=36)

2. **Tanks and Temples数据集**：室外场景数据集
主要用于验证我们使用的网型和开源软件泛化能力，验证其是否对光照变化大、存在动态目标的场景仍具备较为精确地重建能力
![](https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210427225433.png)


## 自采数据集
* 尽量使用单反相机或专业数码相机进行数据采集，如果要用手机进行采集，请使用单摄像头的手机进行数据采集。
* 尽量选择纹理丰富的外界环境进行数据采集，避免玻璃围墙、瓷砖和打蜡地板等强反光材料环境
* 尽量选择光照明亮，且光照条件变化不剧烈的环境，最好选择室内环境。如室内客厅，开启客厅大灯进行灯光补偿。
* 尽量围绕重建物体或环境采集较多的影像，且在采集过程中控制快门速度，避免模糊。

## Resources
[多视图几何三维重建实战系列之COLMAP](https://mp.weixin.qq.com/s?__biz=MzU1MjY4MTA1MQ==&mid=2247511777&idx=2&sn=73ab994649ba559d9628d1fc4dcfda5a&chksm=fbfc85d5cc8b0cc3d89f4ce189cc0cad185fcd7519193e8951833884a2c26b3f1eadfc84d098&scene=178&cur_album_id=1433700656199860224#rd)