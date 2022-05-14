using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace RosSharp.RosBridgeClient
{
    public class RightClavicleController : UnitySubscriber<MessageTypes.Geometry.Pose>
    {
        public GameObject right_clavicle;
        public Vector3 position;
        public Quaternion rotation;
        protected override void ReceiveMessage(MessageTypes.Geometry.Pose message)
        {
            rotation = GetRotation(message).Ros2Unity();
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

        // Start is called before the first frame update
        void Start()
        {
            /*right_clavicle.gameObject.transform.localRotation
             = GameObject.FindGameObjectWithTag("clavicle_r").transform.localRotation;

            rotation = GameObject.FindGameObjectWithTag("clavicle_r").transform.localRotation;*/
            

            base.Start();
        }

        // Update is called once per frame
        void Update()
        {
            //right_clavicle.transform.localRotation = rotation;
        }
    }
}

