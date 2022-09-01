## ROS2 Aruco package with intel realsense camera
This package integrates a USB camera with a modified version of [ros2_aruco](https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco/tree/main/ros2_aruco) in order to detect markers. 

# Requirements

`pip3 install opencv-python opencv-contrib-python`   

From the workspace directory:   
`rosdep install --from-paths src --ignore-src -r -y`

# Quick launch 

- build repository `colcon build --symlink-install`

- with realsense device connected launch `ros2 launch aruco_rs2 rs_aruco.launch.py`

- opens up rviz2, which can visualize the marker frames
