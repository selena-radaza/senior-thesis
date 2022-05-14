using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace RosSharp.RosBridgeClient
{
    public class RotationInformation : UnitySubscriber<MessageTypes.Geometry.Pose>
    {

        public GameObject button;
        public Vector3 position;
        public Quaternion rotation;
        //string text;
        // Start is called before the first frame update
        protected override void Start()
        {
            button.GetComponentInChildren<Text>().text = getModelInfo();
            position = GameObject.FindGameObjectWithTag("up_arm_r").transform.localPosition;
            rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;
        }

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            position = GetPosition(message).Ros2Unity();
            rotation = GetRotation(message).Ros2Unity();

            Debug.Log("Rotation received: " + rotation);


        }

        // Update is called once per frame
        void Update()
        {
            //Debug.Log("Model info:" + getModelInfo());
            button.GetComponentInChildren<Text>().text = getModelInfo();
        }

        public string getModelInfo()
        {
            return "Position: " + position.ToString() + "\nRotation: " + rotation.ToString();
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
                (float)message.orientation.y,
                -(float)message.orientation.z,
                -(float)message.orientation.x,
                (float)message.orientation.w);

            return cur;
        }
    }
}

