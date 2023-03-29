# You running this script/function means you will not blame the author(s) if this breaks your stuff.
# This script/function is provided AS IS without warranty of any kind.
# The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.

import json
import requests

# AVI API endpoint and credentials
avi_api_endpoint = 'https://AVI-FQDN/api'
avi_username = 'admin'
avi_password = 'password'


def handler(context, inputs):
    resourceProperties = inputs['__metadata_resourceProperties']
    vs_uuid = resourceProperties['__vro_sdkObjectId'].split('(', 1)[1].rstrip(')')

    # Define new port configuration
    vs_port = inputs['vs_port']
    pool_port = inputs['pool_port']

    # Retrieve the existing virtual service configuration
    vs_api_url = f'{avi_api_endpoint}/virtualservice/{vs_uuid}'
    vs_response = requests.get(vs_api_url, auth=(avi_username, avi_password), verify=False)
    vs_config = vs_response.json()

    # Extract the pool UUID from the virtual service configuration
    pool_uuid = vs_config['pool_ref'].split('/')[-1]

    # Modify the virtual service configuration to update the load balanced ports
    vs_config['services'][0]['port'] = vs_port
    vs_config['services'][0]['port_range_end'] = vs_port

    # Retrieve the existing pool configuration
    pool_api_url = f'{avi_api_endpoint}/pool/{pool_uuid}'
    pool_response = requests.get(pool_api_url, auth=(avi_username, avi_password), verify=False)
    pool_config = pool_response.json()

    # Modify the pool configuration to update the load balanced ports
    for server in pool_config['servers']:
        server['port'] = pool_port
    pool_config['default_server_port'] = pool_port

    # Send a PUT request to update the pool configuration
    pool_response = requests.put(pool_api_url, auth=(avi_username, avi_password), json=pool_config, verify=False)
    if pool_response.status_code == 200:
        print(f'Successfully updated pool {pool_uuid} with new port configuration: {pool_port}')
    else:
        print(f'Error updating pool {pool_uuid}: {pool_response.text}')

    # Send a PUT request to update the virtual service configuration
    vs_response = requests.put(vs_api_url, auth=(avi_username, avi_password), json=vs_config, verify=False)
    if vs_response.status_code == 200:
        print(f'Successfully updated virtual service {vs_uuid} with new port configuration: {vs_port}')
    else:
        print(f'Error updating virtual service {vs_uuid}: {vs_response.text}')