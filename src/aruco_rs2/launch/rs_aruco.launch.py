import argparse
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

import os
import sys
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    parser = argparse.ArgumentParser(description='aruco_rs2')
    parser.add_argument('-n', '--node-name', dest='node_name', type=str,
                        help='name for device', default='usb_camera')

    args, unknown = parser.parse_known_args(sys.argv[4:])
    node_name = args.node_name
    ns = "/usb_camera"

    aruco_rs2_dir = get_package_share_directory('aruco_rs2')

    params_aruco_node = os.path.join(
        aruco_rs2_dir,
        'config',
        'aruco_node.yaml'
        )

    params_aruco_rs2 = os.path.join(
        aruco_rs2_dir,
        'config',
        'camera_params.yaml'
    )

    return LaunchDescription([
        Node(
            package="ros2_aruco",
            executable="aruco_node",
            output="screen",
            parameters = [params_aruco_node],
        ),
        Node(
            package="usb_cam",
            executable="usb_cam_node_exe",
            output="screen",
            name=node_name,
            namespace = ns,
            parameters=[params_aruco_rs2],
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=['-d' + os.path.join(aruco_rs2_dir, 'config', 'rviz.rviz')],
            output="screen"
        ),
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["1","0","0","0","0","0","world","usb_camera_link"],
            output="screen"
        ),
    ])