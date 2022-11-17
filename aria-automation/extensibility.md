Go to Cloud Assembly.

![image-20221117101335742](./assets/images/extensibility/image-20221117101335742.png)

Navigate to Extensibility - Library - Actions and click NEW ACTION.

![image-20221117101356693](./assets/images/extensibility/image-20221117101356693.png)

Give it a name and choose your project.

![image-20221117101412656](./assets/images/extensibility/image-20221117101412656.png)

Pick your scripting language of choice. Here's an Python based example. Verify you have a Default input named target with value World.

```
def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
```

Hit Save and then Create Version

![image-20221117101452533](./assets/images/extensibility/image-20221117101452533.png)

Give it a version number and click CREATE.

![image-20221117101541526](./assets/images/extensibility/image-20221117101541526.png)

Click versions in upper right hand corner.

![image-20221117101559200](./assets/images/extensibility/image-20221117101559200.png)

Click RELEASE.

![image-20221117101615956](./assets/images/extensibility/image-20221117101615956.png)

Again click RELEASE.

![image-20221117101724988](./assets/images/extensibility/image-20221117101724988.png)

Go to Service Broker to update your content sources.

![image-20221117101738041](./assets/images/extensibility/image-20221117101738041.png)

Create another content source.

![image-20221117101749172](./assets/images/extensibility/image-20221117101749172.png)

Pick Extensibility actions.

![image-20221117101851034](./assets/images/extensibility/image-20221117101851034.png)

Give it a name and choose your source project.

![image-20221117101832381](./assets/images/extensibility/image-20221117101832381.png)

Go to Policies - Definitions. Click on your already existing Definition.

![image-20221117102001115](./assets/images/extensibility/image-20221117102001115.png)

Click ADD ITEMS.

![image-20221117102013343](./assets/images/extensibility/image-20221117102013343.png)

Add Extensibility actions and hit save.

![image-20221117102024323](./assets/images/extensibility/image-20221117102024323.png)

Your newly created action should now be available in the catalog. You can try it out by clicking REQUEST.

![image-20221117102109443](./assets/images/extensibility/image-20221117102109443.png)

Enter a deployment name and click SUBMIT.

![image-20221117102136750](./assets/images/extensibility/image-20221117102136750.png)

Deployment running.

![image-20221117102155148](./assets/images/extensibility/image-20221117102155148.png)

When finished you can view the output from the script.

![image-20221117102220284](./assets/images/extensibility/image-20221117102220284.png)

