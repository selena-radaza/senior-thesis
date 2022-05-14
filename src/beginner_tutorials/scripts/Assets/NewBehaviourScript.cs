using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public string test;
    public Quaternion rotation;
    public int frameCount = 0;
    // Start is called before the first frame update
    void Start()

    {
        // Start Position: Vector3(69.1259995,6.70915615e-05,295.310852)
        // Second Exercise Position:  Vector3(0,0,295)
        rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;
        frameCount++;
    }

    // Update is called once per frame
    void Update()
    {
        if (frameCount < 80)
        {
            float val = 0.01F;

            GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation *= new Quaternion(0, 0, val, 1);
            rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;
            frameCount++;
        }
        else if (frameCount < 160)
        {
            float val = -0.01F;

            GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation *= new Quaternion(0, 0, val, 1);
            rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation;
            frameCount++;
        }



    }
}
