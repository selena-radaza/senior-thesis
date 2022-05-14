using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class UserElbow : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject lower_right_arm;
        public Vector3 position;
        public Quaternion rotation;
        private Quaternion yumi_home_coordinates = new Quaternion(0.0332f, -0.554673f, 0.721133f, -0.413763f);

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            position = GetPosition(message).Ros2Unity();
            rotation = GetRotation(message).Ros2Unity();


        }


        // Start is called before the first frame update
        protected override void Start()
        {
            lower_right_arm.gameObject.transform.localPosition
                 = GameObject.FindGameObjectWithTag("low_arm_r").transform.localPosition;

            /*lower_right_arm.gameObject.transform.localRotation
                = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation * Quaternion.Inverse(yumi_home_coordinates);

            rotation = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation * Quaternion.Inverse(yumi_home_coordinates);*/

            lower_right_arm.gameObject.transform.localRotation
                = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation;

            rotation = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation;

            base.Start();
        }

        // Update is called once per frame
        private void Update()
        {
            //lower_right_arm.transform.localPosition = position;
            lower_right_arm.transform.localRotation = rotation;
        }

        private Vector3 GetPosition(MessageTypes.Geometry.Pose message)
        {
            return new Vector3(
                (float)message.position.x,
                (float)message.position.z,
                (float)message.position.y);
        }

        private Quaternion GetRotation(MessageTypes.Geometry.Pose message)
        {
            Quaternion cur = new Quaternion(
                -(float)message.orientation.z,
                (float)message.orientation.y,
                -(float)message.orientation.x,
                (float)message.orientation.w);


            // Quaternion rotate_y = Quaternion.Euler(90, 0, 90);
            // return cur * rotate_y;
            return cur;

        }
    }
}


