# Campus C-03 AGNI Lab Guide - Wireless Guest Captive Portal

![image1](images/CVCUE_logo.png) 
![image2](images/AGNI_logo.png)


#### This Lab Guide:
Campus/2026_Campus_Workshop/C-03/Rockies Campus C-03 AGNI Lab Guide - Wireless Guest Captive Portal


---

## Table of Contents

Full Lab Topology  
POD Topology

NAC Lab #3 - Configuring Guest Captive Portal  
1. Create a Guest Portal in AGNI  
2. Create a Network in AGNI  
3. Create a Role Profile in CV-CUE  
4. Create a SSID in CV-CUE  

---

## Full Lab Topology

![image3](images/full-lab-topology.png)

---

## POD Topology

![image4](images/pod-lab-topology.png)

---

## NAC Lab #3 - Configuring Guest Captive Portal

## 1. Create a Guest Portal in AGNI

Return to the LaunchPad tab and Log into AGNI [https://launchpad.wifi.arista.com/](https://launchpad.wifi.arista.com/), or access the AGNI tab in your browser.

![image5](images/LaunchPad1.png)

Navigate to **Identity \> Guest \> Portals**.

![image6](images/Portals.png)

In **Guest Portals**, the **Default** portal is always present. Let’s create a new guest portal.

Click the **Add Web Portal** button. 

In the **Configuration** tab, provide the Portal Name \- **ATD-\#\#-Portal** (where \#\# is a 2 digit character between 01-20 that was assigned to your lab/Pod).

Click in the **Authentication Types** drop down box to see the available authentication types. We'll use **Clickthrough** for this lab.

In the **Post-Authentication Redirect URL** box, enter **https://www.arista.com**.

Then select **Customization**

![image7](images/AddWebPortal.png)

The available Theme templates are **Default** or **Split Screen**. Select **Default**.

Click in the **Select element** drop down box to see the available options to customize the portal settings..

* **Page**  
* **Login Toggle**  
* **Terms of Use and Privacy Policy**  
* **Logo**  
* **Guest Login Submit Button**

![image8](images/WebPortalCustom.png)

When done, click **Add Web Portal.** 

Click **\<-- Back** to see the new Guest Portal listing.

![image9](images/GuestPortals.png)

## 2. Create a Network in AGNI

Navigate to the **Access Control \> Networks.**

Click on **Networks** and then **\+ Add**.

![image10](images/AGNI_Networks.png)                ![image11](images/AGNI_Add.png)                     

Add the following:

Name: **Guest Captive Portal**  
Connection Type: **Wireless**  
SSID: **ATD-\#\#-GUEST**  
**Authentication**  
Authentication Type: **Captive Portal**  
Captive Portal Type: **Internal**  
Select internal portal: **ATD-\#\#-Portal**  
**Captive Portal**  
Initial Role for Portal Authentication: **ATD-\#\#-Portal-Role**  
Click **Add Network**	  
![image12](images/AGNI_Add_Network.png)  
![image13](images/AGNI_Add_CP_Network.png) 

Copy the portal URL at the bottom of the page.  
![image14](images/AGNI_CP_Domains.png)

**Keep the browser tab for AGNI open.** We’ll return to get the Domains allowlist for the Role Profile in CV-CUE.

## 3. Create a Role Profile in CV-CUE

Return to the LaunchPad tab and Log into CV-CUE [https://launchpad.wifi.arista.com/](https://launchpad.wifi.arista.com/), or access the CV-CUE tab in your browser. 

![image15](images/LaunchPad2.png)

In **CV-CUE**, navigate to **Configure \> Network Profiles \> Role Profile.**

**Add** Role Profile.

Add the Role Name as **ATD-\#\#-Portal-Role.**

Enable the **Redirection** check box and select **Static Redirection.**

In the **Redirect URL** field, add the portal URL \- copied from AGNI.

**NOTE:** Role Profiles are case sensitive.

![image16](images/CVCUE_Role_Profile.png)

**Keep the browser tab for CV-CUE open.**

Return to the **AGNI tab.** From the **Guest Captive Portal** network in **AGNI**, click on **Show Domains**, click on **Copy** to copy the Domains allowlist.

![image17](images/AGNI_CP_Domains.png)

Return to the **CV-CUE tab**, enable the **HTTPS Redirection** check box.

In the **Websites That Can Be Accessed Before Authentication** field, paste the Domains allowlist you copied from AGNI.

![image18](images/AGNI_HTTPS_Redirection.png)

Click **Save** to save the **Network Profile**.

## 4. Create a SSID in CV-CUE

Navigate to **Configure \> WiFi.**

Add a new SSID by clicking on **Add SSID.**

Provide the SSID Name — **ATD-\#\#-GUEST.**

![image19](images/CVCUE_CP_SSID1.png)

Next, Click on **Security**, then select **OWE Transition Mode.**

![image20](images/CVCUE_CP_SSID2.png)

[Opportunistic Wireless Encryption (OWE) Transition Mode](#full-lab-topology) Opportunistic Wireless Encryption (OWE) Transition Mode enables a seamless, secure migration from open, unencrypted Wi-Fi to encrypted Wi-Fi (Enhanced Open) without requiring manual network changes by users. It allows OWE-capable devices to use encryption while legacy devices still connect via traditional open methods.

Next, Click on the **3 Blue Dots** next to the Network tab.  

Click on the **Access Control** tab.

Enable the **Client Authentication** check box and select **RADIUS MAC Authentication.**

Select **RadSec.**

Select the **Authentication** and **Accounting** servers. 

Select **Send DHCP Options and HTTP User Agent**.

![image21](images/CVCUE_CP_SSID3.png) 

Select the **Role Based Control** checkbox and configure the following settings: 

* Rule Type — **802.1X Default VSA**  
* Operand — **Match**  
* Role — **ATD-\#\#-Portal-Role**. You created the **Portal** role profile while configuring the Role Profile in the previous section.

Select the **Client Isolation** checkbox.

![image22](images/CVCUE_CP_SSID4.png) 

Finally, Click on **Save & Turn SSID On,** then **Customize**.

![image23](images/CVCUE_TurnOn_SSID.png)

![image24](images/CVCUE_SSID_Customize.png)  

**Please Read\!**  
**Only select the “5 GHz” option** on the next screen (**uncheck** the 2.4 & 6GHz boxes), then click “**Turn SSID On**”.

**Using your Laptop or Cellphone, connect to the ATD-\#\#-GUEST Captive Portal network.**

**Next, Go to Monitoring - Sessions in AGNI and select your Captive Portal session to see your client session details.**

NAC LAB #3 COMPLETE
