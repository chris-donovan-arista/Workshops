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
https://www.arista.io/  
to access CloudVision as a Service (CVaaS).

![CVaaS Login Page](images/cvaas-login.png)

in the “Organization” box enter the Organization name “rockies-training-##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod, then click “Enter”.

![Organization Selection](images/cvaas-organization.png)

Click the Log in with Launchpad button and provide your assigned lab/Pod email address and password:

![Launchpad Login](images/launchpad-login.png)

You will now be logged into CloudVision

![CloudVision Dashboard](images/cloudvision-dashboard.png)

---

## 2. Creating Port Profiles

This lab will help you create port profiles and apply them to interfaces in your ATD network.

Click on the Provisioning”menu option, then choose Studios

![Provisioning Studios](images/provisioning-studios.png)

Click Create Workspace and name it Create Port Profiles then select Create. A workspace acts as a sandbox where you can stage your configuration changes before deploying them

![Create Workspace](images/create-workspace.png)

Disable the Active Studios toggle to display all available CloudVision Studios (which when enabled will only show used/active Studios).  
*Note:- the toggle may already be in the disabled position.

![Disable Active Studios](images/disable-active-studios.png)

Create two port profiles using the Access Interface Configuration studio that will be used to provision connected hosts.

Launch the Access Interface Configuration

![Access Interface Configuration Studio](images/access-interface-configuration.png)

Click Add Port Profile, name it “Wireless-Access-Point”, and click the arrow on the right

![Add Port Profile Wireless](images/add-port-profile-wireless.png)

Enter the following values on this configuration page

Description: “Wireless-Access-Point”  

Enabled: Yes  

Mode: Access  

VLANs: “1##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod. e.g Pod01 is VLAN101, Pod13 is VLAN113  

POE:  

Reboot Action: Maintain  

Link Down Action: Maintain  

Shutdown Action: Maintain  

Navigate back to Access interface Configuration by clicking on the top

Click Add Port Profile, name it “Wired-RasPI”, and click the arrow on the right

![Add Port Profile Wired](images/add-port-profile-wired.png)

Enter the following values on this configuration page

Description: “Wired-RasPI”  

Enabled: Yes  

Mode: Access  

VLANs: “1##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod. e.g Pod01 is VLAN101, Pod13 is VLAN113  

802.1X: Enabled = Yes  

Click MAC Based Authentication

![MAC Based Authentication](images/mac-based-auth.png)

Set Enabled:Yes

Navigate back to the previous page

POE:  

Reboot Action: Maintain  

Link Down Action: Maintain  

Shutdown Action: Maintain  

Review and Submit the Workspace

Click Review Workspace

![Review Workspace](images/review-workspace.png)

Note that none of the device configurations have been changed after submitting this workspace

Click Submit Workspace

![Submit Workspace](images/submit-workspace.png)

Click Close

---

## 3. Assigning Port Profiles for AP and RPI

Assign the configured port profiles to the switches access ports

Click Overview option on the navigation bar

![Overview Navigation](images/overview-navigation.png)

Locate the Quick Actions panel on the lower left of the screen and Click Access Interface Configuration

![Quick Actions Access Interface Configuration](images/quick-actions-access-interface.png)

Select the Campus (Workshop), Campus Pod (IT-Bldg), and Access Pod(IDF1)  
*Note: there is only one option for each drop-down.

![Select Campus Pod](images/select-campus-pod.png)

Select to highlight port Ethernet1 on bottom switch: campus-pod<##>-leaf1c  
*Note: you will may see the bottom device with a hostname format: sw-<IP> Example: sw-10.0.113.40

![Select Ethernet1](images/select-ethernet1.png)

Choose the Port Profile of Wireless-Access-Point

Click Yes radio button under Enabled

Click Submit

![Submit Wireless Port Profile](images/submit-wireless-port.png)

Once the Change Control has been executed, click Configure Additional Inputs to configure another access port

![Configure Additional Inputs](images/configure-additional-inputs.png)

Again, select the Campus (Workshop), Campus Pod (IT-Bldg), and Access Pod(IDF1)

Select to highlight port Ethernet2 on campus-pod<##>-leaf1c (hostname may not match)

![Select Ethernet2](images/select-ethernet2.png)

Choose the Port Profile of “Wired-RasPI”

Click Yes radio button under Enabled

Click Submit

![Submit Wired Port Profile](images/submit-wired-port.png)

Once the Change Control has been executed, click Finish

![Finish Configuration](images/finish-configuration.png)

---

LAB GUIDE COMPLETE
