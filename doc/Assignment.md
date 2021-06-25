# 任务书

* [课题背景](#课题背景)
* [技术参数（研究内容）](#技术参数研究内容)
* [应完成的具体工作](#应完成的具体工作)
* [进度安排](#进度安排)
* [应收集的资料及主要参考文献](#应收集的资料及主要参考文献)

------

## 课题背景

建筑信息模型（Building Information Modeling，BIM）是土木工程领域最常用的工程数据模型之一，在开放的IFC工业标准下对设施的物理和功能特性及其相关的项目全寿命周期信息进行可计算、可运算的形式表现，对决策支持提供了极大的便利，有效地支撑土木行业各个应用系统之间的数据交换和建筑物全过程的数据管理。
传统的BIM建模方式是专业建筑设计工程师正向建模，近几年开始出现基于三维激光扫描的BIM逆向建模技术，但任然面临成本高、专业技术人员少等问题。而基于多视点立体匹配（Multi-view stereo, MVS）和深度估计的三维重建算法在近些年里成为点云重建的热门研究方向，本文提出一种基于多视点三维重建逆向生成BIM模型的方法。
基于无监督学习的方法具有以下优点：
1）无需预先采集构建一个大规模数据集，节省人力物力
2）泛化性好，可以较为方便的从单中心物体三维重建扩展到建筑室内的三维重建
3）可以有针对性的对土木工程施工场景进行约束和设计
而对于多视点问题，采用多台内参一样的相机同时拍摄待重建物体显然成本比较大，运用起来也较为复杂，因此采用视频抽帧的方式同时进行多视点的模拟。传统视频抽帧图像序列仅通过计算机视觉算法进行相机标定和位姿估计，场景变化较大、光线和特征缺失等情况都会对使用造成影响。本课题希望融合运动惯性测量单元（Inertial Measurement Unit，IMU）和稀疏视觉特征进行相机内参标定和位姿估计，同时提取“关键帧”进行多视点三维重建，惯性补偿技术可以跟踪由物体运动惯性引起的视频序列在时域上的相关性，可使得重建效果更平滑。
本课题将从RGB视频融合IMU数据出发，通过稀疏视觉特征和惯性侧脸单元进行相机内参标定和位姿估计，抽帧进行传统基于视觉的COLMAP和无监督深度学习多视点三维重建，最终将其转换为BIM模型。

## 技术参数（研究内容）
1. 工作流程概述
	本次毕业设计主要研究多视点立体匹配算法在土木工程施工场景下的三维重建和BIM逆向生成问题，即通过对视频进行抽帧得到的多视点图片序列进行深度估计、三维点云生成和三维模型重建，得到高质量的点云模型和网格化模型，并转化为BIM模型。本次毕业设计主要分为以下四部分工作：
	1）融合多视点和惯性imu单元数据进行视频抽帧及相机标定和姿态估计
	2）多视点三维点云生成算法实现和比较
	a. 使用Colmap算法生成三维点云
	b. 设计无监督深度神经网络进行多视点立体匹配
	3）对点云进行曲面重建
	4）将曲面模型转换为BIM模型

2. 具体工作内容
	1）使用RGB相机和imu惯性测量单元融合采集视频，并进行抽帧和相机标定、位姿估计
	考虑使用intel RealSense L515深度相机作为数据采集设备，关闭深度雷达数据流而只使用其RGB+imu数据流。
	2）基于纯视觉的多视点三维重建COLMAP算法
	主要包括：稀疏重建、深度图估计和稠密重建三个步骤
	3）基于无监督深度学习的三维重建算法
	相较于有监督MVS算法，不依赖于真实的3D数据，利用多个视图之间的光度一致性并加入了像素提督差异作为监督信号，来预测深度图
	4）点云重建算法
	使用MeshLab、PCL等常用工具进行点云重建，常用算法有柏松重建、Delaunay三角剖分
	5）BIM模型生成
	通过导入点云数据模型（rcp）至revit（rvt）软件中分析项目的特征且查阅点云数据的完整性，制作可视化BIM模型


## 应完成的具体工作
1. 调研课题背景
	1. 了解多视点和惯性imu单元融合相关技术
	2. 了解深度估计相关技术
	3. 了解三维点云重建相关技术
	4. 了解BIM在土木工程施工中的应用
2. 完成算法和应用系统的详细设计
	1. 设计多视点和惯性imu单元的融合方案
	2. 设计多视点深度估计的实现方法
	3. 设计三维点云重建算法的技术细节
	4. 设计三维模型到BIM模型的转换流程和方案
3. 采集数据进行实验，并根据效果调整算法
	1. 环绕拍摄待重建物体视频并使用多视点和惯性imu单元进行抽帧和相机位姿估计
	2. 使用传统视觉的方法Colmap重建点云
	3. 使用无监督深度学习MVS方法在官方数据集上测试
	4. 使用无监督深度学习MVS方法在自建数据集上进行训练
	5. 使用PCL库对点云进行曲面重建
	6. 使用土木工程领域相关方法将模型转换为BIM模型
4. 撰写毕业设计论文
大致分为以下几个部分：
一、目录
二、摘要
三、选题的背景和研究意义
四、土木工程施工场景三维重建研究现状
	1）国内现状
	2）国外现状
	3）三维重建技术研究现状
	4）BIM逆向建模技术研究现状
五、关键技术与核心算法
	1）多视点和惯性imu单元进行抽帧和相机位姿估计算法
	2）传统视觉Colmap算法
	3）无监督深度学习MVS算法
	4）PCL库点云重建与滤波算法
	5）三维模型转换为BIM模型方法
六、实验结果与比较
七、改进与优化
八、讨论与分析
	1）今后土木工程施工场景三维重建技术的应用
	2）今后BIM逆向建模技术的发展可能性
九、总结

## 进度安排
**序号**		**设计(论文)各个阶段名称**	**时间安排(教学周)**
1	与导师沟通，确认研究项目、项目可行性和研究方案	第1周
2	查阅文献和资料，联系所学知识了解项目背景和需求	第1～2周
3	分析任务书，完成开题报告	第2周
4	实现基于多视点和运动惯性测量的关键帧提取算法和相机标定、姿态估计算法 第3～4周
5	实现多视点深度估计和立体匹配算法	 第5～7周
6	实现三维点云重建算法和优化		第8～9周
7	实现单一结构构件和模拟施工空间的三维重建及BIM模型生成	第10～11周
8	整合上述步骤的核心算法进行集成测试	第12周
9	整理并撰写论文	 第13～14周
10	论文答辩	第15～16周

## 应收集的资料及主要参考文献
[1]Khot T, Agrawal S, Tulsiani S, et al. Learning unsupervised multi-view stereopsis via robust photometric consistency[J]. arXiv preprint arXiv:1905.02706, 2019.
[2]Schonberger J L, Frahm J M. Structure-from-motion revisited[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 4104-4113.
[3]Schönberger J L, Zheng E, Frahm J M, et al. Pixelwise view selection for unstructured multi-view stereo[C]//European Conference on Computer Vision. Springer, Cham, 2016: 501-518.
[4]Yao Y, Luo Z, Li S, et al. Mvsnet: Depth inference for unstructured multi-view stereo[C]//Proceedings of the European Conference on Computer Vision (ECCV). 2018: 767-783.
[5]Qin T, Shen S. Online temporal calibration for monocular visual-inertial systems[C]//2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2018: 3662-3669.
[6]Qin T, Li P, Shen S. Vins-mono: A robust and versatile monocular visual-inertial state estimator[J]. IEEE Transactions on Robotics, 2018, 34(4): 1004-1020.
[7]刘莎莎. 点云数据与BIM集成的建筑物施工进度监测技术方法[D].西南交通大学,2019.
[8]郑华海,刘匀,李元齐.BIM技术研究与应用现状[J].结构工程师,2015,31(04):233-241.
[9]Asadi K, Han K. Real-time image-to-BIM registration using perspective alignment for automated construction monitoring[C]//Construction Research Congress. 2018, 2018: 388-397.
[10]Banfi F, Stanga C, Brumana R. A Digital Workflow for Built Heritage: From SCAN-to-BIM Process to the VR-Tour of the Basilica of Sant’Ambrogio in Milan[C]//Euro-Mediterranean Conference. Springer, Cham, 2018: 334-343.

