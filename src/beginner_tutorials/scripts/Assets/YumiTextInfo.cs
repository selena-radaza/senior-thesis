using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class YumiTextInfo : MonoBehaviour
{
    private Vector3 position;
    private Vector3 rotation;
    private Vector3 human_rotation;
    public Text position_text;
    public Text rotation_text;
    //public Text diff_text;

    // Start is called before the first frame update
    void Start()
    {
        rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation.eulerAngles;
        human_rotation = GameObject.FindGameObjectWithTag("user_shoulder").transform.localRotation.eulerAngles;

        rotation_text.text = return_text();
    }

    // Update is called once per frame
    void Update()
    {
        rotation = GameObject.FindGameObjectWithTag("up_arm_r").transform.localRotation.eulerAngles;
        human_rotation = GameObject.FindGameObjectWithTag("user_shoulder").transform.localRotation.eulerAngles;

        rotation_text.text = return_text();


    }

    string return_text ()
    {
        string str = "";
        str += "YuMi Rotation: " + rotation.ToString();
        str += "\nHuman Rotation: " + human_rotation.ToString();

        Vector3 diff = rotation - human_rotation;
        str += "\nDifference: " + diff.ToString();

        return str;
    }
}
