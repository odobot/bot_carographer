import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        # Declare the arguments
        DeclareLaunchArgument(
            'robot_description',
            default_value='$(find bot_carographer)/urdf/bot.xacro.urdf',
            description='Path to robot URDF file'
        ),
        
        DeclareLaunchArgument(
            'configuration_directory',
            default_value='$(find bot_carographer)/configuration',
            description='Path to configuration files directory'
        ),
        
        # Load robot description and start state publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),
        
        # Start RPLIDAR sensor node which provides LaserScan data
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',
                'serial_baudrate': 115200,
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Sensitivity'
            }]
        ),
        
        # Start Google Cartographer node with custom configuration file
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            arguments=[
                '-configuration_directory', LaunchConfiguration('configuration_directory'),
                '-configuration_basename', 'bot_2d.lua'
            ]
        ),

        # Additional node which converts Cartographer map into ROS occupancy grid map
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node',
            output='screen',
            arguments=['-resolution', '0.05']
        )
    ])
