
# 摘要

基于无监督学习的土木工程场景三维重建

3D Reconstruction  of Civil Engineering Scenes based on Unsupervised Deep Learning


**关键词**：三维重建，多视点，鲁棒光度一致性，无监督深度学习

**Key words**: 3D reconstruction, multi-view stereo, robust photometric consistency, unsupervised deep learning


三维重建是计算机视觉和土木工程领域的重点研究课题，高效、高质量的重建对土木工程数字化转型具有重要意义。传统的土木工程领域依靠昂贵且复杂的三维激光扫描仪实现三维重建，但该技术严重依赖专业技术人员，在大体量的土木工程项目中极难普遍的适用。
随着深度学习技术的发展和其在计算机视觉领域的应用，深度学习方法在多视点三维重建领域似乎展现出了巨大的可能，然而现有方法强烈依赖有真值的数据集进行训练，导致在无法精确获取真值的土木工程大规模场景中难以适用。本文针对上述问题进行无监督学习多视点三维重建方法改进，利用鲁棒的光度一致性作为监督信号，嫁接现有深度学习网络进行无监督深度学习方法尝试。
本文的主要创新点有：①本文通过鲁棒的光度一致性构建无监督多视点三维重建神经网络，并结合结构化相似性损失和深度图梯度感知平滑损失指导模型；②本文通过top-K策略隐式处理多视点图像间的遮挡问题；③本文将传统方法、有监督学习方法、无监督学习方法进行定性和定量的对比实验，探究无监督方法在多视点三维重建上的可用性。
通过在DTU数据集上进行训练和测试，以及在Tanks and Temples数据集上进行泛化测试，证实本文中没有使用场景真值的无监督学习方法在多视点三维重建问题上取得了很好的效果，可以应用到土木工程场景三维重建问题上。




3D reconstruction is a key research topic in the field of computer vision and civil engineering. Efficient and high-quality reconstruction is of great significance to the digital transformation of civil engineering. The traditional civil engineering field relies on expensive and complex 3D laser scanners to achieve 3D reconstruction. But the technology relies heavily on professional technicians and is extremely difficult to be universally applied in large-scale civil engineering projects.
With the development of deep learning technology and its application in the field of computer vision, deep learning methods seem to show great possibilities in the field of multi-view stereo 3D reconstruction. However, the existing methods rely heavily on datasets with ground truth for training, which makes it difficult to apply in large-scale civil engineering scenes where ground truth cannot be accurately obtained. This thesis improved the unsupervised deep learning multi-view stereo 3D reconstruction method to solve the above problems. The robust photometric consistency was used as the supervised signal, and the unsupervised deep learning method is implemented by grafting existing supervised deep learning networks.
The main contributions and innovation points of this thesis are as follows: ①This thesis reconstruct the unsupervised multi-view stereo 3D neural network by robust photometric consistency monitoring, and the guidance model is combined with structured similarity loss and depth map gradient smoothing loss. ②This thesis used top-K strategy to deal with the occlusion problem of multi-view stereo implicitly. ③This thesis compared the traditional method, supervised deep learning method, and unsupervised deep learning method qualitatively and quantitatively to explore the usability of unsupervised method in multi-view stereo 3D reconstruction.
Through training and testing on DTU dataset and generalization testing on Tanks and Temples dataset, it is proved that the unsupervised deep learning method, which does not use scene ground truth, has a great effect on multi-view stereo 3D reconstruction problems and can be applied to 3D reconstruction problems of civil engineering scenes.


