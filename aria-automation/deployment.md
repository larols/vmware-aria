#### To complete the setup you will need to prepare the following.

##### vCenter Server FQDN:

##### vCenter username with the [right permissions](https://docs.vmware.com/en/VMware-vRealize-Suite-Lifecycle-Manager/8.10/com.vmware.vrsuite.lcm.8.10.doc/GUID-AC013263-7003-402E-9A22-83BFFC4E6CAE.html) for vRSLCM to deploy the appliacnes to your vCenter server

##### Network segment where your appliances will get deployed:

##### Subnetmask:

##### Default gateway:

##### DNS Servers:

##### Domain Name:

##### NTP Server:

##### Lifecycle Manager;

- ##### Virtual Machine Name:

- ##### IP Address:

- ##### Hostname:

##### Identity Manager Configuration,

- ##### Virtual Machine Name:

- ##### IP Address:

- ##### Hostname:

##### vRealize Automation Configuration,

- ##### Virtual Machine Name:

- ##### IP Address:

- ##### Hostname:

- ##### License Key:



Download and mount VMware vRealize Suite Lifecycle Manager Easy Installer for vRA. This ISO package contains vRealize Automation, VMware Identity Manager and vRealize Suite Lifecycle Manager. 

![image-20221114134437580.png](./assets/image-20221114134437580.png)

The vRealize Easy Installer helps you install vRealize Automation and VMware Identity Manager in less time than it would take to install individual products. 

![image-20221114141744010.png](./assets/image-20221114141744010.png)

EULA and CEIP.

![image-20221114142634759](./assets/image-20221114142634759.png)

Specify the vCenter Server details.

![image-20221114145546861](./assets/image-20221114145546861-1668434154722-10.png)

If your SSL certificate is untrusted you will get a warning.

![image-20221114145614545](./assets/image-20221114145614545.png)

Select a Location for the virtual appliances.

![image-20221114145653462](./assets/image-20221114145653462-1668434217247-12.png)

Select a compute resource to deploy the virtual appliances.

![image-20221114145724643](./assets/image-20221114145724643-1668434245909-14.png)

Select a Storage Location.

![image-20221114145804917](./assets/image-20221114145804917-1668434290951-16.png)

Network Configuration.

![image-20221114150000257](./assets/image-20221114150000257.png)

Password Configuration (initial setup account will be created in step 10.)

![image-20221114150023388](./assets/image-20221114150023388-1668434425579-18-1668434429391-20.png)

Lifecycle Manager Configuration.

![image-20221114150738623](./assets/image-20221114150738623.png)



Identity Manager Configuration. The Default Configuration Admin you create in this step will later be used to do the initial configuration of vRA and vIDM.

![image-20221114150839061](./assets/image-20221114150839061.png)

Aria Automation Configuration. I'm choosing a Standard one node deployment to keep it simple in my lab.

![image-20221114150953057](./assets/image-20221114150953057.png)

Make sure all your values are correct and hit SUBMIT.

![image-20221114151103964](./assets/image-20221114151103964.png)

