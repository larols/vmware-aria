# You running this script/function means you will not blame the author(s) if this breaks your stuff. 
# This script/function is provided AS IS without warranty of any kind. Author(s) disclaim all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. 
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.

import requests
import requests.packages,urllib3
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def handler(context, inputs):
    #Secret Cloud Assembly properties - https://docs.vmware.com/en/vRealize-Automation/8.10/Using-and-Managing-Cloud-Assembly/GUID-895A8127-CC67-4A53-B633-879F373E7606.html
    nsxuser = context.getSecret(inputs['nsxuser'])
    nsxpassword = context.getSecret(inputs['nsxpassword'])
    deploymentName = str(inputs["deploymentName"])
    nsxmanager = "YOUR NSX MANAGER IP"

    # Remove rule from Isolate Deployments policy
    headers = {'content-type': 'application/json'}
    url = 'https://172.16.252.147:888/policy/api/v1/infra/domains/default/security-policies/Isolate_deployments/rules/'+deploymentName+''
    resp = requests.delete(url=url,headers=headers,auth=(nsxuser,nsxpassword),verify=False)
    response = resp.content
    if resp.status_code == 200:
        print ("Removed rule from Isolate Deployments policy")
    else:
        print (response)
        sys.exit()    
  
    # Remove group in NSX 
    url = 'https://'+nsxmanager+'/policy/api/v1/infra/domains/default/groups/'+deploymentName+''
    resp = requests.delete(url=url,headers=headers,auth=(nsxuser,nsxpassword),verify=False)
    response = resp.content
    if resp.status_code == 200:
        print ("Removed the NSX group")
    else:
        print (response)
    sys.exit()
        
        