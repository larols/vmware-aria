# You running this script/function means you will not blame the author(s) if this breaks your stuff.
# This script/function is provided AS IS without warranty of any kind.
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.

import requests


def handler(context, inputs):
    nsxuser = context.getSecret(inputs['nsxuser'])
    nsxpassword = context.getSecret(inputs['nsxpassword'])
    deploymentname = str(inputs["deploymentName"])
    nsxmanager = "172.16.252.147:888"

    headers = {'content-type': 'application/json'}

    # Remove rule from Isolate Deployments policy
    url = f'https://{nsxmanager}/policy/api/v1/infra/domains/default/security-policies/Isolate_deployments/rules/{deploymentname}'
    try:
        resp = requests.delete(url=url, headers=headers, auth=(nsxuser, nsxpassword), verify=False)
        resp.raise_for_status()
        print(f"Removed rule {deploymentname} from Isolate Deployments policy")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Remove group in NSX
    url = f'https://{nsxmanager}/policy/api/v1/infra/domains/default/groups/{deploymentname}'
    try:
        resp = requests.delete(url=url, headers=headers, auth=(nsxuser, nsxpassword), verify=False)
        resp.raise_for_status()
        print(f"Deleted the {deploymentname} NSX group")
    except Exception as e:
        print(f"Error: {e}")
        return
