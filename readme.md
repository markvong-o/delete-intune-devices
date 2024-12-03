# Delete Intune Devices Python Script

## Leverage MS Graph API via the msgraph-sdk for python

### Pre-req:

1. Create a <a target="_blank" href="https://learn.microsoft.com/en-us/graph/auth-register-app-v2">mobile/desktop app in Azure</a>

2. Redirect URI should be

```   http://localhost:8401```

3. Assign API Permissions

```   User.ReadWrite.All, DeviceManagementManagedDevices.ReadWrite.All, Directory.ReadWrite.All```

4. Copy the Client ID

### Steps for launching app

1. Unzip file to find delete_intune_devices folder

2. In terminal, open open folder to root dir ./delete_intune_devices.

3. Activate virtual env

```   . ./venv/bin/activate```

4. Install libraries

```   pip install requirements.txt```

5. Run the script

```   python3 delete_intune_devices.py```
