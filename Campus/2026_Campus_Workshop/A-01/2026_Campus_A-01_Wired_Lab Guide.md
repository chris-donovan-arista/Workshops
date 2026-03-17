# Campus A-01 Wired Lab Guide  
## Provisioning a Campus Fabric

This Lab Guide:

Campus/2026_Campus_Workshop/A-01/2026_Campus_A-01_Wired_Lab Guide.md

---

## Table of Contents

Full Lab Topology  
POD Topology  
1. Accessing CloudVision as a Service  
2. Onboarding a new device into CVaaS  

---

## Full Lab Topology

![Full Lab Topology](images/full-lab-topology.png)

---

## POD Topology

![POD Topology](images/pod-lab-topology.png)

---

## Accessing CloudVision as a Service

In your Google Chrome browser, enter the following URL: https://www.arista.io/ to access CloudVision as a Service (CVaaS).

* In the **“Organization”** box enter the Organization name “rockies-training-<span style="color: red;">##</span>” where <span style="color: red;">##</span> is a 2 digit character between 01-20 that was assigned to your lab/Pod, then click **“Enter”**.

![CVaaS Login Page](images/cvaas-login.png)


* Click the Log in with Launchpad button and provide your assigned lab/Pod email address and password:

![Organization Selection](images/launchpad-login.png)

* You will now be logged into CloudVision

![CloudVision Dashboard](images/cloudvision-dashboard.png)

---

## Onboarding a new device into CVaaS

In this lab you will be configuring the switches through CloudVision. Today you will be adding a second Leaf Switch to an existing Campus Fabric/POD using Cloud Vision’s guided workflow.

* Login to CloudVision, then click on the Network Hierarchy menu option.

![Network Hierarchy Menu](images/network-hierarchy-menu.png)

* Navigate through the Network Hierarchy Tree to: **Network > Workshop > IT-Bldg > IDF1**

![Network Hierarchy](images/network-hierarchy-tree.png)

* Hover your mouse over **IDF1** and select the **3 dots** that appear. Select **Add Device** to begin the device provisioning guided workflow.

![Add Device](images/add-device.png)

* The Deployment Details should be pre-populated. Verify the value in each section (provided below),

   *  Deployment Type: Access Pod 
   *  Campus: **Workshop**  
   *  Campus-Pod: **IT-Bldg**  
   *  Access-Pod: **IDF1**  
   *  Under **Select Available Devices** select the **check box**de with a hostname of **sw-10.#.#.#** and then 
   *  Select **Continue**

![Deployment Details](images/deployment-details.png)


* Locate the new device being added under Role Assignment. 

   *  Update the hostname from **sw-[IP_ADDRESS]** to **campus-pod[POD#]-leaf1b**  
   *   Under Role select **Leaf** 
   *  Select **Continue**





![Role Assignment](images/role-assignment.png)

* Select **Continue**

*(Although not part of the lab today, this section of the workflow allows us to set the leaf we are currently provisioning to also provide Zero Touch Provisioning workflow to switches that are downstream from this new Leaf.)*

![Continue](images/hierarchy-deploy-ztp-option.png)

* The inputs provided in the guided workflow will be used to generate inputs within CloudVision Studios. We will select Build Workspace and those inputs will generate the configuration to provision our new device. (This may take up to 1 minute)


![Build Workspace](images/build-workspace.png)

* After the Workspace has completed building you will get 2 small window pop ups.
    * **Workspace created successfully**
    * **Success**. 
    * Select the X on these boxes 
    * Select **Review Workspace**

![Review Workspace](images/review-workspace.png)

* This will bring you into the Workspace that was generated from the guided workflow. You should see 2 devices (leaf1a and your newly added switch) shown under Proposed Configuration.

    *  Take some time to review the proposed configuration.
    * leaf1a - Check for the creation of a new port-channel and mlag configuration.
    * leaf1b - Complete provisioned switch configuration

![Review Workspace](images/review-workspace2.png)

* After taking some time to review the workspace select **Submit Workspace**.

![Submit Worksapce](images/submit-workspace.png)

* Select **View Change Control**.

![Change Control](images/review-change-control.png)

* This will bring us to the Change Control that was created by the workspace submission. In this step we will be utilizing a Change Control Templates.

*A change control template provides the ability to create a configurable structure for repeatable change control operations*

* Select a Template
* From the available dropdown select Leaf Provisioning.(This template will add a 60 second delay before pushing configuration to leaf1a to ensure leaf1b gets the proposed configuration first)
* Select Apply Template.

![Change Control Template](images/change-control-template.png)

![Change Control Template](images/change-control-template2.png)

* The template selected will update the Change Control Stages into 2 sections. The first section will begin the configuration on the new Leaf immediately. The second section will delay pushing the configuration changes for 60 seconds, then configure leaf1a. You can expand all change control stages by selecting the 2 arros facing away from each

![Change Control Stages](images/change-control-stages.png)

* Select Review and Approve

![Review and Approve](images/review-and-approve.png)

* Up until this point, we have not made any changes to the actual running configuration of the devices. You can take some time to once again review the proposed configuration changes then select Approve and Execute.

*If Approve and Execute is not present select the Slider next to Execute Immediately.*

![Approve and Execute](images/approve-and-execute.png)

* The change control will execute and apply all the proposed configuration changes to the devices. The newly added device will be reloaded as it exits Zero Touch Provisioning (ZTP) mode and boots up with the designed configuration. You can review the Change Control logs by selecting Logs in the change control window.

![Change Control Logs](images/change-control-logs.png)

* Upon the completion of the Change Control we have deployed the configuration and provisioned leaf1b.


LAB GUIDE COMPLETE
