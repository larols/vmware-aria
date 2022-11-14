![image-20221114161451571](./assets/image-20221114161451571.png)



Click Infrastructure tab.

![image-20221114161520199](./assets/image-20221114161520199.png)

Click Continue and then scroll down in the menu to your left and click Cloud Accounts. Choose vCenter Server.

![image-20221114161623186](./assets/image-20221114161623186.png)

Click New Cloud Account and enter a name, vCenter FQDN and the username and password to be used for connecting to your vCenter Server. Click Validate. If Validate is successful continue and mark "Allow provisioning to these datacenters." Click ADD.

![image-20221114161733521](./assets/image-20221114161733521.png)

Time to create a project. Go to Infrastructure - Project. Click New Project. Give your project a name and click CREATE.

![image-20221114161902839](./assets/image-20221114161902839.png)

Go to the tab Users and click ADD USERS. 

![image-20221114161936960](./assets/image-20221114161936960.png)

Search for the user you created during step 10 in the [initial deployment](./deployment.md).

![image-20221114162019778](./assets/image-20221114162019778.png)



![image-20221114162050907](./assets/image-20221114162050907.png)



![image-20221114162115323](./assets/image-20221114162115323.png)

Scroll down and enter MFP-${###} in the Custom Nameing field.

![image-20221114180830306](./assets/image-20221114180830306.png)

![image-20221114162331501](./assets/image-20221114162331501.png)



![image-20221114162644549](./assets/image-20221114162644549.png)



![image-20221114162926021](./assets/image-20221114162926021.png)



![image-20221114162958833](./assets/image-20221114162958833.png)



[Code example](https://github.com/larols/vmware-aria/blob/main/aria-automation/Windows%202019.yaml)

![image-20221114173200042](./assets/image-20221114173200042.png)



![image-20221114175545096](./assets/image-20221114175545096.png)

![image-20221114180141082](./assets/image-20221114180141082.png)





