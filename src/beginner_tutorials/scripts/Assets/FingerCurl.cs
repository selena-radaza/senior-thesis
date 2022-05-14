using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FingerCurl : MonoBehaviour

    
{
    public Quaternion rotation;
    public Vector3 position;
    GameObject[] gameObs;
    // Start is called before the first frame update
    void Start()
    {
        float val = 50.0f;
        rotation = new Quaternion(0, 0, -0.5f, 1) ;
        gameObs = GameObject.FindGameObjectsWithTag("finger_component");
       for (int i = 0; i < gameObs.Length; i++)
        {
            gameObs[i].transform.localRotation = rotation;
        }
    }

    // Update is called once per frame
    void Update()
    {
        //gameObject.transform.rotation *= Quaternion.identity;
    }
}
