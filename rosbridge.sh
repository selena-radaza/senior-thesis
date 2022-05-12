export ROS_IP=$(ip route get 8.8.8.8 | awk '{gsub(".*src",""); print $1; exit}')
export ROS_MASTER_URI=http://$ROS_IP:11311

roslaunch rosbridge_server rosbridge_websocket.launch address:=$ROS_IP