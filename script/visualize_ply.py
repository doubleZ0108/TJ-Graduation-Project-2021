from argparse import ArgumentParser
import open3d as o3d
import numpy as np

# from https://github.com/intel-isl/Open3D/blob/master/examples/Python/Advanced/load_save_viewpoint.py
if __name__ == "__main__":
    '''
    parser = ArgumentParser()
    parser.add_argument('--dataset_name', type=str, required=True,
                        choices=['dtu', 'tanks', 'blendedmvs'],
                        help='the scan to visualize')
    parser.add_argument('--scan', type=str, required=True,
                        help='the scan to visualize')

    parser.add_argument('--use_viewpoint', default=False, action='store_true',
                        help='use precalculated viewpoint')
    parser.add_argument('--save_viewpoint', default=False, action='store_true',
                        help='save this viewpoint')

    args = parser.parse_args()
    '''
    use_viewpoints = 0
    save_viewpoint = 0
    pcd = o3d.io.read_point_cloud("./this.ply")   
    
  
    #print(f'{args.scan} contains {len(pcd.points)/1e6:.2f} M points')
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    ctr = vis.get_view_control()
    opt = vis.get_render_option()
    opt.point_size = 1.0
    opt.background_color = np.array([1,1, 1.0]) #0.5 0.5 1.0 #1, 1, 1 #0.5, 0.5, 0.5
    vis.add_geometry(pcd)
    vis.run()
    if use_viewpoints:
        param = o3d.io.read_pinhole_camera_parameters("./viewpoint/bas.json")
        ctr.convert_from_pinhole_camera_parameters(param)
        vis.run()
    if save_viewpoint:
        vis.run()
        param = ctr.convert_to_pinhole_camera_parameters()
        o3d.io.write_pinhole_camera_parameters("./viewpoint/bas.json", param)
    '''
    else:
        vis.run()
    vis.destroy_window()
    '''