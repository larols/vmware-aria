![image-20221118003043088](./assets/images/subscriptions/image-20221118003043088.png)

![image-20221118003120924](./assets/images/subscriptions/image-20221118003120924.png)

Update your yaml code so it looks like [this](https://github.com/larols/vmware-aria/blob/main/aria-automation/assets/yaml/Rename%20VM.yaml). This will ask the user to input a name for the VM.

```
formatVersion: 1
inputs:
  hostname:
    type: string
    title: Input VM Name
    description: Name of your VM
resources:
  Cloud_vSphere_Machine_1:
    type: Cloud.vSphere.Machine
    properties:
      image: windows2019
      flavor: small
      newName: ${input.hostname}
```

You can hit TEST to verify this works.

![image-20221118003332714](./assets/images/subscriptions/image-20221118003332714.png)

Lastly before hitting CLOSE. Record the Cloud Template ID from the URL. In my case the url is,

```
https://vra-fqdn/automation-ui/#/blueprint-ui;ash=%2Fblueprint%2Fedit%2Fb566ff96-8984-4054-883d-f4cf13211ea5
```

And the ID that I'm interested in keeping from the URL is,

```
b566ff96-8984-4054-883d-f4cf13211ea5
```

We will use this later.

![image-20221118005025550](./assets/images/subscriptions/image-20221118005025550.png)



![image-20221118003353517](./assets/images/subscriptions/image-20221118003353517.png)

![image-20221118003411353](./assets/images/subscriptions/image-20221118003411353.png)

Select your scripting language of choice. In the example below I'm using Python. Click LOAD TEMPLATE and choose Rename VM. Hit LOAD.

![image-20221118003518386](./assets/images/subscriptions/image-20221118003518386.png)

First off I will remove the two Default inputs that comes with the template. Thereafter you can change the FaaS provider to On Prem. Lastly modify the python script so that the new_name will be based on the customProperties from the Cloud Template. 

```
new_name = inputs["newName"] will be changed to new_name = inputs["customProperties"]["newName"]
```

Your script should then look like [this](https://github.com/larols/vmware-aria/blob/main/aria-automation/assets/python/RenameVM.py),

```
def handler(context, inputs):
    """Set a name for a machine
    :param inputs
    :param inputs.resourceNames: Contains the original name of the machine.
           It is supplied from the event data during actual provisioning
           or from user input for testing purposes.
    :param inputs.newName: The new machine name to be set.
    :return The desired machine name.
    """
    old_name = inputs["resourceNames"][0]
    new_name = inputs["customProperties"]["newName"]

    outputs = {}
    outputs["resourceNames"] = inputs["resourceNames"]
    outputs["resourceNames"][0] = new_name

    print("Setting machine name from {0} to {1}".format(old_name, new_name))

    return outputs
```

Save and Close your script.

![image-20221118004405671](./assets/images/subscriptions/image-20221118004405671.png)

Lastly we need to create a subscription. Go to Extensibility - Subscriptions and click NEW SUBSCRIPTION. 

Give the subscription a name. Choose the Event Topic Compute Allocation. And set Action/Workflow to your newly created Action Rename VM.

Enable Condition 'Filter event in topic' and add *event.data.blueprintId ==''* together with the cloud template ID that you recorded earlier in between the ''. In my case it will looks like this,

```
event.data.blueprintId =='b566ff96-8984-4054-883d-f4cf13211ea5'
```

This will make sure this subscription only runs for this specific cloud template. Hit SAVE.

![image-20221118005415497](./assets/images/subscriptions/image-20221118005415497.png)

Your subscription is created and enabled.

![image-20221118005648357](./assets/images/subscriptions/image-20221118005648357.png)

Go back to the design tab. Select your Rename VM Cloud Template and click DEPLOY.

![image-20221118005751811](./assets/images/subscriptions/image-20221118005751811.png)

Give the deployment a name. Click NEXT.

![image-20221118010219300](./assets/images/subscriptions/image-20221118010219300.png)

Give the VM a name and click DEPLOY.

![image-20221118010242850](./assets/images/subscriptions/image-20221118010242850.png)

Deployment is running. You can see the old name togehter with the new name in Custom Properties.

![image-20221118010547833](./assets/images/subscriptions/image-20221118010547833.png)

You can also see the Action being triggered in Extensibility - Actions Runs.

![image-20221118010357531](./assets/images/subscriptions/image-20221118010357531.png)

When the creation is completed your new VM will be name accordingly to your custom input. 

![image-20221118010723879](./assets/images/subscriptions/image-20221118010723879.png)

To publish this to the Service Broker Catalog you need to create a version of the Cloud Template and Release it to the Catalog.

![image-20221118010936601](./assets/images/subscriptions/image-20221118010936601.png)

It will be added automatically to Service Broker after some time if you follow the steps in [Service Broker Content Sharing Policy](/aria-automation/servicebroker.md). You can also force it by going to Service Broker - Content and Policies - Content Sources - Edit your Cloud Template content source and click SAVE & IMPORT.

![image-20221118011038572](./assets/images/subscriptions/image-20221118011038572.png)