using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class UserShoulder : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject upper_right_arm;
        public Vector3 position;
        public Quaternion rotation;
        private Quaternion yumi_home_rotation2 = new Quaternion(-0.236319f, -0.0463f, -0.868148f, 0.432317f);
        private Quaternion yumi_home_rotation1 = new Quaternion(.271905f, -0.4372f, 0.699496f, -0.49561f);

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            //position = GetPosition(message).Ros2Unity();
            rotation = GetRotation(message).Ros2Unity();
            position = GetPosition(message).Ros2Unity();
            //Debug.Log("Rotation When Received: " + rotation);


        }


        // Start is called before the first frame update
        protected override void Start()

        {
            //upper_right_arm.gameObject.transform.position
            //    = position;

            upper_right_arm.gameObject.transform.localPosition
                = GameObject.FindGameObjectWithTag("up_arm_r").transform.localPosition;

            //position = GameObject.FindGameObjectWithTag("up_arm_r").transform.localPosition;

            //upper_right_arm.gameObject.transform.localRotation
            //  = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation * Quaternion.Inverse(yumi_home_rotation2) * Quaternion.Inverse(yumi_home_rotation1);

            //rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation * Quaternion.Inverse(yumi_home_rotation2) * Quaternion.Inverse(yumi_home_rotation1);

            upper_right_arm.gameObject.transform.localRotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.rotation;

            rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;

            base.Start();
        }

        // Update is called once per frame
        private void Update()
        {
            //upper_right_arm.transform.position = position;
            upper_right_arm.transform.rotation = rotation;
            //Debug.Log("Joint 2: " + rotation);
            //Debug.Log("Rotation After Updated: " + rotation);
            //Debug.Log("Position After Updated: " + position);
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
            // -y, z, x
            // 






            //xyz:  Rotations are happening around the y position
            Quaternion cur = new Quaternion(
                -(float)message.orientation.z,
                (float)message.orientation.y,
                -(float)message.orientation.x,
                (float)message.orientation.w);

            /*Quaternion cur = new Quaternion(
                (float)message.orientation.x,
                (float)message.orientation.y,
                (float)message.orientation.z,
                (float)message.orientation.w);*/



            return cur;

            // Rotate 180 around "y" to make arm face the right way
            //return cur * RotateAroundAxis(0f, 1f, 0f, 180f);
            /*Quaternion cur = new Quaternion(
                (float)message.orientation.x,
                (float)message.orientation.y,
                (float)message.orientation.z,
                (float)message.orientation.w);

            // Rotate around z 90 degrees (counter clockwise)
            Quaternion z_rotate = cur * RotateAroundAxis(0, 0, 1, -90);

            // Rotate around y 90 degrees (counter clockwise)

            Quaternion y_rotate = z_rotate * RotateAroundAxis(1, 0, 0, -90);

            // Negate z and return?
            return new Quaternion(y_rotate.x, y_rotate.z, y_rotate.y, y_rotate.w);
*/
            // Possibly try
            // Rotate around x 90
            // swap x and z axes
            /*Quaternion cur = new Quaternion(
                (float)message.orientation.x,
                (float)message.orientation.y,
                (float)message.orientation.z,
                (float)message.orientation.w);

            // Rotate around x 90 degrees
            Quaternion x_rotate = cur * RotateAroundAxis(1, 0, 0, 90);

            return new Quaternion(x_rotate.z, x_rotate.y, x_rotate.x, x_rotate.w);*/
        }
    }
}


