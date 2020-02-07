## *********************************************************
##
## File autogenerated for the astra_camera package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Preferred camera stream', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'rgb_preferred', 'edit_method': "{'enum_description': 'preferred video stream mode', 'enum': [{'srcline': 29, 'description': 'RGB video stream preferred', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const bool', 'value': True, 'ctype': 'bool', 'type': 'bool', 'name': 'RGB'}, {'srcline': 30, 'description': 'IR video stream preferred', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const bool', 'value': False, 'ctype': 'bool', 'type': 'bool', 'name': 'IR'}]}", 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Video mode for IR camera', 'max': 17, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'ir_mode', 'edit_method': "{'enum_description': 'output mode', 'enum': [{'srcline': 10, 'description': '1280x1024@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_30Hz'}, {'srcline': 11, 'description': '1280x1024@15Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_15Hz'}, {'srcline': 12, 'description': '1280x720@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'XGA_30Hz'}, {'srcline': 13, 'description': '1280x720@15Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'XGA_15Hz'}, {'srcline': 14, 'description': '640x480@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'VGA_30Hz'}, {'srcline': 15, 'description': '640x480@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 6, 'ctype': 'int', 'type': 'int', 'name': 'VGA_25Hz'}, {'srcline': 16, 'description': '320x240@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 7, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_25Hz'}, {'srcline': 17, 'description': '320x240@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_30Hz'}, {'srcline': 18, 'description': '320x240@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 9, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_60Hz'}, {'srcline': 19, 'description': '160x120@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 10, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_25Hz'}, {'srcline': 20, 'description': '160x120@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 11, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_30Hz'}, {'srcline': 21, 'description': '160x120@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 12, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_60Hz'}, {'srcline': 22, 'description': '640x400@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 13, 'ctype': 'int', 'type': 'int', 'name': '640400_30Hz'}, {'srcline': 23, 'description': '320x200@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 14, 'ctype': 'int', 'type': 'int', 'name': '320200_30Hz'}, {'srcline': 24, 'description': '1280x800@7Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 15, 'ctype': 'int', 'type': 'int', 'name': '1280800_7Hz'}, {'srcline': 25, 'description': '1280x800@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': '1280800_30Hz'}, {'srcline': 26, 'description': '640x400@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 17, 'ctype': 'int', 'type': 'int', 'name': '640400_60Hz'}]}", 'default': 5, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Video mode for color camera', 'max': 17, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_mode', 'edit_method': "{'enum_description': 'output mode', 'enum': [{'srcline': 10, 'description': '1280x1024@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_30Hz'}, {'srcline': 11, 'description': '1280x1024@15Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_15Hz'}, {'srcline': 12, 'description': '1280x720@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'XGA_30Hz'}, {'srcline': 13, 'description': '1280x720@15Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'XGA_15Hz'}, {'srcline': 14, 'description': '640x480@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'VGA_30Hz'}, {'srcline': 15, 'description': '640x480@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 6, 'ctype': 'int', 'type': 'int', 'name': 'VGA_25Hz'}, {'srcline': 16, 'description': '320x240@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 7, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_25Hz'}, {'srcline': 17, 'description': '320x240@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_30Hz'}, {'srcline': 18, 'description': '320x240@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 9, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_60Hz'}, {'srcline': 19, 'description': '160x120@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 10, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_25Hz'}, {'srcline': 20, 'description': '160x120@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 11, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_30Hz'}, {'srcline': 21, 'description': '160x120@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 12, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_60Hz'}, {'srcline': 22, 'description': '640x400@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 13, 'ctype': 'int', 'type': 'int', 'name': '640400_30Hz'}, {'srcline': 23, 'description': '320x200@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 14, 'ctype': 'int', 'type': 'int', 'name': '320200_30Hz'}, {'srcline': 24, 'description': '1280x800@7Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 15, 'ctype': 'int', 'type': 'int', 'name': '1280800_7Hz'}, {'srcline': 25, 'description': '1280x800@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': '1280800_30Hz'}, {'srcline': 26, 'description': '640x400@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 17, 'ctype': 'int', 'type': 'int', 'name': '640400_60Hz'}]}", 'default': 5, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Video mode for depth camera', 'max': 17, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_mode', 'edit_method': "{'enum_description': 'output mode', 'enum': [{'srcline': 10, 'description': '1280x1024@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_30Hz'}, {'srcline': 11, 'description': '1280x1024@15Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_15Hz'}, {'srcline': 12, 'description': '1280x720@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'XGA_30Hz'}, {'srcline': 13, 'description': '1280x720@15Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'XGA_15Hz'}, {'srcline': 14, 'description': '640x480@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'VGA_30Hz'}, {'srcline': 15, 'description': '640x480@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 6, 'ctype': 'int', 'type': 'int', 'name': 'VGA_25Hz'}, {'srcline': 16, 'description': '320x240@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 7, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_25Hz'}, {'srcline': 17, 'description': '320x240@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_30Hz'}, {'srcline': 18, 'description': '320x240@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 9, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_60Hz'}, {'srcline': 19, 'description': '160x120@25Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 10, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_25Hz'}, {'srcline': 20, 'description': '160x120@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 11, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_30Hz'}, {'srcline': 21, 'description': '160x120@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 12, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_60Hz'}, {'srcline': 22, 'description': '640x400@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 13, 'ctype': 'int', 'type': 'int', 'name': '640400_30Hz'}, {'srcline': 23, 'description': '320x200@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 14, 'ctype': 'int', 'type': 'int', 'name': '320200_30Hz'}, {'srcline': 24, 'description': '1280x800@7Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 15, 'ctype': 'int', 'type': 'int', 'name': '1280800_7Hz'}, {'srcline': 25, 'description': '1280x800@30Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': '1280800_30Hz'}, {'srcline': 26, 'description': '640x400@60Hz', 'srcfile': '/home/n9646/git/ros_rc_car_tx2/src/ros_astra_camera/cfg/Astra.cfg', 'cconsttype': 'const int', 'value': 17, 'ctype': 'int', 'type': 'int', 'name': '640400_60Hz'}]}", 'default': 5, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Depth data registration', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_registration', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Synchronization of color and depth camera', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_depth_synchronization', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Auto-Exposure', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_exposure', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Auto-White-Balance', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'auto_white_balance', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Skip N images for every image published (rgb/depth/depth_registered/ir)', 'max': 10, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'data_skip', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'ir image time offset in seconds', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'ir_time_offset', 'edit_method': '', 'default': -0.033, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'color image time offset in seconds', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_time_offset', 'edit_method': '', 'default': -0.033, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'depth image time offset in seconds', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_time_offset', 'edit_method': '', 'default': -0.033, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 291, 'description': 'X offset between IR and depth images', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_ir_offset_x', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': -20.0, 'type': 'double'}, {'srcline': 291, 'description': 'Y offset between IR and depth images', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'depth_ir_offset_y', 'edit_method': '', 'default': 4.0, 'level': 0, 'min': -20.0, 'type': 'double'}, {'srcline': 291, 'description': 'Z offset in mm', 'max': 200, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'z_offset_mm', 'edit_method': '', 'default': 0, 'level': 0, 'min': -200, 'type': 'int'}, {'srcline': 291, 'description': 'Scaling factor for depth values', 'max': 1.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'z_scaling', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.5, 'type': 'double'}, {'srcline': 291, 'description': 'Use internal timer of OpenNI device', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_device_time', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Astra_SXGA_30Hz = 1
Astra_SXGA_15Hz = 2
Astra_XGA_30Hz = 3
Astra_XGA_15Hz = 4
Astra_VGA_30Hz = 5
Astra_VGA_25Hz = 6
Astra_QVGA_25Hz = 7
Astra_QVGA_30Hz = 8
Astra_QVGA_60Hz = 9
Astra_QQVGA_25Hz = 10
Astra_QQVGA_30Hz = 11
Astra_QQVGA_60Hz = 12
Astra_640400_30Hz = 13
Astra_320200_30Hz = 14
Astra_1280800_7Hz = 15
Astra_1280800_30Hz = 16
Astra_640400_60Hz = 17
Astra_RGB = True
Astra_IR = False
