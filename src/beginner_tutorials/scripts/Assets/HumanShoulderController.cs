using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class HumanShoulderController : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject upper_right_arm;
        public Vector3 position;
        public Quaternion rotation;
        private Quaternion yumi_home_rotation2 = new Quaternion(-0.236319f, -0.0463f, -0.868148f, 0.432317f);
        private Quaternion yumi_home_rotation1 = new Quaternion(.271905f, -0.4372f, 0.699496f, -0.49561f);

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            rotation = GetRotation(message).Ros2Unity();

        }


        // Start is called before the first frame update
        protected override void Start()

        {

            GameObject clavicle = GameObject.FindGameObjectWithTag("clavicle_r");

            //upper_right_arm.transform.parent = clavicle.transform;
            upper_right_arm.gameObject.transform.position
                = GameObject.FindGameObjectWithTag("up_arm_r").transform.position;

            //position = upper_right_arm.transform.localPosition;

            upper_right_arm.gameObject.transform.localRotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;

            rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;

            base.Start();
        }

        // Update is called once per frame
        private void Update()
        {
            upper_right_arm.transform.localRotation = rotation;

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


