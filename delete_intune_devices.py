# Requirements:
# 1. Create an app registration in Azure portal
# 2. Assign Graph API permissions: User.ReadWrite.All, DeviceManagementManagedDevices.ReadWrite.All, Directory.ReadWrite.All
# 3. Copy the client ID

import asyncio
from azure.identity import InteractiveBrowserCredential
from msgraph import GraphServiceClient
import json

# Get client ID of app in microsoft portal
_client_id = input('Please input the client id from the azure apps portal: ')


_scopes = ['User.ReadWrite.All',
           'DeviceManagementManagedDevices.ReadWrite.All', 'Directory.ReadWrite.All']

# Multi-tenant apps can use "common",
# single-tenant apps must use the tenant ID from the Azure portal
_tenant_id = 'common'
_redirect_uri = 'http://localhost:8401'


# azure.identity
credential = InteractiveBrowserCredential(
    client_id=_client_id, tenant_id=_tenant_id, redirect_uri=_redirect_uri)

graph_client = GraphServiceClient(credential, _scopes)

# Get all managed devices
async def get_managed_devices():
    managed_devices = await graph_client.device_management.managed_devices.get()
    print(
        f'List of managed devices... {json.dumps(managed_devices, indent=4)}')
    return managed_devices

# Delete provided device by id
async def delete_managed_device(_device_id):
    print(f'Deleting device:{_device_id}...')
    await graph_client.device_management.managed_devices.by_managed_device_id(_device_id).delete()

# Runs function to get all managed devices
asyncio.run(get_managed_devices())

# Runs function to delete provided device by device ID
device_id = input("Enter the id of the device to be deleted: ")
asyncio.run(delete_managed_device(device_id))
