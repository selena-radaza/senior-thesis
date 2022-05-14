using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CameraSwitch : MonoBehaviour
{
    public GameObject frontCam;
    public GameObject backCam;
    public GameObject rightCam;
    public GameObject leftCam;
    public GameObject topCam;

    public GameObject humanFrontCam;
    public GameObject humanBackCam;
    public GameObject humanLeftCam;
    public GameObject humanRightCam;
    public GameObject humanTopCam;
    // Start is called before the first frame update
    void Start()
    {
        frontCam.SetActive(true);
        backCam.SetActive(false);
        rightCam.SetActive(false);
        leftCam.SetActive(false);
        topCam.SetActive(false);

        humanFrontCam.SetActive(true);  
        humanBackCam.SetActive(false );
        humanRightCam.SetActive(false);
        humanLeftCam.SetActive(false);
        humanTopCam.SetActive(false);

       // GameObject.Find("Button").GetComponentInChildren<Text>().text = "Top View";
    }

    public void onTopViewPress()
    {
        Debug.Log("top view button pressed\n");
        turnOffCameras();
        topCam.SetActive(true);
        humanTopCam.SetActive(true);
    }

    public void onRightViewPress()
    {
        Debug.Log("Right view pressed\n");
        turnOffCameras();
        rightCam.SetActive(true);
        humanRightCam.SetActive(true);
    }

    public void onLeftViewPress()
    {
        Debug.Log("Left view pressed\n");
        turnOffCameras();
        leftCam.SetActive(true);
        humanLeftCam.SetActive(true);
    }

    public void onBackViewPress()
    {
        Debug.Log("Back view pressed\n");
        turnOffCameras();
        backCam.SetActive(true);
        humanBackCam.SetActive(true);
    }

    public void onFrontViewPress()
    {
        Debug.Log("Front view pressed\n");
        turnOffCameras();
        frontCam.SetActive(true);
        humanFrontCam.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void turnOffCameras()
    {
        frontCam.SetActive(false);
        backCam.SetActive(false);
        rightCam.SetActive(false);
        leftCam.SetActive(false);
        topCam.SetActive(false);

        humanBackCam.SetActive(false);
        humanFrontCam.SetActive(false);
        humanTopCam.SetActive(false);
        humanLeftCam.SetActive(false);
        humanRightCam.SetActive(false);
    }
}
