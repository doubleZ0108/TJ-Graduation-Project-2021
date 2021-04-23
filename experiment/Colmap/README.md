# 传统方法Colmap进行三维重建实践（GUI｜命令行）

Colmap算法**pipeline**：
[image:09909703-ADA7-42F0-91C0-1446F9791DE5-56719-0001067DAC376629/62F04787-5D3D-4638-AF5A-862CE30B48B4.png]


## Colmap安装
[[在Ubuntu Docker中安装Colmap]]

---
## 数据采集
[[多视角三维重建(MVS)的数据采集]]
---

## Colmap GUI操作
### 稀疏重建
采用增量SfM技术
> 其中SfM技术出自[GitHub - openMVG/openMVG: open Multiple View Geometry library. Basis for 3D computer vision and Structure from Motion.](https://github.com/openMVG/openMVG)

#### 1. 准备工作
1. 创建工程目录`TestScan`
2. 在其中创建`images`目录并存放原始图像
3. 运行`colmap gui`，点击`file - New Project`弹出Project窗口
4. `在Database`行点击`New`，在`TestScan`目录中创建`TestScan.db`文件用于存储原始图片地址、特征匹配等数据
5. 在`Images`行点击`Select`选择场景原始图片所在目录
6. 最后点击`save`
初始的目录结构为：
```
.
|-- TestScan.db
`-- images
    |-- 00000000.jpg
    |-- 00000001.jpg
    |-- ...
    `-- 00000048.jpg
```

#### 2. 特征提取
此步骤进行对应点搜索，可以理解为全局特征匹配
点击`processing - Feature Extraction`
- 选择相机模型为`Pinhole`
- 选择`Parameters from EXIF`：从EXIF中提取相机内参（一般采集到的影响都携带EXIF文件）
- 其他参数暂且默认
然后点击`Extract`进行特征提取
[image:67D5D609-8FF0-4712-83B0-94F823E54EDD-804-00002C9A741A4CE9/2021-04-06_10-35.png]

#### 3. 特征匹配
点击`processing - Feature Matching`，参数全部选用默认，然后点击`Run`进行特征匹配

这个步骤结束之后会自动生成**场景图**和**匹配矩阵**（以不同视图之间同名特征数为权重，以不同视图为图节点的图结构）

> 从右侧的`Log`中可以看到这两步的输出[image:3D59CA63-98EF-4233-A958-4013F8BE3D8E-804-00002C981608174B/2021-04-06_10-39.png]

#### 4. 增量式建模
点击`reconstruction - start reconstruction`进行一键式增量迭代重建

此步骤逐渐增加视角，并进行迭代优化重投影误差
目的是计算不同视图的相机参数、得到场景的稀疏点云和确定不同视图与点云间的可视关系
最后可以得到场景的**稀疏点云**和各个视角的**相机姿态**
[image:6EFB7775-C10B-45C5-9067-E47E3157C4B4-804-00002D0A6B404230/2021-04-06_10-49.png]

以第49张图像（39个视角）为例
- 已有点云576个
- 首先进行姿态估计（Pose Refinement Report）
- 再进行BA优化：整体稀疏点云融合测量点149个，滤除测量点32个
- 再进行三角测量（Retriangulation）
- 最后再进行迭代全局的BA优化，优化已有相机的姿态和三维稀疏点云坐标
```
==============================================================================
Registering image #39 (49)
==============================================================================

  => Image sees 576 / 991 points

Pose refinement report
----------------------
    Residuals : 1132
   Parameters : 8
   Iterations : 7
         Time : 0.0134351 [s]
 Initial cost : 0.535158 [px]
   Final cost : 0.462099 [px]
  Termination : Convergence

  => Continued observations: 540
  => Added observations: 73

Bundle adjustment report
------------------------
    Residuals : 24684
   Parameters : 2030
   Iterations : 21
         Time : 0.501096 [s]
 Initial cost : 0.374389 [px]
   Final cost : 0.367663 [px]
  Termination : Convergence

  => Merged observations: 149
  => Completed observations: 27
  => Filtered observations: 32
  => Changed observations: 0.016853

Bundle adjustment report
------------------------
    Residuals : 24690
   Parameters : 2000
   Iterations : 3
         Time : 0.0764892 [s]
 Initial cost : 0.430376 [px]
   Final cost : 0.427614 [px]
  Termination : Convergence

  => Merged observations: 10
  => Completed observations: 1
  => Filtered observations: 0
  => Changed observations: 0.000891

==============================================================================
Retriangulation
==============================================================================

  => Completed observations: 9
  => Merged observations: 186
  => Retriangulated observations: 0
```

---
### 深度图估计与优化
Colmap中代价构造、累积、估计和优化是封装在一起的，利用GEM模型进行求解
**主要分为四个步骤**：匹配代价构造 -> 代价累积 -> 深度估计 -> 深度图估计
> 这里的原理暂时省略，[多视图几何三维重建实战系列之COLMAP](https://mp.weixin.qq.com/s?__biz=MzU1MjY4MTA1MQ==&mid=2247511777&idx=2&sn=73ab994649ba559d9628d1fc4dcfda5a&chksm=fbfc85d5cc8b0cc3d89f4ce189cc0cad185fcd7519193e8951833884a2c26b3f1eadfc84d098&scene=178&cur_album_id=1433700656199860224#rd)

#### 1. 图像去畸变
点击`reconstruction - dense reconstruction`，在稠密重建窗口中点击`select`选择文件存放位置，然后点击`undistortion`即可去除图像畸变
> ⚠️注意：这里不要选择项目的根目录，拷贝图片的时候会报错路径已存在导致colmap gui闪退的；同时undistortion也只能点一次，第二次同样会因为路径已存在闪退

==[image:AFD1E7A3-1533-4A96-A37C-EFE4672D40BD-804-00008ACC9698B4DE/2021-04-09_10-40.png]==

带有畸变的图像会导致边缘有较大的时差估计误差，因此在深度图估计之前，使用光学一致性和几何一致性联合约束构造代价匹配
> dtu数据集和之前配置成针孔模型已经隐含无畸变
> 如果使用自采集数据集需要更改相机模型为带畸变参数的相机模型

#### 2. 深度估计
在稠密重建窗口中点击`stereo`进行场景深度估计
深度估计结束后可以得到`photometric`和`geometric`下的深度图和法向量图
> 这一步很慢而且资源消耗比较大
[image:FD8125BC-401D-4935-B7F9-8D0A32024913-804-00008D0EF3AAA6F3/2021-04-09_11-15.png]
之后点击红框里的这些就可以观察光学一致性photometric和几何一致性geometric后的depth map和normal map

[image:51562502-0B3B-4CA8-A509-3E893C1A2FC9-804-00008D5484C61606/1476DCB5-C004-4BB2-8700-CD79B42F135E.png]

Colmap会利用光学一致性同时估计视角的深度值和法向量值，并利用几何一致性进行深度图优化

---
### 稠密重建
点击`Fusion`即可进行基于深度图融合的稠密重建
[image:D632FD09-66C9-4117-B1E0-5557B22A3AAB-804-0000423990237907/2021-04-06_17-18_1.png]

重建后会在`dense`中生成`ply`模型文件
可以安装[MeshLab](https://www.meshlab.net)进行显示
```bash
sudo snap install meshlab
```

【报错：meshlab无法打开ply文件】
==[image:D8ED2166-032D-4293-B0F8-99064AFF94BB-804-0000387D0EE5F32B/2021-04-06_14-18.png]==

**问题分析**：用文本浏览器打开ply文件发现header之后全部问乱码
==[image:96D93079-D496-4FD4-AB12-D03A70D70C00-804-00003856E8A37CCA/BFCA8075-4921-4811-99A0-2830B2F44D28.png]==
找了很多资料还是没有找到解决方案，最后找师兄要了一个显示ply的python脚本，主要是用的是open3d库就成功了😭，这个故事告诉我们 听老师和师兄的一句建议就可以节省一整个下午debug的时间
脚本放在github上，暂未开源，如果有需求可以留言哈～

或者采用Colmap GUI官方的可视化方法，点击`File - Import model from...`，选择生成的`fused.ply`即可打开查看融合后的点云效果；不过`meshed-poisson.ply`无法打开，还是要使用Meshlab
==[image:57EA76FC-971A-4C40-BF56-7AB6C552FE67-804-000042399057F6D7/2021-04-06_17-18.png]==

### 中间数据分析 —— 匹配矩阵
点击`Extras - Match Matrix`可以导出当前场景的匹配矩阵
[image:D302915D-8399-4C7B-B412-D75B412E9EAA-804-000094330DA608BF/8278ADD8-0E5E-4C6F-8FC1-6E34825BEA12.png]

从中可以看到改组图像中相机的运动规律。如果相机围绕物体圆周采样，则匹配矩阵则会出现条带，各个条带平行关系越强，相机的运动控制越严格

> 看了些其他人的比较图和结论，采集数据集的前期控制对重现效果有影响


---
## Colmap命令行操作
准备好带有`images`图像目录的文件

1. **特征提取**
```bash
colmap feature_extractor \
   --database_path ./database.db \
   --image_path ./images
```
**输出**：database.db中保存特征点
2. **特征点匹配**
```bash
colmap exhaustive_matcher \
   --database_path ./database.db
```
3. **稀疏重建**
```bash
mkdir sparse
colmap mapper \
    --database_path ./database.db \
    --image_path ./images \
    --output_path ./sparse
```
**输出**：`sparse`文件夹，目录结构如下：
```
└── sparse
    └── 0
        ├── cameras.bin        # 相机内参
        ├── images.bin         # 相机位姿
        ├── points3D.bin       # 稀疏3D点
        └── project.ini
```
4. **图像去畸变**
```bash
mkdir dense
colmap image_undistorter \
    --image_path ./images \
    --input_path ./sparse/0 \
    --output_path ./dense \
    --output_type COLMAP \
```
**输出**：`dense`文件夹，目录结构如下：
```
└── dense
    ├── images
    │   ├── 0.JPG
    │   ├── ...
    │   └── 48.JPG
    ├── run-colmap-geometric.sh
    ├── run-colmap-photometric.sh
    ├── sparse
    │   ├── cameras.bin
    │   ├── images.bin
    │   └── points3D.bin
    └── stereo
        ├── consistency_graphs
        ├── depth_maps
        ├── fusion.cfg
        ├── normal_maps
        └── patch-match.cfg
```
5. **稠密重建**
```bash
colmap patch_match_stereo \
    --workspace_path ./dense \
    --workspace_format COLMAP \
    --PatchMatchStereo.geom_consistency true    
```
**输出**：`dense/stereo`文件夹，为每张图像估计`depth_map`和`normal_map`
```
└── dense
    ├── images
    │   ├── 0.JPG
    │   ├── ...
    │   └── 48.JPG
    ├── run-colmap-geometric.sh
    ├── run-colmap-photometric.sh
    ├── sparse
    │   ├── cameras.bin
    │   ├── images.bin
    │   └── points3D.bin
    └── stereo
        ├── consistency_graphs
        ├── depth_maps
        │   ├── 0.JPG.geometric.bin
        │   ├── 0.JPG.photometric.bin
        │   ├── ...
        │   ├── ...
        │   ├── 48.JPG.geometric.bin
        │   └── 48.JPG.photometric.bin
		├── fusion.cfg
        ├── normal_maps
        │   ├── 0.JPG.geometric.bin
        │   ├── 0.JPG.photometric.bin
        │   ├── ...
        │   ├── ...
        │   ├── 48.JPG.geometric.bin
        │   └── 48.JPG.photometric.bin
        └── patch-match.cfg
```
6. **融合**
```bash
./colmap stereo_fusion \
    --workspace_path ./dense \
    --workspace_format COLMAP \
    --input_type geometric \
    --output_path ./dense/result.ply
```
**输出**：`result.ply`点云模型文件

## Resources
* [多视图几何三维重建实战系列之COLMAP](https://mp.weixin.qq.com/s?__biz=MzU1MjY4MTA1MQ==&mid=2247511777&idx=2&sn=73ab994649ba559d9628d1fc4dcfda5a&chksm=fbfc85d5cc8b0cc3d89f4ce189cc0cad185fcd7519193e8951833884a2c26b3f1eadfc84d098&scene=178&cur_album_id=1433700656199860224#rd)
* [三维重建_COLMAP安装、使用和参数说明（翻译自官方文档）_一步一脚印-CSDN博客](https://blog.csdn.net/X_kh_2001/article/details/82591978)
* [三维重建：colmap安装与使用 - 学而时嘻之HUST - 博客园](https://www.cnblogs.com/Todd-Qi/p/10792685.html)·