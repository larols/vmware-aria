# You running this script/function means you will not blame the author(s) if this breaks your stuff.
# This script/function is provided AS IS without warranty of any kind.
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.

import json
import requests

def handler(context, inputs):
    nsxuser = context.getSecret(inputs['nsxuser'])
    nsxpassword = context.getSecret(inputs['nsxpassword'])
    deploymentname = str(inputs["deploymentName"])
    nsxmanager = "YOUR NSX MANAGER IP"

    headers = {'content-type': 'application/json'}

    # Creating new group in NSX
    url = f'https://{nsxmanager}/policy/api/v1/infra/domains/default/groups/{deploymentname}'
    data = {"expression" : [ {"member_type": "VirtualMachine","key": "Tag","operator": "EQUALS","scope_operator": "EQUALS","value": f"deploymentname|{deploymentname}","resource_type": "Condition"} ],"resource_type" : "Group","display_name" : f"{deploymentname}","description" : "Automatically created using vRA","_system_owned" : "false","_protection" : "NOT_PROTECTED","_revision" : 0}
    try:
        resp = requests.patch(url=url,data=json.dumps(data),headers=headers,auth=(nsxuser,nsxpassword),verify=False)
        resp.raise_for_status()
        print ("Created new NSX group")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Updating Isolate Deployment policy with the new deployment rule
    url = f'https://{nsxmanager}/policy/api/v1/infra'
    data = { "resource_type": "Infra", "children": [ { "resource_type": "ChildDomain", "Domain": { "id": "default", "resource_type": "Domain", "children": [ { "resource_type": "ChildSecurityPolicy", "marked_for_delete": "false", "SecurityPolicy": { "id": "Isolate_deployments", "display_name": "Isolate Deployments", "resource_type": "SecurityPolicy", "category": "Environment", "sequence_number": 99, "rules": [ { "resource_type": "Rule", "display_name": f"{deploymentname}", "sources_excluded": "true", "source_groups": [ f"/infra/domains/default/groups/{deploymentname}" ], "destination_groups": [ f"/infra/domains/default/groups/{deploymentname}" ], "services": [ "ANY" ], "action": "DROP", "scope": [ f"/infra/domains/default/groups/{deploymentname}" ] } ] } } ] } } ] }
    try:
        resp = requests.patch(url=url,data=json.dumps(data),headers=headers,auth=(nsxuser,nsxpassword),verify=False)
        resp.raise_for_status()
        print ("Updated Isolate Deployment policy with the new deployment")
    except Exception as e:
        print(f"Error: {e}")
        return