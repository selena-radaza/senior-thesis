using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class RightWristController : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject right_wrist;
        public Vector3 position;
        public Quaternion rotation;

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            //position = GetPosition(message).Ros2Unity();
            rotation = GetRotation(message).Ros2Unity();
            Debug.Log("Rotation When Received: " + rotation);


        }


        // Start is called before the first frame update
        protected override void Start()

        {
            Application.targetFrameRate = 15;

            right_wrist.gameObject.transform.localPosition
                = GameObject.FindGameObjectWithTag("right_wrist_r").transform.localPosition;

            //position = GameObject.FindGameObjectWithTag("right_wrist_r").transform.localPosition;

            right_wrist.gameObject.transform.localRotation
                = GameObject.FindGameObjectWithTag("right_wrist_r").transform.localRotation;

            rotation = GameObject.FindGameObjectWithTag("right_wrist_r").transform.localRotation;

            base.Start();
        }

        // Update is called once per frame
        private void Update()
        {
            //right_wrist.transform.localPosition = position;
            right_wrist.transform.localRotation = rotation;
            Debug.Log("Rotation After Updated: " + rotation);
            //Debug.Log("Position After Updated: " + position);
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


