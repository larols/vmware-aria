import json
import requests


def handler(context, inputs):
    ingress_policy = inputs["ingress_policy"]
    actual_name = inputs["actual_name"]
    deployment_id = inputs["deployment_id"]

    if ingress_policy != "internet":
        # Run validation if ingress_policy is not "internet"
        global bearer_token
        bearer_token = vraauth(inputs)
        resource_ids = getresourceid(bearer_token, inputs)
        internet_resource_ids = []
        for resource_id in resource_ids:
            if not internetexit(bearer_token, resource_id):
                internet_resource_ids.append(resource_id)
        if internet_resource_ids:
            return "Cannot change ingress policy for resources with IDs {}: when ingress policy is set to 'internet'".format(
                ", ".join(internet_resource_ids))
    else:
        # Do something if ingress_policy is "internet"
        return ""


# Make sure we are not trying to change ingress policy from internet to something else
def internetexit(bearer_token, resource_id):
    url = "VRA URL"
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    with requests.Session() as session:
        resp = session.get(f"{url}/deployment/api/resources/{resource_id}", headers=vraheaders, verify=False)
        resp.raise_for_status()
        data = resp.json()
        print(data)
        for tag in data['properties']['tags']:
            if tag['key'] == 'ingress' and tag['value'] == 'internet':
                return False
    return True


# Get the resource ids using actual names of the virtual machines
def getresourceid(bearer_token, inputs):
    deployment_id = inputs["deployment_id"]
    actual_name = inputs["actual_name"]
    url = "https://xint-vra01.vmlab.se"
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    with requests.Session() as session:
        resp = session.get(f"{url}/deployment/api/deployments/{deployment_id}/resources", headers=vraheaders,
                           verify=False)
        resp.raise_for_status()
        data = resp.json()

        # Filter content list for elements with type "Cloud.vSphere.Machine"
        machine_elements = [elem for elem in data['content'] if elem['type'] == 'Cloud.vSphere.Machine']

        # Extract the "id" fields of the filtered elements
        resource_ids = [elem['id'] for elem in machine_elements]
        internet_resource_ids = []
        for resource_id in resource_ids:
            if not internetexit(bearer_token, resource_id):
                internet_resource_ids.append(resource_id)
        return internet_resource_ids or []


# get bearer_token for vRA Api
def vraauth(inputs):
    url = "VRA URL"
    vralogin = {
        "username": "USERNAME",
        "password": "PASSWORD",
        "domain": "DOMAIN"
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

