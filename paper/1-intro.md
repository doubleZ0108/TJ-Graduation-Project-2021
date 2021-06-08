# 第一章 引言

## 1.1 研究背景及意义
### 1.1.1 土木工程场景三维重建的研究背景与价值

随着数字化进程在土木工程领域的推进，各类土木工程场景的数字模型在设计、仿真、施工、验收等多生命周期越来越多地发挥重要作用。尤其是建筑结构信息（Building Information Modeling，简称BIM）在开放的IFC土木工程工业标准下，对建筑的物理特性、功能特征以及项目的全生命周期进行可建模、可运算的表达，高效地支撑土木工程领域各系统和模块间的数据交互以及建筑全过程的数据管理[1]。
然而，由于自然条件限制、工时紧等因素，在建筑真实施工时，不可避免地要对建筑设计时的图纸和数字模型等进行调整，因此，在建筑建成后，真实建筑的数字孪生模型与设计阶段的BIM模型存在出入[2]。另一方面，传统的BIM建模是通过专业建筑设计工程师在专用建模软件，如Rivit中进行的正向建模，BIM模型的准确性和精度不仅高度依赖于建模工程师的经验等主观能力，更十分受限于建筑图纸的规范性和完整性，对于图纸残缺的建筑，正向建模很难保证BIM建模的准确性；对于大量无从获得精确图纸的古建筑，面临年代久远、资料档案缺失等诸多问题，常规的BIM建模方式也难以适用[3]。
三维重建技术可以很好的解决上述问题，重建得到稠密的高精度点云模型，通过三维模型转换软件，如GeoSLAM、PointCab等，可以便捷高效的转换为BIM模型。因此三维重建技术作为土木工程领域的重点和热门研究课题：高效、便捷、高精度的三维重建方法对BIM技术的反推动作用及土木工程领域的数字化转型有着极为重要的研究和应用价值。


### 1.1.2 无监督深度学习在该领域的应用价值

土木工程领域传统的三维重建方法主要通过三维激光扫描技术[4]实现，三维激光扫描仪发射和接受高能量的激光束，通过飞行时间和光速算得距离，进而获取场景物体表面的三维坐标点值和纹理信息等，然后融合时间序列生成点云。该方法已成功在一些真实的大型工程项目中得到应用，如上海世茂深坑酒店方案优化项目[5]、武汉绿地中心钢结构项目[6]等。但该技术严重依赖专业技术人员，且高昂的扫描成本让很多项目无法采用，尤其在大体量的土木工程项目中极难得到普遍的适用。
立体匹配、深度估计和三维重建算法也是计算机领域一直以来的研究课题，从单目、双目深度估计到多视点三维重建技术在近几年随着深度学习技术的兴起也有很多新的探索。如能依照计算机领域相关算法，通过计算机视觉、图像处理、深度学习等方法对土木工程场景进行三维重建大大节约成本且可不断进行算法迭代创新优化以适应新需求。
近几年，随着香港科技大学权龙教授实验室提出的基于深度学习的多视点立体匹配算法MVSNet[7]的成功，越来越多的基于深度学习的多视点三维重建算法研究成果发表。但由于它们高度依赖已标定数据集的真值，在土木工程大型场景极难获取准确且完整的三维信息真值的大背景下，基于有监督的深度学习方法较难发挥出强大的优势。如能将有监督的多视点三维重建网络进行迁移，通过不需要获取数据集真值的无监督深度学习方法进行算法研究和实践，在土木工程场景三维重建问题中有着极为重要的意义。这不仅可以最大程度的利用现有标准数据集、网络架构、最佳实践等，更能通过施工工地采集得到的大量原始数据进行更加精准场景的训练，并使算法保持良好的泛化能力。

## 1.2 研究现状

多视点三维重建相关领域的主要方法包括基于计算机视觉和摄影几何的传统方法、一系列启发式传播策略方法，以及近几年提出的基于深度学习的深度估计和三维重建方法。对比情况如表1.1所示。

> table 1.1

基于计算机视觉的传统方法一般集成从运动中恢复结构（Structure from Motion，简称SfM）和多视点立体匹配（Multi-View Stereo，简称MVS），从一组不同视角下拍摄的有序或无序图像集合中同时恢复相机位姿和场景三维结构。主要包括多视点数据集采集、稀疏重建、深度图估计和稠密重建四个核心步骤。最具代表性的是北卡罗来纳大学教堂山分校和苏黎世联邦工业大学提出的Colmap[8][9]方法，该方法代码封装性良好，并提供GUI可分步观察重建流程，可快速用于三维重建实践，但由于采用传统算法，在深度图估计上耗时较长。
近几年，随着卷积神经网络（Convolutional Neural Networks，简称CNNs）等深度学习方法的兴起，使得很多复杂的传统问题有了新的求解途径，而基于深度学习的三维重建算法无疑是深度学习在计算机视觉领域的一次十分成功的应用。直觉上，人脑同样是基于非严格的几何特征观察场景中的深度信息并对物体进行“三维重建”的，极端情况，对于单张图像而言，虽然已经完全丢失深度信息，但人脑仍然可以凭借经验进行深度维度的大致估计，而深度学习方法正适用于此非严格数学逻辑问题的求解。
Han等人[10]首先提出可以使用深度神经网络的方法进行两个图像块的匹配；Zbontar[11]和Luo等人[12]使用基于深度学习得到的图像特征进行立体匹配，并使用半全局匹配（Semi-Global Matching，简称SGM）方法进行后处理，取得了很好的成果。后续的深度学习工作进一步充分利用神经网络的特性：GCNet[13]使用3D CNNs对代价体进行正则化，并且使用soft argmin进行误差回归；SurfaceNet[14]构建有色体元结构（Colored Voxel Cubes，简称CVC），将所有像素值和相机参数融合成单一的代价体作为网络的输入；LSM[15]利用可微投影变换进行端到端的训练和推理，均取得了一定的成果。但上述方法大都通过标准3D网格进行空间表达估计图像中每个像素是否附着在3D网格表面，这使得深度神经网络很难扩展，同时由于巨大的内存消耗，网络很难被加速。
2018年，香港科技大学权龙教授实验室提出的MVSNet，将相机参数编码为可微单应变换，并融合图像信息构建代价体，同时嫁接了2D特征提取和3D损失回归的有监督深度学习神经网络，在DTU数据集上取得了惊人的结果，并且在Tanks and Temples数据集榜单上取得了第一名的成绩。从此开启了有监督深度学习MVS的大繁荣：RMVSNet[16]通过基于区域的卷积神经网络（Region-based Convolutional Neural Networks，简称R-CNN）降低3D卷积消耗；PointMVSNet[17]直接将目标场景作为点云处理，并通过多阶段的方式预测深度；Cascade[18]采用缩小范围的深度值多阶段推断法。但上述方法极大地依赖于数据集的真值，无法使用大量获取的无精准深度的训练数据。
无监督深度学习方面，C.Godard等人[19]和Y. Kuznietsov等人[20]提出的基于无监督深度学习的单目深度估计方法利用光度一致性作为损失函数进行训练，但他们的方法非常依赖帧之间的视觉变换信息，因此在有遮挡和光照变化较大的场景表现效果较差，究其关键，还是在光度一致性损失上不够鲁棒。


## 1.3 挑战与目标

本节将分析三维重建领域现有方法的不足，以及面对土木工程场景实际情况的三维重建技术面临的挑战，然后据此引出本文的主要研究内容。

### 1.3.1 土木工程场景三维建模面临的问题和挑战

根据1.2节对多视点三维重建领域现有方法，尤其是基于深度学习方法的简述，土木工程三维场景三维建模领域面临的主要问题和挑战包含如下两方面：
A.	土木工程场景数据集真值难以获取
目前在三维重建问题中，基于深度学习的方法能够取得精度最高、完整度最好的重建效果，但目前较为成熟的深度学习方法都为有监督方法，极大地依赖有真值的数据集，且容易受到数据集中内容的影响。现有的数据集主要集中在光照高度可控的小规模室内场景，虽然也有一部分具有真值的室外场景数据集，但数据在采集过程中就存在一定程度的偏差，对于模型的训练会造成比较大的影响。而对于土木工程这类大规模场景，无论是使用三维激光扫描仪还是其他高精度设备都很难高效、准确、大量的获取场景的真值，标准土木工程场景大型数据集更无从谈起。
B.	基于无监督深度学习中光度一致性损失不够鲁棒
现有基于无监督深度学习三维重建方法主要应用在单目视图或双目视图中，在这类问题中原始输入图像不会在光照上存在比较大的差异，且不必考虑遮挡问题的影响。但在多视点三维重建问题中，由于输入是一系列图像序列，某一视图中的像素很可能在其他视图中因遮挡关系而不可见，且在相隔较远的帧之间很可能会存在比较大的光照差异，不鲁棒的光度一致性损失在多视点三维重建中同样无法达到鲁棒的效果。

	

### 1.3.2 本文研究内容

针对土木工程场景数据集真值难以获取及光照和遮挡等影响的问题，本文总结前人在无监督多视点重建上的工作，进一步完善并说明基于鲁棒的光度一致性损失的无监督多视点三维重建方法，最终应用于土木工程场景的三维重建中。
本文的研究内容主要包含以下三个方面：
A.	基于无监督学习的多视点三维重建方法
无监督学习的方法不需要依赖具有真值的数据集，能够较好的克服土木工程场景数据集真值难以获取的问题。同时有监督学习方法中的数据集也可以方便的使用于无监督的训练中，且成熟的有监督学习网络架构也可以对无监督学习网络架构起到较多的指导作用。因此，本文将对有监督学习网络进行适当调整，针对无监督学习说明一种损失函数计算方法。并将三维重建问题进行解耦，转换为通过一组新视点图像对参考图像深度图的预测问题，最后通过深度图融合，生成场景的稠密点云。
B.	鲁棒的光度一致性损失
由于无监督方法没有数据集真值作为学习依照，因此良好高效的损失函数是无监督网络的关键。本文通过总结前人在光度一致性方面的探索，进一步完善并说明一种鲁棒的光度一致性损失计算方法。
C.	将传统方法、有监督方法、无监督方法进行对比实验
笔者选取基于计算机视觉的传统方法Colmap、基于有监督的深度学习网络MVSNet，以及本文中基于鲁棒光度一致性的无监督学习网络，分析每种方法的原理、流程和实现，并依次配置环境进行三种算法重建效果的对比实验。
本文的研究思路如图1.1所示，笔者首先进行无监督多视点三维重建方法的探索，并与传统计算机视觉方法和有监督深度学习多视点三维重建方法进行对比实验，最终在土木工程场景上进行三维重建。


## 1.4 论文结构安排
第1章 引言：首先介绍了土木工程场景三维重建的课题研究背景与研究意义，并明确了无监督深度学习在该领域的应用价值，然后描述了相关领域的研究现状，最后阐述了本文研究内容面临的问题与挑战。
第2章 理论基础：主要介绍三维重建的基础知识，包括对极几何、单应变换、平面扫描、立体匹配等，并简要介绍卷积神经网络和无监督深度学习等深度学习方法的基础知识。
第3章 多视点三维重建：主要围绕传统计算机视觉方法Colmap和有监督学习MVSNet方法，详细介绍三维重建的架构与算法。
第4章 无监督深度学习算法实现：主要介绍笔者对本文基于无监督深度学习多视点三维重建的方法，尤其是鲁棒的光学一致性、无监督损失函数和深度学习网络架构等方面。
第5章 实验结果与评估：主要介绍笔者进行实验的环境配置与数据集，并在DTU数据集和Tanks and Temples数据集上进行方法结果测试，同时进行消融实验和与其他方法的对比实验，总结评估笔者本文中方法的效果。
第6章 总结与展望：总结本文所做工作，并通过分析不足提出一些展望，明确未来研究方向。


-----
```
[1]	刘占省,赵明,徐瑞龙. BIM技术在建筑设计、项目施工及管理中的应用[J].建筑技术开发,2013,40(3):65-71. 
[2]	张冰,李欣,万欣欣.从数字孪生到数字工程建模仿真迈入新时代[J].系统仿真学报,2019,31(03):369-376.
[3]	石力文,侯妙乐,胡云岗,李爱群,解琳琳.基于点云数据与BIM的古建筑三维信息表达方法研究[J].遗产与保护研究,2018,3(07):46-52.
[4]	缪盾,吴竞,张广兴.BIM结合三维激光扫描在建筑中的应用[J].低温建筑技术,2017,39(05):133-134+143.
[5]	李小飞,李赟,张林,王硕,钱海波.基于三维激光扫描的BIM技术在上海世茂深坑酒店方案优化中的应用[J].施工技术,2015,44(19):30-33.
[6]	姚习红,徐晓雨,高志民.基于三维激光扫描的BIM技术在武汉绿地中心钢结构项目中的应用[J].钢结构,2018,33(08):118-121.
[7]	Yao Y, Luo Z, Li S, et al. Mvsnet: Depth inference for unstructured multi-view stereo: Proceedings of the European Conference on Computer Vision[C], 2018: 767-783.
[8]	Schonberger J L, Frahm J M. Structure-from-motion revisited: Proceedings of the IEEE conference on computer vision and pattern recognition[C], 2016: 4104-4113.
[9]	Schönberger J L, Zheng E, Frahm J M, et al. Pixelwise view selection for unstructured multi-view stereo: European Conference on Computer Vision. Springer[C], Cham, 2016: 501-518.
[10]	Han X, Leung T, Jia Y, et al. Matchnet: Unifying feature and metric learning for patch-based matching: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition[C], 2015: 3279-3286.
[11]	Zbontar J, LeCun Y. Stereo matching by training a convolutional neural network to compare image patches[J]. J. Mach. Learn. Res., 2016, 17(1): 2287-2318.
[12]	Luo W, Schwing A G, Urtasun R. Efficient deep learning for stereo matching: Proceedings of the IEEE conference on computer vision and pattern recognition[C], 2016: 5695-5703.
[13]	Kendall A, Martirosyan H, Dasgupta S, et al. End-to-end learning of geometry and context for deep stereo regression: Proceedings of the IEEE International Conference on Computer Vision[C], 2017: 66-75.
[14]	Ji M, Gall J, Zheng H, et al. Surfacenet: An end-to-end 3d neural network for multiview stereopsis: Proceedings of the IEEE International Conference on Computer Vision[C], 2017: 2307-2315.
[15]	Kar A, Häne C, Malik J. Learning a multi-view stereo machine[J]. arXiv preprint arXiv:1708.05375, 2017.
[16]	Yao Y, Luo Z, Li S, et al. Recurrent mvsnet for high-resolution multi-view stereo depth inference: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition[C], 2019: 5525-5534.
[17]	Chen R, Han S, Xu J. Visibility-aware point-based multi-view stereo network[J]. IEEE transactions on pattern analysis and machine intelligence, 2020.
[18]	Gu X, Fan Z, Zhu S, et al. Cascade cost volume for high-resolution multi-view stereo and stereo matching: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition[C], 2020: 2495-2504.
[19]	Godard C, Mac Aodha O, Brostow G J. Unsupervised monocular depth estimation with left-right consistency: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition[C], 2017: 270-279.
[20]	Kuznietsov Y, Stuckler J, Leibe B. Semi-supervised deep learning for monocular depth map prediction: Proceedings of the IEEE conference on computer vision and pattern recognition[C], 2017: 6647-6655.
```