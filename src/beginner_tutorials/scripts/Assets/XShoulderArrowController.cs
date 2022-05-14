using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class XShoulderArrowController : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject arrow;
        public Vector3 position;
        public Quaternion rotation;

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            rotation = GetRotation(message).Ros2Unity();
            print("Rotation when received: " + rotation);
        }

        private Quaternion GetRotation(MessageTypes.Geometry.Pose message)
        {

            Quaternion cur = new Quaternion(
                (float)message.orientation.y,
                -(float)message.orientation.z,
                -(float)message.orientation.x,
                (float)message.orientation.w);

            return cur;

            // return cur *= Quaternion.Euler(0f, 90f, 0f);


        }
        // Start is called before the first frame update
        protected override void Start()
        {
            arrow.gameObject.transform.position
                = GameObject.FindGameObjectWithTag("up_arm_r").transform.position;

            Debug.Log("Arrow position: " + arrow.gameObject.transform.position);

            arrow.gameObject.transform.localRotation
                = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;

            rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;
        }

        // Update is called once per frame
        private void Update()
        {
            arrow.transform.localRotation = rotation;
            Debug.Log("Updated " + rotation);
        }
    }
}


