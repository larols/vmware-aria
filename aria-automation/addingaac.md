Before I started this I have downloaded VMware-vRealize-Automation-SaltStack-Config-8.10.1.0-20668427_OVF10.ova and placed a copy in /tmp on my vRSLCM node. If vRSLCM have internet access you can download it directly from within vRSLCM.

![image-20221118155001862](./assets/images/multivm/image-20221118155001862.png)

Locker.

![image-20221118155010612](./assets/images/multivm/image-20221118155010612.png)

Certificates - GENERATE.

![image-20221118162734529](./assets/images/multivm/image-20221118162734529.png)

![image-20221118162951095](./assets/images/multivm/image-20221118162951095.png)

Go to Lifecycle Operations.

![image-20221118163002897](./assets/images/multivm/image-20221118163002897.png)

Settings - Binary Mapping.

![image-20221118155741409](./assets/images/multivm/image-20221118155741409.png)

Click ADD BINARIES. Change Base Location to /tmp. Click DISCOVER. Select the SaltStack Config ova and click ADD.

![image-20221118160324044](./assets/images/multivm/image-20221118160324044.png)

Got to Environments. Click the three dots and choose Add Product.

![image-20221118163306903](./assets/images/multivm/image-20221118163306903.png)

VreAlize Automation SaltStack Config. New Install. Version. vRA-Integrated. Deployment Type: Standard. Click Next.

![image-20221118163344806](./assets/images/multivm/image-20221118163344806.png)

Add, Select and Validate your license. 

![image-20221118163741156](./assets/images/multivm/image-20221118163741156.png)

Select the Certificate you created earlier.

![image-20221118164024656](./assets/images/multivm/image-20221118164024656.png)

Select Cluster, Folder, Resource Pool, Network, Datastore. Enable Integrate with Identity Manager.

![image-20221118164111575](./assets/images/multivm/image-20221118164111575.png)

Network settings.

![image-20221118164121802](./assets/images/multivm/image-20221118164121802.png)

Check Integrate with Identity Manager.

![image-20221118164206344](./assets/images/multivm/image-20221118164206344.png)

Run Pre Check and verify everything is OK.

![image-20221118164328083](./assets/images/multivm/image-20221118164328083.png)

Submit.

![image-20221118164359757](./assets/images/multivm/image-20221118164359757.png)

Wait for installation to complete.

![image-20221118164814366](./assets/images/multivm/image-20221118164814366.png)













