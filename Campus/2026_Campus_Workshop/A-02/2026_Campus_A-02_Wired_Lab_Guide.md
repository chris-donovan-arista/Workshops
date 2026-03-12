# Campus A-02 Wired Lab Guide

## Access Interface Configuration

![CloudVision](images/cv-logo.png)

This Lab Guide:

https://github.com/arista-rockies/Workshops/tree/main/Campus

---

## Table of Contents

1. Full Lab Topology  
2. POD Topology  
3. Accessing CloudVision as a Service  
4. Creating Port Profiles  
5. Assigning Port Profiles for AP and RPI  

---

## Full Lab Topology

![Full Lab Topology](images/full-lab-topology.png)

---

## POD Topology

![POD Topology](images/pod-lab-topology.png)

---

## 1. Accessing CloudVision as a Service

In your Google Chrome browser, enter the following URL:  
https://www.arista.io/ to access CloudVision as a Service (CVaaS).

1. in the “Organization” box enter the Organization name “rockies-training-##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod, then click “Enter”.

![CVaaS Login Page](images/cvaas-login.png)

2. Click the Log in with Launchpad button and provide your assigned lab/Pod email address and password:

![Launchpad Login](images/launchpad-login.png)



You will now be logged into CloudVision

![CloudVision Dashboard](images/cloudvision-dashboard.png)

---

## 2. Creating Port Profiles

This lab will help you create port profiles and apply them to interfaces in your ATD network.

1. Click on the **Provisioning** menu option, then choose **Studios**

![Provisioning Studios](images/provisioning-studios.png)

2. Click Create Workspace and name it Create Port Profiles then select Create. A workspace acts as a sandbox where you can stage your configuration changes before deploying them

![Create Workspace](images/create-workspace.png)

3. Disable the Active Studios toggle to display all available CloudVision Studios (which when enabled will only show used/active Studios).  
*Note:- the toggle may already be in the disabled position.*

![Disable Active Studios](images/show-active-studios.png)

4. Create two port profiles using the Access Interface Configuration studio that will be used to provision connected hosts.

   a. Launch the Access Interface Configuration
  
![Access Interface Configuration Studio](images/access-interface-configuration.png)

   b. Click Add Port Profile, name it “Wireless-Access-Point”, and click the arrow on the right

![Add Port Profile Wireless1](images/add-port-profile-wireless1.png)

   c. Enter the following values on this configuration page

 - Description: “Wireless-Access-Point”  
 - Enabled: Yes  

![Add Port Profile Wireless2](images/add-port-profile-wireless2.png)

- Mode: Access  
- VLANs: “1##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod. e.g Pod01 is VLAN101, Pod13 is VLAN113  


![Add Port Profile Wireless3](images/add-port-profile-wireless3.png)

- Port-Channel:
  - Port-Channel: Yes
  - Description: Wireless Access Point Port-Channel
  - Mode: Active
  - Enabled: Yes
  - MLAG: Yes
  - Select LACP Fallback

*The Wireless Access Point has the capability to run a port channel but is not currently configured as such. We will use LACP fallback so we may provision the Access Point with its current configuration*

![Add Port Profile Wireless4](images/add-port-profile-wireless4.png)

- LACP Fallback
  - Mode: Individual

![Add Port Profile Wireless5](images/add-port-profile-wireless5.png)


- POE:  
    - Reboot Action: Maintain  
    - Link Down Action: Maintain  
    - Shutdown Action: Maintain  

![Add Port Profile Wireless6](images/add-port-profile-wireless6.png)


d. Navigate back to Access interface Configuration by clicking on the top


![Interface Studio Navigate](images/interface-studio-navigate.png)

e. Click Add Port Profile, name it “Wired-RasPi”, and click the arrow on the right

![Add Port Profile Wired](images/add-port-profile-wired1.png)

f. Enter the following values on this configuration page
  - Description: “Wired-RasPI”  
  - Enabled: Yes  

![Add Port Profile Wired 2](images/add-port-profile-wired2.png)

  - Mode: Access  
  - VLANs: “1##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod. e.g Pod01 is VLAN101, Pod13 is VLAN113  
  - Spanning Tree
    - Portfast: edge
    - BPDU Guard: enabled


![Add Port Profile Wired 3](images/add-port-profile-wired3.png)

  - 802.1X: Enabled = Yes  
  - Click MAC Based Authentication

![Add Port Profile Wired 4](images/add-port-profile-wired4.png)

  - Set Enabled:Yes
    - Navigate back to the previous page

![Add Port Profile Wired 5](images/add-port-profile-wired5.png)


  - POE:  
     - Reboot Action: Maintain   
     - Link Down Action: Maintain  
     - Shutdown Action: Maintain  

![Add Port Profile Wired 6](images/add-port-profile-wired6.png)

5. Review and Submit the Workspace

  - Click Review Workspace

![Review Workspace](images/review-workspace.png)

*Note that none of the device configurations have been changed after submitting this workspace*
   
  - Click Submit Workspace

![Review Workspace2](images/review-workspace2.png)


c. Click Close

![Close Workspace Pop up](images/submit-workspace.png)

---

## 3. Assigning Port Profiles for AP and RPI

1. Assign the configured port profiles to the switches access ports

  - Click Overview option on the navigation bar

![Overview Navigation](images/overview-navigation.png)

  - Locate the Quick Actions panel on the lower left of the screen and Click Access Interface Configuration

![Quick Actions Access Interface Configuration](images/quick-actions-access-interface.png)

  - Device Type: **Access Pod**
  - Campus: **Workshop**
  - Campus Pod: **IT-Bldg**
  - Access Pod: **IDF1**

*Note: These should be the only one options for each drop-down.*

![Quick Action Select Device](images/quick-action1.png)

  - **Select** to highlight port **Ethernet1** on switch labeled **campus-pod{$POD#}-leaf1b**
  - Port Profile: **Wired-RasPi**
  - Enabled: **Yes** 
  - Click **Submit**

![Submit Wireless Port Profile](images/quick-action2.png)

  - Once the Change Control has been executed, click **Configure Additional Inputs** to configure another access port

![Configure Additional Inputs](images/configure-additional-inputs.png)

  - Device Type: **Access Pod**
  - Campus: **Workshop**
  - Campus Pod: **IT-Bldg**
  - Access Pod: **IDF1**
  - **Select** to highlight port **Ethernet14** on switches labeled **campus-pod{$POD#}-leaf1a and b**
  - Port Profile: **Wireless-Access-Point**
  - Enabled: **Yes** 
  - Click **Submit**

![Quick Actions 3](images/quick-action3.png)


  - Once the Change Control has been executed, click Finish

![Finish Configuration](images/finish-configuration.png)

---

LAB GUIDE COMPLETE
