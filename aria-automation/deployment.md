Download and mount VMware vRealize Suite Lifecycle Manager Easy Installer for vRA. This ISO package contains vRealize Automation, VMware Identity Manager and vRealize Suite Lifecycle Manager. 

![image-20221114134437580.png](./assets/images/deployment/image-20221114134437580.png)

The vRealize Easy Installer helps you install vRealize Automation and VMware Identity Manager in less time than it would take to install individual products. 

![image-20221114141744010.png](./assets/images/deployment/image-20221114141744010.png)

EULA and CEIP.

![image-20221114142634759](./assets/images/deployment/image-20221114142634759.png)

Specify the vCenter Server details.

![image-20221114145546861](./assets/images/deployment/image-20221114145546861-1668434154722-10.png)

If your SSL certificate is untrusted you will get a warning.

![image-20221114145614545](./assets/images/deployment/image-20221114145614545.png)

Select a Location for the virtual appliances.

![image-20221114145653462](./assets/images/deployment/image-20221114145653462-1668434217247-12.png)

Select a compute resource to deploy the virtual appliances.

![image-20221114145724643](./assets/images/deployment/image-20221114145724643-1668434245909-14.png)

Select a Storage Location.

![image-20221114145804917](./assets/images/deployment/image-20221114145804917-1668434290951-16.png)

Network Configuration.

![image-20221114150000257](./assets/images/deployment/image-20221114150000257.png)

Password Configuration (initial setup account will be created in step 10.)

![image-20221114150023388](./assets/images/deployment/image-20221114150023388-1668434425579-18-1668434429391-20.png)

Lifecycle Manager Configuration.

![image-20221114150738623](./assets/images/deployment/image-20221114150738623.png)



Identity Manager Configuration. The Default Configuration Admin you create in this step will later be used to do the initial configuration of vRA and vIDM.

![image-20221114150839061](./assets/images/deployment/image-20221114150839061.png)

Aria Automation Configuration. I'm choosing a Standard one node deployment to keep it simple in my lab.

![image-20221114150953057](./assets/images/deployment/image-20221114150953057.png)

Make sure all your values are correct and hit SUBMIT.

![image-20221114151103964](./assets/images/deployment/image-20221114151103964.png)

