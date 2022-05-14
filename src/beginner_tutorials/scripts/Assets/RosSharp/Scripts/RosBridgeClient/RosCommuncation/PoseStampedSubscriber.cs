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

using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class PoseStampedSubscriber : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        //public Transform PublishedTransform;

        public Vector3 position;
        public Quaternion rotation;
        public bool isMessageReceived;
        public GameObject lower_arm;
        public GameObject right_arm;

        protected override void Start()
        {
			base.Start();
		}
		
        private void Update()
        {
            if (isMessageReceived)
                ProcessMessage();
        }

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            position = GetPosition(message).Ros2Unity();
            Debug.Log("Position: " + position);

            lower_arm.transform.localPosition = position;

            //var behaviors = arm.GetComponents<MonoBehaviour>(); // Issue is somewhere here
            //var script = behaviors[0] as NewBehaviourScript;
            //script.position.Set(position.x, position.y, position.z);
            //position = new Vector3(0, 0, 0);
         
            //arm.transform.position = GameObject.FindGameObjectWithTag("up_arm_r").transform.position;

            //rotation = GetRotation(message).Ros2Unity();
            //arm.transform.rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.rotation;
            //isMessageReceived = true;
        }

        private void ProcessMessage()
        {
            //arm.transform.position = position + new Vector3(0.1f, 0.1f, 0.1f);
            //arm.transform.rotation = rotation;
        }

        private Vector3 GetPosition(MessageTypes.Geometry.Pose message)
        {
            return new Vector3(
                (float)message.position.x,
                (float)message.position.y,
                (float)message.position.z);
        }

        private Quaternion GetRotation(MessageTypes.Geometry.Pose message)
        {
            return new Quaternion(
                (float)message.orientation.x,
                (float)message.orientation.y,
                (float)message.orientation.z,
                (float)message.orientation.w);
        }
    }
}