using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class LowerLeftArmController : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject lower_left_arm;
        public Vector3 position;
        public Quaternion rotation;

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            position = GetPosition(message).Ros2Unity();
            rotation = GetRotation(message).Ros2Unity();
            Debug.Log("Rotation When Received: " + rotation);


        }


        // Start is called before the first frame update
        protected override void Start()
        {
            lower_left_arm.gameObject.transform.localPosition
                = GameObject.FindGameObjectWithTag("low_arm_l").transform.localPosition;

            position = GameObject.FindGameObjectWithTag("low_arm_l").transform.localPosition;

            lower_left_arm.gameObject.transform.localRotation
                = GameObject.FindGameObjectWithTag("low_arm_l").transform.localRotation;

            rotation = GameObject.FindGameObjectWithTag("low_arm_l").transform.localRotation;

            base.Start();
        }

        // Update is called once per frame
        private void Update()
        {
            lower_left_arm.transform.localPosition = position;
            lower_left_arm.transform.localRotation = rotation;
            Debug.Log("Rotation After Updated: " + rotation);
            Debug.Log("Position After Updated: " + position);
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


