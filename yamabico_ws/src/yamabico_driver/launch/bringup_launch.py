import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    driver_dir = get_package_share_directory('yamabico_driver')
    driver_param = os.path.join(driver_dir, 'config', 'driver_node.param.yaml')
    ypspur_coordinator_path = os.path.join(driver_dir, 'scripts', 'ypspur_coordinator_bridge')

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'robot_param',
            description='Path to robot .param file for ypspur-coordinator',
        ),
        launch.actions.LogInfo(msg='Launching ypspur-coordinator...'),
        launch.actions.ExecuteProcess(
            cmd=[ypspur_coordinator_path,
                 launch.substitutions.LaunchConfiguration('robot_param')],
            output='screen',
        ),
        launch.actions.LogInfo(msg='Launching yamabico_driver node...'),
        Node(
            package='yamabico_driver',
            executable='yamabico_driver',
            output='screen',
            parameters=[driver_param],
        ),
    ])
