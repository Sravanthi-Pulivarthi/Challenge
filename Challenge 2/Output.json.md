{
  "compute": {
    "azEnvironment": "AzurePublicCloud",
    "customData": "",
    "evictionPolicy": "",
    "isHostCompatibilityLayerVm": "false",
    "licenseType": "",
    "location": "CentralIndia",
    "name": "web-vm",
    "offer": "UbuntuServer",
    "osProfile": {
      "adminUsername": "web_user",
      "computerName": "webserver",
      "disablePasswordAuthentication": "false"
    },
    "osType": "Linux",
    "placementGroupId": "",
    "plan": {
      "name": "",
      "product": "",
      "publisher": ""
    },
    "platformFaultDomain": "1",
    "platformUpdateDomain": "1",
    "priority": "",
    "provider": "Microsoft.Compute",
    "publicKeys": [],
    "publisher": "Canonical",
    "resourceGroupName": "azure-stack",
    "resourceId": "/subscriptions/2459f7c9-8b96-4c49-9f0e-153ba2183299/resourceGroups/azure-stack/providers/Microsoft.Compute/virtualMachines/web-vm",
    "securityProfile": {
      "secureBootEnabled": "false",
      "virtualTpmEnabled": "false"
    },
    "sku": "18.04-LTS",
    "storageProfile": {
      "dataDisks": [],
      "imageReference": {
        "id": "",
        "offer": "UbuntuServer",
        "publisher": "Canonical",
        "sku": "18.04-LTS",
        "version": "latest"
      },
      "osDisk": {
        "caching": "ReadWrite",
        "createOption": "FromImage",
        "diffDiskSettings": {
          "option": ""
        },
        "diskSizeGB": "30",
        "encryptionSettings": {
          "enabled": "false"
        },
        "image": {
          "uri": ""
        },
        "managedDisk": {
          "id": "/subscriptions/2459f7c9-8b96-4c49-9f0e-153ba2183299/resourceGroups/azure-stack/providers/Microsoft.Compute/disks/web-disk",
          "storageAccountType": "Standard_LRS"
        },
        "name": "web-disk",
        "osType": "Linux",
        "vhd": {
          "uri": ""
        },
        "writeAcceleratorEnabled": "false"
      },
      "resourceDisk": {
        "size": "34816"
      }
    },
    "subscriptionId": "2459f7c9-8b96-4c49-9f0e-153ba2183299",
    "tags": "",
    "tagsList": [],
    "userData": "",
    "version": "18.04.202210180",
    "vmId": "e6a85e01-d76c-46f5-82d6-408fd5455cf8",
    "vmScaleSetName": "",
    "vmSize": "Standard_B1s",
    "zone": ""
  },
  "network": {
    "interface": [
      {
        "ipv4": {
          "ipAddress": [
            {
              "privateIpAddress": "192.168.1.4",
              "publicIpAddress": "20.193.224.172"
            }
          ],
          "subnet": [
            {
              "address": "192.168.1.0",
              "prefix": "24"
            }
          ]
        },
        "ipv6": {
          "ipAddress": []
        },
        "macAddress": "6045BD72C712"
      }
    ]
  }
}
