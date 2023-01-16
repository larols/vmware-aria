# You running this script/function means you will not blame the author(s) if this breaks your stuff. 
# This script/function is provided AS IS without warranty of any kind.
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

    # Creating new group in NSX 
    headers = {'content-type': 'application/json'}
    url = 'https://'+nsxmanager+'/policy/api/v1/infra/domains/default/groups/'+deploymentName+''
    data = {"expression" : [ {"member_type": "VirtualMachine","key": "Tag","operator": "EQUALS","scope_operator": "EQUALS","value": "deploymentName|"+deploymentName+"","resource_type": "Condition"} ],"resource_type" : "Group","display_name" : ""+deploymentName+"","description" : "Automatically created using vRA","_system_owned" : "false","_protection" : "NOT_PROTECTED","_revision" : 0}
    resp = requests.patch(url=url,data=json.dumps(data),headers=headers,auth=(nsxuser,nsxpassword),verify=False)
    response = resp.content
    if resp.status_code == 200:
        print ("Created new NSX group")
    else:
        print (response)
        sys.exit()
        
    # Updating Isolate Deployment policy with the new deployment
    url = 'https://'+nsxmanager+'/policy/api/v1/infra'
    data = { "resource_type": "Infra", "children": [ { "resource_type": "ChildDomain", "Domain": { "id": "default", "resource_type": "Domain", "children": [ { "resource_type": "ChildSecurityPolicy", "marked_for_delete": "false", "SecurityPolicy": { "id": "Isolate_deployments", "display_name": "Isolate Deployments", "resource_type": "SecurityPolicy", "category": "Environment", "sequence_number": 99, "rules": [ { "resource_type": "Rule", "display_name": ""+deploymentName+"", "sources_excluded": "true", "source_groups": [ "/infra/domains/default/groups/"+deploymentName+"" ], "destination_groups": [ "/infra/domains/default/groups/"+deploymentName+"" ], "services": [ "ANY" ], "action": "DROP", "scope": [ "/infra/domains/default/groups/"+deploymentName+"" ] } ] } } ] } } ] }
    resp = requests.patch(url=url,data=json.dumps(data),headers=headers,auth=(nsxuser,nsxpassword),verify=False)
    response = resp.content
    if resp.status_code == 200:
        print ("Updated Isolate Deployment policy with the new deployment")
    else:
        print (response)
        sys.exit()