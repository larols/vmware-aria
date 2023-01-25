#WORK IN PROGRESS - Do not expect this script to work :)

# You running this script/function means you will not blame the author(s) if this breaks your stuff.
# This script/function is provided AS IS without warranty of any kind.
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.

import requests
import json

# existingTags=inputs['existingTags']

# deploymentId = inputs['__metadata_deploymentId']
deploymentId = "6d6caf82-1e20-46af-a8a7-03dda1e52e59"
# resourceId = inputs['__metadata_resourceProperties']['resourceId']
resourceId = "358a6c31-89fc-416d-a30e-a73b72f91553"
# resourceName = inputs['__metadata_resourceProperties']['resourceName']
resourceName = "vSphere_Machine_1-mcm10596-222966367295"
newTag = "any"
url = "YOUR VRA IP"


def handler(context, inputs):
    bearer_token = vraauth(inputs)
    existingTags = get_existing_tags(bearer_token, inputs)
    print(f"Current set of tags for {resourceId} are: {existingTags}")
    newTags = update_existingTags_with_newTag(existingTags)
    print(f"New set of tags for {resourceId} will be: {newTags}")
    post_updated_tags_to_resource(bearer_token, newTags, inputs)


# post the new set of tags to the resourceId
def post_updated_tags_to_resource(bearer_token, newTags, inputs):
    vraheaders = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + bearer_token
    }
    # parsing data to prepare valid input
    prefix = '{"actionId":"Cloud.vSphere.Machine.Update.Tags","inputs":{"tags":'
    json_prefix = json.dumps(prefix)
    json_prefix = json_prefix[1:-1]
    while "\\" in json_prefix:
        json_prefix = json_prefix.replace("\\", "")

    suffix = '},"reason":"update tags"}'
    json_suffix = json.dumps(suffix)
    json_suffix = json_suffix[1:-1]
    while "\\" in json_suffix:
        json_suffix = json_suffix.replace("\\", "")

    json_newTags = json.dumps(newTags)
    json_data = (json_prefix + json_newTags + json_suffix)

    # post new tags to resourceId
    with requests.Session() as session:
        resp = session.post(f"{url}/deployment/api/deployments/{deploymentId}/resources/{resourceId}/requests",
                            data=json_data, headers=vraheaders, verify=False)
        resp.raise_for_status()
        json_data = resp.json()


# updating service key with new tag value
def update_existingTags_with_newTag(existingTags):
    newTags = [tag if tag["key"] != "service" else {"key": "service", "value": f"{newTag}"} for tag in existingTags]
    return newTags


# get the existing tags for resourceId
def get_existing_tags(bearer_token, inputs):
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
        return existingTags


# get bearer_token for vRA Api
def vraauth(inputs):
    vralogin = {
        "username": inputs["vraUsername"],
        "password": inputs["vraPassword"],
        "domain": inputs['vraDomain']
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

