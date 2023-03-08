# You running this script/function means you will not blame the author(s) if this breaks your stuff.
# This script/function is provided AS IS without warranty of any kind.
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.


import requests
import json
import time

bearer_token = None

def handler(context, inputs):
    global bearer_token
    bearer_token = vraauth(inputs)
    internetexit(bearer_token, inputs)
    existingTags = get_existing_tags(bearer_token, inputs)
    newTags = update_existingTags_with_newTag(existingTags, inputs)
    nsx_policy_update(inputs)
    if inputs["newTag"] == "internet":
        nsx_policy_update(inputs)
    post_updated_tags_to_resource(bearer_token, newTags, inputs)

# Create NSX FW rule in Isolate Deployments policy that blocks deployment from accessing RFC1918 when ingress policy is changed to internet
def nsx_policy_update(inputs):
    nsxmanager = inputs["nsxmanager"]
    nsxuser = inputs["nsxuser"]
    nsxpassword = inputs["nsxpassword"]
    deploymentname = get_deploymentname(bearer_token, inputs)
    url = f'https://{nsxmanager}/policy/api/v1/infra'
    headers = {'content-type': 'application/json'}
    data = { "resource_type": "Infra", "children": [ { "resource_type": "ChildDomain", "Domain": { "id": "default", "resource_type": "Domain", "children": [ { "resource_type": "ChildSecurityPolicy", "marked_for_delete": "false", "SecurityPolicy": { "id": "Isolate_deployments", "display_name": "Isolate Deployments", "resource_type": "SecurityPolicy", "category": "Environment", "sequence_number": 98, "rules": [ { "resource_type": "Rule", "display_name": f"{deploymentname}_Isolate_out", "sources_excluded": "false", "source_groups": [ f"/infra/domains/default/groups/{deploymentname}" ], "destinations_excluded": "true", "destination_groups": [ f"/infra/domains/default/groups/Local_Subnets" ], "services": [ "ANY" ], "action": "ALLOW", "direction": "OUT", "scope": [ f"/infra/domains/default/groups/{deploymentname}" ] } ] } } ] } } ] }
    try:
        resp = requests.patch(url=url, data=json.dumps(data), headers=headers, auth=(nsxuser, nsxpassword), verify=False)
        resp.raise_for_status()
        print (f"Ingress policy set to internet so adding rule in Isolate Deployment policy called {deploymentname}_Isolate_out")
    except Exception as e:
        print(f"Error: {e}")
        return

# Get deploymentname from __metadata_deploymentId to be used in nsx_policy_update
def get_deploymentname(bearer_token, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    url = inputs["vra_url"]
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    with requests.Session() as session:
        resp = session.get(f"{url}/deployment/api/deployments/{deploymentId}", headers=vraheaders, verify=False)
        resp.raise_for_status()
        json_data = resp.json()
        deploymentname = json_data["name"]
        return deploymentname

# post the new set of tags to the resourceId
def post_updated_tags_to_resource(bearer_token, newTags, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
    newTag = inputs["newTag"]
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    # parse and prepare json_data
    json_data = json.dumps({
        "actionId": "Cloud.vSphere.Machine.Update.Tags",
        "inputs": {
            "tags": newTags
        },
        "reason": "update tags"
    })
    # post new tags to resourceId
    with requests.Session() as session:
        for i in range(5):
            resp = session.post(f"{url}/deployment/api/deployments/{deploymentId}/resources/{resourceId}/requests",
                                data=json_data, headers=vraheaders, verify=False)
            if resp.status_code == 409:
                time.sleep(15)
                continue
            resp.raise_for_status()
            json_data = resp.json()
            break

# updating ingress key(s) with new tag value(s)
def update_existingTags_with_newTag(existingTags, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
    newTag = inputs["newTag"]
    existingTags = [d for d in existingTags if d.get('key') != 'ingress']
    existingTags.append({'key': 'ingress', 'value': newTag})
    newTags = existingTags
    print(f"New set of tags for {resourceId} will be: {existingTags}")
    return (newTags)

# get the existing tags for resourceId
def get_existing_tags(bearer_token, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
    newTag = inputs["newTag"]
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    with requests.Session() as session:
        resp = session.get(f"{url}/deployment/api/resources/{resourceId}", headers=vraheaders, verify=False)
        resp.raise_for_status()
        json_data = resp.json()
        existingTags = json_data["properties"]["tags"]
        print(f"Current set of tags for {resourceId} are: {existingTags}")
        return existingTags


# Make sure we are not trying to change ingress policy from internet to something else
def internetexit(bearer_token, inputs):
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
    newTag = inputs["newTag"]
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    with requests.Session() as session:
        resp = session.get(f"{url}/deployment/api/resources/{resourceId}", headers=vraheaders, verify=False)
        resp.raise_for_status()
        data = resp.json()
        for tag in data['properties']['tags']:
            if tag['key'] == 'ingress' and tag['value'] == 'internet':
                raise Exception(f"Error: Changing from ingress policy internet to {newTag} is not allowed.")


# get bearer_token for vRA Api
def vraauth(inputs):
    url = inputs["vra_url"]
    vralogin = {
        "username": inputs["vra_username"],
        "password": inputs["vra_password"],
        "domain": inputs['vra_domain']
    }
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    with requests.Session() as session:
        resp = session.post(f"{url}/csp/gateway/am/api/login?access_token", json=vralogin, headers=vraheaders,
                            verify=False)
        resp.raise_for_status()
        refresh_token = {"refreshToken": resp.json()['refresh_token']}
        resp = session.post(f"{url}/iaas/api/login", json=refresh_token, headers=vraheaders, verify=False)
        resp.raise_for_status()
        bearer_token = resp.json()['token']
        return bearer_token

