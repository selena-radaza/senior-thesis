using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SideRaiseUpperArm : MonoBehaviour
{
    public string test;
    public Quaternion shoulder_rotation;
    public Quaternion elbow_rotation;
    public int frameCount = 0;
    // Start is called before the first frame update
    void Start()

    {
        // Shoulder Start Position:  (0, -90, 0)
        // Elbow Start Position: (0, -40, -90)
        shoulder_rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;
        elbow_rotation = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation;
        frameCount++;
    }

    // Update is called once per frame
    void Update()
    {
        if (frameCount < 60)
        {
            float val = 0.01F;

            GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation *= new Quaternion(val, 0, 0, 1);
            shoulder_rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;

            GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation *= new Quaternion(0, 0, val, 1);
            elbow_rotation = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation;
            frameCount++;
        }
        else if (frameCount < 120)
        {
            float val = -0.01F;

            GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation *= new Quaternion(val, 0, 0, 1);
            shoulder_rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;

            GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation *= new Quaternion(0, 0, val, 1);
            elbow_rotation = GameObject.FindGameObjectWithTag("low_arm_r").transform.localRotation;
            frameCount++;
        }



    }
}
