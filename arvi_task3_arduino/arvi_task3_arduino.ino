//#define USE_USBCON
#include <ros.h>
 

#include <std_msgs/String.h>

ros::NodeHandle  nh;



void command_cb( const std_msgs::String & cmd_msg){
  if(cmd_msg.data=="ON"){
    pinMode(7,HIGH);  
  }else if(cmd_msg.data=="OFF"){
    pinMode(7,LOW);  
  }
}


ros::Subscriber<std_msgs::String> sub("command", command_cb);

void setup(){
  pinMode(7, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  
}

void loop(){
  nh.spinOnce();
  delay(1);
}
