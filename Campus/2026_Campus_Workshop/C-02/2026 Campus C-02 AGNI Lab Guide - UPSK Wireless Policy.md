# Campus C-02 AGNI Lab Guide - UPSK Wireless Policy

![image1](images/CVCUE_logo.png)
![image2](images/AGNI_logo.png)
---

This Lab Guide:

Campus/2026_Campus_Workshop/C-02/Rockies Campus C-02 AGNI Lab Guide - UPSK Wireless Policy

---

## Table of Contents

Full Lab Topology  
POD Topology

NAC Lab #2 - Create UPSK Wireless Policy  
1. Create Identity UPSK SSID:  
2. Create UPSK Network and Segment:  
3. Create an AGNI Local User and Enroll Personal Device  
4. Create an AGNI Client Group  

---

## Full Lab Topology

![image3](images/full-lab-topology.png)

---

## POD Topology


![image4](images/pod-lab-topology.png)
---

## NAC Lab #2 - Create UPSK Wireless Policy

---

### 1. Create Identity UPSK SSID:

Return to the LaunchPad tab and Log into CV-CUE https://launchpad.wifi.arista.com/, or access the CV-CUE tab in your browser.

![image5](images/image5.png)

Next, we will modify the PSK SSID we created in the CV-CUE lab.

While on the Corp folder, Click on Configure and then WiFi

![image6](images/image6.png)

Next, click on the 3 Dots and select Create a Copy on the SSID ATD-##-PSK where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod

![image7](images/image7.png)
![image8](images/image8.png)

Select - Currently Selected Folders and then Continue.

![image9](images/image9.png)

Click on the new SSID and select Edit.

![image10](images/image10.png)

On the Basic Tab rename the SSID to ATD-##-UPSK, and copy the SSID Name and paste it in the Profile Name field.

![image11](images/image11.png)

Next, click on the Security Tab and change the WPA2 Security from PSK to UPSK

![image12](images/image12.png)

Next, select UPSK Identity Lookup

![image13](images/image13.png)


For more information on UPSK click here: https://arista.my.site.com/AristaCommunity/s/article/Unique-PSKs

Next, Click on the Access Control tab.  Under RADIUS Settings, select RadSec and then AGNI for the Authentication and Accounting Servers, and select Send DHCP Options and HTTP User Agent.

![image14](images/image14.png)

Confirm the Username and Password, Called Station, COA information.

![image15](images/image15.png)
![image16](images/image16.png)

Finally, Save and turn on the SSID.

![image17](images/image17.png)
![image18](images/image18.png)

Please Read!

Only select the “5 GHz” option on the next screen (uncheck the 2.4 GHz box if it’s checked), then click “Turn SSID On”.

---

### 2. Create UPSK Network and Segment:

Return to the LaunchPad tab, and select the AGNI tile, or go to your AGNI tab in your browser.

![image19](images/image19.png)

Click on Networks and then + Add.

![image20](images/image20.png)
![image21](images/image21.png)

Add the following:

Name: Wireless-UPSK  
Connection Type: Wireless  
SSID: ATD-##-UPSK  
Authentication Type: Unique PSK (UPSK)

Add Network

![image22](images/image22.png)

You should now see this listed in your networks.

![image23](images/image23.png)

Next, we will add the Segment.

Under Access Control, click on Segments and then + Add

![image24](images/image24.png)
![image25](images/image25.png)

Name: Wireless-UPSK  
Description: Wireless-UPSK

Click on + Add Condition

![image26](images/image26.png)

Conditions: Network:Authentication Type is UPSK

*Note: Conditions are always Matches ALL.

![image27](images/image27.png)
![image28](images/image28.png)
![image29](images/image29.png)
![image30](images/image30.png)
![image31](images/image31.png)
Click on + Add Action

![image32](images/image32.png)

Actions: Allow Access

![image33](images/image33.png)
![image34](images/image34.png)
![image35](images/image35.png)

Finally, click on Add Segment.

You should now see Wireless-UPSK in the list of segments.

![image36](images/image36.png)

---

### 3. Create an AGNI Local User and Enroll Personal Device

In this section you will create a local user and enroll the MAC of your device.

In AGNI, under Identity, click on User and then + Add User.

![image37](images/image37.png)
![image38](images/image38.png)
Fill out the sections.  Use Arista01! for the password.

Disable - User must change password at next login:

![image39](images/image39.png)
![image40](images/image40.png)
Click Add User

NOTE: You will notice that Password has now changed to UPSK Passphrase

Copy and write down or save to text file the new UPSK Passphrase.

![image41](images/image41.png)

Next, connect your client to ATD-##-UPSK using your UPSK Passphrase.

Click on Sessions and validate your device connection.

![image42](images/image42.png)
![image43](images/image43.png)

Next, validate your device by clicking on User and then Users.  Select your user.

![image44](images/image44.png)

Click on Show Clients

![image46](images/image46.png)

---

### 4. Create an AGNI Client Group

In this section, you will simulate your device as an IoT device.

Disable and forget previously saved lab networks so your wireless connection on your test device does not auto connect.  Under your user client list, delete your device.

![image47](images/image47.png)
![image48](images/image48.png)
![image49](images/image49.png)

Next, you will add your client device as an IoT device in a Client Group.

First, we will need to create the Client Group.

In AGNI, under Identity, click on Client Groups and then + Add.

![image50](images/image50.png)
![image51](images/image51.png)

Name: Corp Approved Devices  
Description: Corp Approved Devices  
User Association: Not user associated  

Enable the Group UPSK.  Copy the UPSK Passphrase

Then click on Add Group

![image52](images/image52.png)
![image53](images/image53.png)

Next, connect your client to ATD-##-UPSK using the Client Group UPSK Passphrase.

Click on Sessions and validate your device connection.

![image54](images/image54.png)
![image55](images/image55.png)

Next Click on your Client.

![image56](images/image56.png))
![image57](images/image57.png)

Notice your Client Group.  Here you have the option to change the Client Group your device belongs to.

![image58](images/image58.png)

Next, delete your device from the Client Group - Corp Approved Devices.

![image59](images/image59.png)
![image60](images/image60.png)

Next, under Identity, click on Clients and then + Add Client.

![image61](images/image61.png)
![image62](images/image62.png)

Select the Client Group: Corp Approved Devices

Add in the MAC Address of your test device like your phone that is not randomized.

Then select Add Client

![image63](images/image63.png)

You will then see the Client added to the Group.

![image64](images/image64.png)

Validate and Verify your connection using the Client Group UPSK Passphrase.

![image65](images/image65.png)
![image66](images/image66.png)
---

NAC LAB #2 COMPLETE
