![image-20221118003043088](./assets/images/subscriptions/image-20221118003043088.png)

![image-20221118003120924](./assets/images/subscriptions/image-20221118003120924.png)

Update your yaml code so it looks like this,

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

