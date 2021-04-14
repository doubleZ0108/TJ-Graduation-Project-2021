# Feature Extractioni
colmap feature_extractor \
   --database_path ./database.db \
   --image_path ./images

# Feature Matching
colmap exhaustive_matcher \
   --database_path ./database.db

# Sparse Reconstruction
mkdir sparse
colmap mapper \
    --database_path ./database.db \
    --image_path ./images \
    --output_path ./sparse

# Image Undistortion
mkdir dense
colmap image_undistorter \
    --image_path ./images \
    --input_path ./sparse/0 \
    --output_path ./dense \
    --output_type COLMAP \

# Dense Reconstruction
colmap patch_match_stereo \
    --workspace_path ./dense \
    --workspace_format COLMAP \
    --PatchMatchStereo.geom_consistency true 

# Stereo Fusion
colmap stereo_fusion \
    --workspace_path ./dense \
    --workspace_format COLMAP \
    --input_type geometric \
    --output_path ./dense/result.ply