"""URG (北陽電機 LiDAR) を起動する launch ファイル.

serial_port は実機に合わせて変更すること（ls /dev/serial/by-id/ で確認）。
/scan トピックに sensor_msgs/LaserScan が配信される。
"""
import launch
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='urg_node',
            executable='urg_node_driver',
            name='urg_node',
            output='screen',
            parameters=[{
                # 実機の by-id パスに合わせて変更する
                'serial_port': '/dev/serial/by-id/usb-Hokuyo_Data_Flex_for_USB_URG-Series_USB_Driver-if00',
                'frame_id': 'laser',
                'angle_min': -2.356194,   # -135 deg
                'angle_max': 2.356194,    #  135 deg
            }],
        ),
        # base_footprint → laser の静的 TF（URG の取り付け位置に合わせて調整）
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_laser',
            arguments=['0', '0', '0.1', '0', '0', '0', 'base_footprint', 'laser'],
        ),
    ])
