# Campus A-03 Wired Lab Guide

## Day-2 Operations, Dashboards, and Events

![CloudVision](images/cv-logo.png)

This Lab Guide:

https://github.com/arista-rockies/Workshops/tree/main/Campus

---

## Table of Contents

Full Lab Topology  
POD Topology  
1. Accessing CloudVision as a Service  
2. Operations: Add a VLAN  
3. Rollback a Change Control  
4. Dashboards (Built-in and Custom)  
5. Events  
6. Customize Notifications  

---

## Full Lab Topology

![Full Lab Topology](images/full-lab-topology.png)

---

## POD Topology

![POD Topology](images/pod-lab-topology.png)

---

## Accessing CloudVision as a Service

In your Google Chrome browser, enter the following URL:  
https://www.arista.io/  
to access CloudVision as a Service (CVaaS).

1. In the “Organization” box enter the Organization name “rockies-training-##” where ## is a 2 digit character between 01-20 that was assigned to your lab/Pod, then click “Enter”.

![CVaaS Login Page](images/cvaas-login.png)


2. Click the Log in with Launchpad button and provide your assigned lab/Pod email address and password:


![Launchpad Login](images/launchpad-login.png)

3. You will now be logged into CloudVision

![CloudVision Dashboard](images/cloudvision-dashboard.png)

---

## Operations: Add a VLAN

Adding a VLAN is a common provisioning task. Let’s use the existing Campus Fabric Studio to add an incremental configuration (add a VLAN). This VLAN will be specific to your pod and not routable outside.

* Select Provisioning, then Studios

![Provisioning Studios](images/provisioning-studios.png)

* Create a new Workspace and name it similar to  “<add-vlan2##>” where ## is your pod number. Examples:

Pod 1 = VLAN 201  
Pod 2 = VLAN 202  
…  
Pod 13 = VLAN 213  
etc.

![Create Workspace](images/create-workspace.png)

* Once the workspace is created, open the existing Campus Fabric (L2/L3/EVPN) studio: (If the Studios main page is not present you may have to select the blue Studios breadcrumb towards the top left of the page)

![Campus Fabric Studio](images/campus-fabric-studio.png)

  * Within the Campus Fabric studio, validate that the Device Selection still applies to All Devices

![Device Selection All Devices](images/device-selection-all.png)

  * Within the Campus Services (Non-VXLAN) select the Campus:Workshop expand arrow button on the right

![Campus Services Expand](images/campus-services-expand.png)

* Add new VLAN and add to the “IT-Bldg” Campus POD.

  * Within the Campus: Workshop section, click the Campus-Pod: IT-Bldg name or the right arrow Expand button

![Campus Pod Expand](images/campus-pod-expand.png)

OR

  * click the Add VLAN button

![Add VLAN Button](images/add-vlan-button.png)

  * Once an entry is added for VLAN <2##>, click the right arrow Expand button

![Expand New VLAN](images/expand-new-vlan.png)

  * Customize the new VLAN by giving it a name

![Customize VLAN Name](images/customize-vlan-name.png)

  * Add the VLAN to the Access-Pod by clicking Add Pod and selecting IDF1

![Add Pod IDF1](images/add-pod-idf1.png)

You can skip entries for all of the remaining sections.

4. Review and Submit Workspace

  * Click “Review Workspace” to submit the staged changes.

![Review Workspace](images/review-workspace.png)

  * Notice that the Studio is adding the VLAN to all three devices within the Pod as well as adding the newly created VLAN to the trunk interfaces.

![Review Workspace2](images/review-workspace2.png)

  * Once you review the changes, click Submit Workspace

![Submit Workspace](images/submit-workspace.png)

  * Click View Change Control

![View Change Control](images/view-change-control.png)

  * Review the Change Control and select “Review and Approve”

![Review and Approve](images/review-and-approve.png)

  * If necessary toggle the Execute Immediately button and select Approve and Execute

![Approve and Execute](images/approve-and-execute.png)


* Verify the VLAN has been added to the device configuration by using the Devices Comparison function.

  * Select Devices then Comparison menu
  
 ![Navigate Comparison](images/navigate-comparison.png) 

  * Select a Time Comparison
  * Choose a device from the list. example leaf1a
  * Select a time period, for example 30 minutes ago 
  * Click the Compare button 

![Devices Comparison](images/devices-comparison.png)



  * The first screen presented shows the overview:
  * Select the Configuration section

![Comparison Overview](images/comparison-overview.png)


*Note: Notice that the configuration has been updated. Feel free to explore other comparisons by feature. Since this VLAN was localized only, no new IP routes or MAC addresses should be learned.*

![Config Comparison](images/config-comparison.png)

Lab section completed!

 In the next lab section you will see how to roll back a previous change control

---

## Rollback a Change Control

A common operational task is to roll back a specific configuration and restore back to previous state. You may need to do this for all devices affected by a change, or only a subset of devices under troubleshooting.

CloudVision change controls allow this flexibility for granular change management per device and fleet-wide

Let’s roll back the change control we used to add a VLAN via Studios.

  * First go to Provisioning then Change Control menu. Select the change control corresponding to your VLAN addition

![Select Change Control](images/select-change-control.png)

  * Click the Rollback button

![Rollback Button](images/rollback-button.png)

  * In the next screen, select the top list check mark to select all the devices and click Create Rollback Change Control

![Create Rollback Change Control](images/create-rollback-cc.png)

  * Verify the Configuration Changes section by clicking “View Diff”  Once you have reviewed the change, click the Review and Approve button

![View Diff](images/view-diff.png)

  * You’ll be presented with one more opportunity to review the changes. Select Execute Immediately if not already toggled on and Approve and Execute

![Execute Rollback](images/execute-rollback.png)

  *  Monitor the change control for completion to ensure the added VLAN is cleaned up on all three switches.

![Rollback Completed](images/rollback-completed.png)

You have now successfully added a VLAN through Studios and then rolled back that change across all switches.

---

## Dashboards (Built-in and Custom)

Dashboards are an important way to visualize commonly requested information. This lab section shows you how to navigate the built-in dashboards and customize your own.

### Built in Dashboard: “Campus Health Overview”

  * Open the Dashboards Section to arrive at the Dashboards landing page.

![Dashboards Landing Page](images/dashboards-landing.png)

  * Select the built-in Campus Health Overview dashboard

![Campus Health Overview](images/campus-health-overview1.png)

  * You’ll be presented with a curated selection of common campus related monitoring tools

![Campus Health Overview](images/campus-health-overview2.png)
*Note: We will explore the Quick Actions interactive functions of this dashboard in another lab section.* 

  * Feel free to explore the Campus Health dashboard briefly and then navigate back to the Dashboards landing page by selecting Dashboards in the upper left.

![Explore Dashboards](images/explore-dashboards.png)

### Built in Dashboard: “Device Hardware”

 * Next, Select the Device Hardware dashboard

![Device Hardware Dashboard](images/device-hardware-dashboard.png)

  * By default, this dashboard selects all devices. 
  
  ![Device Hardware Dashboard2](images/device-hardware-dashboard2.png)
  
  * Change the dashboard to select only leaf1c by deleting the current query device:*. Replace with the query device:campus-pod[pod#]leaf1c

![Device Query Edit](images/device-query-edit.png)

  * Once you’ve selected an individual device, the dashboard will filter to results for only this device.

![Dashboard Filter](images/dashboard-filter.png)

  * Navigate back to the Dashboards landing page by clicking Dashboards in upper left.

![Dashboard Navigate](images/dashboard-navigate.png)

---
 ### Customized dashboard.

  * Click the New Dashboard button.

![New Dashboard](images/new-dashboard.png)

  * Select the pencil next to Untitled dashboard
  * Provide a useful name for the Dashboard, such as “Workshop Dashboard” 

![Rename Dashboard](images/rename-dashboard.png)


  * Next, let’s add some metrics to display from the workshop devices.

![Change Metrics to Summaries](images/add-metrics.png)


  * Within new metrics tile now added to your dashboard, select either the 3 dots > Configure or **Click to Configure**

![Metrics Configure](images/metrics-configure.png)

  * Within the right side menu bar, locate the device metric **Memory > Memory Usage** 

![Metrics Configure](images/metrics-configure2.png)

  * Review the availabe Visualization options. Select each of them to determine which would best suite your personal preference.

*Note: sometimes when changing the visualization you will have to re-select the metric you would like displayed*

![Metrics Configure](images/metrics-visualization-table.png)

![Metrics Configure](images/metrics-visualization-bar.png)

![Metrics Configure](images/metrics-visualization-line.png)



* Create another metric by selecting Metrics to the right and configure the new dashboard tile.


![Metrics Configure](images/metrics-configure3.png)

* Within the Configure Metrics Panel menu, select the dropdown under Data Sources. Select Interfaces

![Metrics Configure](images/metrics-configure4.png)


* Under the available metrics scroll down and locate **Bitrate In** and **Bitrate Out**
* Under Dataset select **Ethernet16** on both **leaf1a and leaf1b**

![Metrics Configure](images/metrics-configure5.png)

* In the dashboard tile select the Pencil Icon and change the tile name to **Pod Uplinks Bitrate**
* Select the visualization style that you believe best displays this data

*Note: sometimes when changing the visualization you will have to re-select the metric you would like displayed*

![Metrics Configure](images/metrics-configure6.png)

   * Dismiss the customization menu with the X button in upper right

![Close Metrics](images/close-metrics.png)

*You can resize an individual tile by dragging the lower right corner. To move the tile location you can drab the op middle of the tile and re-locate it to it's desired location.*

*Take some time to explore additional dashboard tile options*

![Moving Tiles](images/moving-tiles.png)

    * When done save and complete the dashboard customization by clicking the Done button in upper menu bar


![Done Dashboard](images/done-dashboard.png)

### Exporting and Importing Dashboards Sharing your Dashboard across Cloudvision systems!

* In the upper right corner, select the **three-dots** menu and click Export as JSON
* Click Download in the lower right corner. This will download a file you can share with others.


![Export JSON](images/export-json.png)


* To demonstrate the ability to import a dashboard we will delete our custom dashboard
  * After exporting your dashboard in the previous step
  * Select the **Dashboard** breadcrumb at the top of the page
  * Select the Check Box next to the **Workshop Dashboard**
  * Select the **Delete**

![Delete Dashboard](images/del-dashboard.png)

* In the top corner select **Import**
* Click **Select File**
* Locate the dashboard downloaded to your local PC.
* Select **Upload**

![Import Dashboard](images/import-dashboard1.png)
* Review the Dashboard Name and the Status displays **Ready to Upload**
* Select **Import**
* Select **Finish**

![Import Dashboard](images/import-dashboard2.png)

Lab section completed!

---

## Events

In this section, we will explore the CloudVision Events. We will reivew the tools and filters to help process and manage critical errors versus informational data.

* First Open the Events section from the menu bar:

![Events Menu](images/events-menu.png)

* To filter only display more recent events, select the dropdown next to the displayed timeframe
* Select **1 Hour**
* You can select how the events are displayed in the menu by selecting the icon for either a **graphical view** or a **table view**

![Change Timeframe](images/change-timeframe.png)


* Focusing on the Event List next, Note the Export button to download the current Event list as CSV. Notice you can download All Events or only Selected:

![Export Events CSV](images/export-events-csv1.png)

* Select the Gear icon to toggle Event List **Roll Up**. *This setting combines repeated events into groups.* Toggle this On and Off, watch the effect this has on the list of Events.

![Event Rollup Toggle](images/event-rollup-toggle.png)

* Next, utilizing the Event Filters on the right you can reduce the amount of data displayed.

  * Ensure that only **Critical** and **Warning** are the only highlighted event severity by toggling off all other severity levels.
  * Select the dropdown under Type. Search for **Device Clock Out of Sync** and **Unexpected Link Failure**

*We are now only seeing events associated with the filter we have established*
![Severity Filter](images/severity-filter.png)

* Acknowledge and Unacknowledging events

  * Review the events displayed. You can acknoledge events by selecting the radial button nexto the the displayed event.
  * Select **Acknowledge X**
  * A pop up window will be displayed. You can **Acknowledge** these events and include a note to provide additional context on root cause or fix action.

![Acknowledge Events](images/acknowledge-events.png)



*  Acknowledged events are not deleted from the event list, only flagged as acknowledged and can be referenced by changing the filtered Acknowledgement State. Click Acknowledgement State and select Acknowledged

![Acknowledgement State](images/acknowledgement-state.png)

* You can also **Un-acknowledge** an event.
  * While reviewing the Acknowledged events, select the check box next to the events. 
  * Select **Unacknowledge X**
  * Select **Unacknowledge**

![Unacknowledge Events](images/unacknowledge-events.png)

**Events and filtering lab section complete!**



---

## Customize Notifications
In this section we will show you how to customize the notifications that can be generated (e.g. email, chat, SNMP, Syslog, etc) from the events.

### Configure “SendGrid” email service.

  * Navigate to the **Events** menu

![Events Menu](images/events-menu.png)

  * Select the **Configure** dropdown 
  * Select **Event Notifications** 

![Notifications Button](images/notifications-button.png)

* Select **Receivers**
* Select **+ Add Receiver**

![Add Receiver](images/add-receiver.png)

* Provide a name for the reciever Example: **SendGrid for Campus Workshop**
* Select **+Add Configuration**
* Select **SendGrid** from the list

![SendGrid Configuration](images/sendgrid-configuration.png)

* Provide your email address under **Recipient Email**
* Select **Save**

![SendGrid Configuration](images/sendgrid-configuration2.png)

* Configure Rules to identify what events are sent
  * Select **Rules** from the Menu
  * Select **+ Add Rule**

![Add Rule](images/add-rule.png)

 * Configure Rule Conditions
   * Select **+ Device**
   * under the dropdown select **leaf1a**

![Rule Device Selection](images/rule-device-selection.png)

  * Select **+ Event Type** 
    * Select Events **Change Control Created, Change Control Executed, Change Control Failed, Device Designed Configuration Changed, Change Control Succeeded, Device Clock Out of Sync, and Device Stopped Streamining** feel free to add additional event types
  * Under the dropdown for Receiver Select **SendGrid for Campus Workshop**

![Add Event Type](images/add-event-type.png)

Make sure to save your changes in this screen with the Save button along the top of your screen.

![Receiver Save Changes](images/receiver-save-changes.png)

Now test your new receiver and rule.

* Select **Status** on the left navigation pane
* Under Event Type locate **Device Stopped Streaming** in the dropdown
* Under Devic select **Leaf1a** from the dropdown
* Select **Send Test Notification**

![Test Notification Sender](images/test-notification-sender.png)

 * After a minute or two, you should receive the email alert at the email address you configured in the Receiver.

![Test Notification Email](images/test-notification-email.png)

Congratulations, you’ve completed the “Event Notification Lab” !

---

END OF LAB GUIDE
