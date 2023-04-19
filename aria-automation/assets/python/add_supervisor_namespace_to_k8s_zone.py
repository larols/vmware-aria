import requests
import json

# Set vra_url as a global variable
vra_url = "https://vra_fqdn"
k8s_zone_id = "9c75b67a-ea18-45bf-b0bc-17e237cddab0" #K8s zone id - You can grab it from the URL when editing the k8s zone in Cloud assembly. "/automation-ui/#/provisioning-ui;ash=%2Fcmx%2FkubernetesZones%2Fedit%2F9c75b67a-ea18-45bf-b0bc-17e237cddab0"


# get bearer_token for vRA Api
def vraauth(inputs):
    vralogin = {
       "username": "username",
        "password": "password",
        "domain": "domain"
    }
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    with requests.Session() as session:
        resp = session.post(f"{vra_url}/csp/gateway/am/api/login?access_token", json=vralogin, headers=vraheaders, verify=False)
        resp.raise_for_status()
        refresh_token = {"refreshToken": resp.json()['refresh_token']}
        resp = session.post(f"{vra_url}/iaas/api/login", json=refresh_token, headers=vraheaders, verify=False)
        resp.raise_for_status()
        bearer_token = resp.json()['token']
        return bearer_token


# Update K8s zone with newly created supervisor namespace
def update_k8s_zone(context, inputs):
    token = vraauth(inputs)
    target_id = inputs['__metadata']['targetId']

    # Get the existing k8s zone
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{vra_url}/cmx/api/resources/k8s-zones/{k8s_zone_id}", headers=headers, verify=False)
    response.raise_for_status()
    k8s_zone = response.json()

    # Add the new supervisor namespace to the existing list
    new_namespace = {"namespaceSelfLinkId": target_id}
    k8s_zone["supervisorNamespaces"].append(new_namespace)
    print(k8s_zone)
    # PUT the updated k8s zone
    response = requests.put(f"{vra_url}/cmx/api/resources/k8s-zones/{k8s_zone_id}", headers=headers, json=k8s_zone, verify=False)
    response.raise_for_status()
    return response.json()
