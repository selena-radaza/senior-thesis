using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class ShoulderArrowController : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject arrow;
        public Vector3 position;
        public Quaternion rotation;

        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            rotation = GetRotation(message).Ros2Unity();
        }

        private Quaternion GetRotation(MessageTypes.Geometry.Pose message)
        {
          
            Quaternion cur = new Quaternion(
                (float)message.orientation.y,
                -(float)message.orientation.z,
                -(float)message.orientation.x,
                (float)message.orientation.w);

            return cur;

          
        }
        // Start is called before the first frame update
        protected override void Start()
        {
            arrow.gameObject.transform.position
                = GameObject.FindGameObjectWithTag("up_arm_r").transform.position;

            Debug.Log("Arrow position: " + arrow.gameObject.transform.position);

            arrow.gameObject.transform.rotation
                = GameObject.FindGameObjectWithTag("up_arm_r").transform.rotation;
        }

        // Update is called once per frame
        private void Update()
        {
            arrow.gameObject.transform.localRotation = rotation;
        }
    }
}

