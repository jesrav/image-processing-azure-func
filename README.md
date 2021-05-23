# image-processing-azure-func

Example azure function app, that processes images, using a blob trigger.

## Get started

### Debugging locally
To run locally using the vscode azure function extension, copy the local.settings_copy.json into local.settings.json and fill out the missing environment variables.
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "IMAGE_STORAGE_CONNECTION_STRING": ""
  }
}
````
Where AzureWebJobsStorage is the connection string to the container where data about the triggers will be stored, 
and IMAGE_STORAGE_CONNECTION_STRING the connection string to the container where you will be uploading images to.

### Upload test image
Upload image to `<your-container>/raw/` and check the output in `<your-container>/processed/`



