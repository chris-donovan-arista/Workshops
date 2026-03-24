# Campus A-02 Wired Lab Guide

## Access Interface Configuration

![CloudVision](images/cv-logo.png)

This Lab Guide:

https://github.com/arista-rockies/Workshops/tree/main/Campus

---

## Table of Contents

1. [Full Lab Topology](#1-full-lab-topology)
2. [POD Topology](#2-pod-topology)
3. [Accessing CloudVision as a Serivce](#3-accessing-cloudvision-as-a-service)
4. [Creating Port Profiles](#4-creating-port-profiles)
5. [Assigning Port Profiles for AP and RPI](#5-assigning-port-profiles-for-ap-and-rpi)

---

## 1. Full Lab Topology

![Full Lab Topology](images/full-lab-topology.png)

---

## 2. POD Topology

![POD Topology](images/pod-lab-topology.png)

---

## 3. Accessing CloudVision as a Service

1. In your Google Chrome browser, enter the following URL: https://www.arista.io/ to access CloudVision as a Service (CVaaS).
   - In the **“Organization”** box enter the Organization name **rockies-training-##** where **##** is a 2 digit character between 01-20 that was assigned to your lab/Pod, then click **Enter**.

![CVaaS Login Page](images/cvaas-login.png)


2. Click the Log in with Launchpad button and provide your assigned lab/Pod email address and password:

![Organization Selection](images/launchpad-login.png)

3. You will now be logged into CloudVision

![CloudVision Dashboard](images/cloudvision-dashboard.png)

---

## 4. Creating Port Profiles

This lab will help you create 2 port profiles and apply them to interfaces in your Lab network.

1. Click on the **Provisioning** menu option, then choose **Studios**

![Provisioning Studios](images/provisioning-studios.png)

In order to make any changes within the Studios framework, you need to create a Workspace.

2. Click **Create Workspace** 
    - name it **Create Port Profiles** 
    - Select **Create**. 
    
*A workspace acts as a sandbox where you can stage your configuration changes before deploying them*

![Create Workspace](images/create-workspace.png)

3. Select the **Access Interface Configuration Studio**
  
![Access Interface Configuration Studio](images/access-interface-configuration.png)

4. Click **Add Port Profile**, 
    - name it “Wireless-Access-Point”
    - Click the **expand arrow** on the right of the new profile name

![Add Port Profile Wireless1](images/add-port-profile-wireless1.png)

5. Enter the following values on this configuration page

    - Description: **Wireless-Access-Point**
    - Enabled: **Yes** 

![Add Port Profile Wireless2](images/add-port-profile-wireless2.png)

6. Configure the VLAN and Mod
    - Mode: **Access**  
    - VLANs: **1##** where **##** is a 2 digit character assigned to your lab/Pod. e.g Pod01 is VLAN101, Pod13 is VLAN113  


![Add Port Profile Wireless3](images/add-port-profile-wireless3.png)

7. Port-Channel:
    - Port-Channel: **Yes**
    - Description: **Wireless Access Point Port-Channel**
    - Mode: **Active**
    - Enabled: **Yes**
    - MLAG: **Yes**
    - Select **LACP Fallback**

*The Wireless Access Point has the capability to run a port channel but is not currently configured as such. We will use LACP fallback so we may provision the Access Point with its current configuration*

![Add Port Profile Wireless4](images/add-port-profile-wireless4.png)

8. LACP Fallback
    - Mode: **Individual**
    - Navigate back to the previous page by clicking the breadcrump labeled **Wireless-Access-Point**

![Add Port Profile Wireless5](images/add-port-profile-wireless5.png)

9. POE:  
    - Reboot Action: **Maintain**
    - Link Down Action: **Maintain**  
    - Shutdown Action: **Maintain** 

![Add Port Profile Wireless6](images/add-port-profile-wireless6.png)


10. Navigate back to the Access interface Configuration Studio landing page by clicking the breakdrumb labeled **Access Interface Configuration** toward top of your window


![Interface Studio Navigate](images/interface-studio-navigate.png)

11. Click Add Port Profile 
    - Name the profile **Wired-RasPi** 
    - Click the **expand arrow** on the right of the new profile name

![Add Port Profile Wired](images/add-port-profile-wired1.png)

12. Enter the following values on this configuration page
    - Description: **Wired-RasPi**
    - Enabled: **Yes**  

![Add Port Profile Wired 2](images/add-port-profile-wired2.png)

13. Mode, VLAN and Spanning-tree:
    - Mode: **Access**  
    - VLANs: **1##** where **##** is a 2 digit character assigned to your lab/Pod. e.g Pod01 is VLAN101, Pod13 is VLAN113  
    - Spanning Tree
      - Portfast: **edge**
      - BPDU Guard: **enabled**


![Add Port Profile Wired 3](images/add-port-profile-wired3.png)

14. 802.1X:
    - Enabled: **Yes**  
    - Click **MAC Based Authentication**

![Add Port Profile Wired 4](images/add-port-profile-wired4.png)

15. Mac Based Authentication:
    - Set Enabled: **Yes**
    - Navigate back to the previous page by clicking the breadcrump labeled **Wired-RasPi**

![Add Port Profile Wired 5](images/add-port-profile-wired5.png)


16. POE:  
     - Reboot Action: **Maintain**   
     - Link Down Action: **Maintain** 
     - Shutdown Action: **Maintain** 

![Add Port Profile Wired 6](images/add-port-profile-wired6.png)

17. Select **Review Workspace**

![Review Workspace](images/review-workspace.png)

*Note that no device configurations changes are being proposed. We have simply created the **template** we will use to assign configuration to an interface*
   
18. Select **Submit Workspace**

![Review Workspace2](images/review-workspace2.png)


19. Click **Close**

![Close Workspace Pop up](images/submit-workspace.png)


**Lab Section Complete!**

---

## 5. Assigning Port Profiles for AP and RPI

1. Assign the configured port profiles to the switches access ports

    - Navigate to **Network Hierarchy**
    - Navigate through 
      - **Network**  
      - **Workshops** 
      - **IT-Bldg**  
      - **IDF1**

![Hierarchy Navigation](images/hierarchy-navigation.png)

2. Select the **Front Panel** tab

![Hierarchy Front Panel](images/quick-action1.png)

3. Select **Ethernet1** on **leaf1b**
    - Select **Configure**

![Quick Action Select Interface](images/quick-action2.png)

4. All Fields should be pre-populated except the below
    - Port Profile: **Wired-RasPi**
    - Enabled: **Yes**
    - Select **Submit**

![Submit Wired Profile](images/quick-action3.png)

5. Once the Change Control has been executed, click **Close** 

![Quick Action Close](images/quick-action4.png)

6. AP Interface Configuration
  - Select **Ethernet14** on both **leaf1a** and **leaf1b**
  - Select **Configure**
  

![Quick Actions 3](images/quick-action5.png)


7. All Fields should be pre-populated except the below
    - Port Profile: **Wireless-Access-Point**
    - Enabled: **Yes**
    - Select **Submit**

![Finish Configuration](images/quick-action6.png)

8. Select **Close**

![Quick Action Close](images/quick-action4.png)
---

**LAB GUIDE COMPLETE!**
