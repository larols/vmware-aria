Tags are powerful metadata that you can associate with resources and include in templates. You can use tags in a variety of management scenarios, including workload placement and resource labeling.

![image-20221118111558010](./assets/images/tagging/image-20221118111558010.png)

![image-20221118111800454](./assets/images/tagging/image-20221118111800454.png)

![image-20221118111647508](./assets/images/tagging/image-20221118111647508.png)

```
formatVersion: 1
resources:
  Cloud_vSphere_Machine_1:
    type: Cloud.vSphere.Machine
    properties:
      image: windows2019
      flavor: small
      tags: 
        - key: os
          value: windows
```

![image-20221118112249728](./assets/images/tagging/image-20221118112249728.png)

Hit DEPLOY. Give your Deployment a name and deploy your template.

![image-20221118112736449](./assets/images/tagging/image-20221118112736449.png)

------

![image-20221118113123977](./assets/images/tagging/image-20221118113123977.png)

```
formatVersion: 1
resources:
  Cloud_vSphere_Machine_1:
    type: Cloud.vSphere.Machine
    properties:
      image: windows2019
      flavor: small
      tags: 
        - key: os
          value: windows
      constraints: 
        - tag: cz:development
```

![image-20221118113229155](./assets/images/tagging/image-20221118113229155.png)

![image-20221118113357178](./assets/images/tagging/image-20221118113357178.png)

Click on Provisioning diagram to see details.

![image-20221118113810943](./assets/images/tagging/image-20221118113810943.png)

![image-20221118113820064](./assets/images/tagging/image-20221118113820064.png)

I recommend reading this about tags: https://docs.vmware.com/en/vRealize-Automation/8.10/Using-and-Managing-Cloud-Assembly/GUID-2F1E458B-06B1-43F5-A730-714987CB9332.html