#WORK IN PROGRESS - Do not expect this script to work :)

# You running this script/function means you will not blame the author(s) if this breaks your stuff.
# This script/function is provided AS IS without warranty of any kind.
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.

import requests
import json
import time

newTag = "web"


def handler(context, inputs):
    bearer_token = vraauth(inputs)
    existingTags = get_existing_tags(bearer_token, inputs)
    newTags = update_existingTags_with_newTag(existingTags, inputs)
    post_updated_tags_to_resource(bearer_token, newTags, inputs)


# post the new set of tags to the resourceId
def post_updated_tags_to_resource(bearer_token, newTags, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
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
        for i in range(3):
            resp = session.post(f"{url}/deployment/api/deployments/{deploymentId}/resources/{resourceId}/requests",
                                data=json_data, headers=vraheaders, verify=False)
            if resp.status_code == 409:
                time.sleep(15)
                continue
            resp.raise_for_status()
            json_data = resp.json()
            break


# updating service key(s) with new tag value(s)
def update_existingTags_with_newTag(existingTags, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
    existingTags = [d for d in existingTags if d.get('key') != 'service']
    new_services = newTag.split(", ")
    for i, service in enumerate(new_services):
        existingTags.append({'key': f'service', 'value': service})
    newTags = existingTags
    return (newTags)


# get the existing tags for resourceId
def get_existing_tags(bearer_token, inputs):
    deploymentId = inputs['__metadata_deploymentId']
    resourceId = inputs['__metadata_resourceProperties']['resourceId']
    url = inputs["vra_url"]
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

