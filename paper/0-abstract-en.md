# ABSTRACT

**3D Reconstruction of Civil Engineering Scenes based on Unsupervised Deep Learning**


​	3D reconstruction is a key research topic in the field of computer vision and civil engineering. Efficient and high-quality reconstruction is of great significance to the digital transformation of civil engineering. The traditional civil engineering field relies on expensive and complex 3D laser scanners to achieve 3D reconstruction. But such techniques rely heavily on professional technicians and are difficult to be widely applied in large-scale civil engineering projects.

​	With the development of deep learning technology and its application in the field of computer vision, deep learning methods seem to show great potentials in the field of multi-view stereo 3D reconstruction. However, existing methods rely heavily on datasets with ground truth for training, which makes it difficult to be applied in large-scale civil engineering scenes where ground truth cannot be accurately obtained. This thesis proposes to exploit unsupervised deep learning-based methods for multi-view stereo 3D reconstruction problems, which can overcome the above challenges and obtain satisfactory results. The robust photometric consistency is used as the supervised signal, and the unsupervised deep learning method is implemented by grafting existing supervised deep learning networks.

​	The main contributions and innovation points of this thesis are as follows: ①This thesis reconstructs the unsupervised multi-view stereo 3D neural network by robust photometric consistency monitoring, and the guidance model is combined with structured similarity loss and depth map gradient smoothing loss. ②This thesis employs the top-K strategy to deal with the occlusion problem of multi-view stereo implicitly. ③This thesis compares the traditional method, supervised deep learning method, and unsupervised deep learning method qualitatively and quantitatively to explore the usability of unsupervised method in multi-view stereo 3D reconstruction.

​	Through training and testing on DTU dataset and generalized testing on Tanks and Temples dataset, it is proved that the proposed unsupervised deep learning method, which does not use scene ground truth, has a great effect on multi-view stereo 3D reconstruction problems and can be applied to 3D reconstruction problems of practical civil engineering scenes.  


**Key words**: 3D reconstruction, multi-view stereo, robust photometric consistency, unsupervised deep learning