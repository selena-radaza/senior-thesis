using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ManualFrontRaise : MonoBehaviour
{
    // Start is called before the first frame update

    public Quaternion start_position = new Quaternion(0.710722566f, 0.628822327f, -0.148129314f, 0.278412998f);
    public Quaternion end_position = new Quaternion(0.525818229f, 0.478533983f, -0.395720929f, 0.58131355f);
    public Quaternion rotation;
    public GameObject shoulder;
    private float time_count = 0.0f;

    void Start()
    {
        Application.targetFrameRate = 30;
        rotation = start_position;
        shoulder.gameObject.transform.localRotation = start_position;
        downwardMotion();
        upwardMotion();

       
    }

    void downwardMotion()
    {
        shoulder.transform.localRotation = Quaternion.Slerp(start_position, end_position, time_count);
        time_count += Time.deltaTime;
    }

    void upwardMotion()
    {
        shoulder.transform.localRotation = Quaternion.Slerp(end_position, start_position, time_count);
        time_count += Time.deltaTime;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
