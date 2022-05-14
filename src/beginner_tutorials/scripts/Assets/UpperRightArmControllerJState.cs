/*
© Siemens AG, 2017-2018
Author: Dr. Martin Bischoff (martin.bischoff@siemens.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
<http://www.apache.org/licenses/LICENSE-2.0>.
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Added allocation free alternatives
// UoK , 2019, Odysseas Doumas (od79@kent.ac.uk / odydoum@gmail.com)

using UnityEngine;
using System.Collections.Generic;
using RosSharp.RosBridgeClient.MessageTypes.Sensor;
using System;

namespace RosSharp.RosBridgeClient
{
    public class UpperRightArmControllerJState : UnitySubscriber<MessageTypes.Sensor.JointState>
    {
        //public Transform PublishedTransform;
        //public string FrameId = "Unity";
        //public JointStateSubscriber jsSub;

        public List<string> JointNames;
        public List<JointStateWriter> JointStateWriters;
        public MessageTypes.Geometry.PoseStamped poseMessage;
        public Transform PublishedTransform;
        GameObject shoulder;

        protected override void ReceiveMessage(JointState message)
        {
            int index;
            for (int i = 0; i < message.name.Length; i++)
            {
                index = JointNames.IndexOf(message.name[i]);
                if (index != -1)
                {
                    JointStateWriters[index].Write((float)message.position[i]);
                    //Go from radians to degrees
                    double deg = message.position[i] * (180 / 3.1415926535);
                    float degFloat = Convert.ToSingle(deg);
                    poseMessage.header.Update();

                    Vector3 posePos = GameObject.FindGameObjectWithTag("up_arm_r").transform.localPosition;
                    Quaternion poseRot = new Quaternion(degFloat, 0, 0, 1);
                    Pose p = new Pose(posePos, poseRot);

                    //GetGeometryPoint(PublishedTransform.position.Unity2Ros(), message.position[i]);

                }
                    
            }

            
        }

        private static void GetGeometryPoint(Vector3 position, MessageTypes.Geometry.Point geometryPoint)
        {
            geometryPoint.x = position.x;
            geometryPoint.y = position.y;
            geometryPoint.z = position.z;
        }

        private static void GetGeometryQuaternion(Quaternion quaternion, MessageTypes.Geometry.Quaternion geometryQuaternion)
        {
            geometryQuaternion.x = quaternion.x;
            geometryQuaternion.y = quaternion.y;
            geometryQuaternion.z = quaternion.z;
            geometryQuaternion.w = quaternion.w;
        }
    }
}
