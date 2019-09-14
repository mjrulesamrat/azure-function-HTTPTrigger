# Azure Functions HTTPTrigger Demo

## Prerequisites

### Install Azure Functions core tools
> https://docs.microsoft.com/en-gb/azure/azure-functions/functions-run-local#linux


### Install Azure CLI
> https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest#install

Check version :  `$ az --version`

### Have an active subsciption with Azure

Login to az cli : `$ az login`

latest docs: https://docs.microsoft.com/en-gb/cli/azure/?view=azure-cli-latest

---

## Running Project locally:

### Create a virtual environment

To run and test project locally one requires a virual environment installed locally. Currently Azure functions supports Python3.6 version. So, let's create one with Python3.6.

> `$ virtualenv -p python3.6 venv_demo`

Activae virtual environment

> `$ . venv_demo/bin/activate`

Install requirements:
> `$ pip install -r requirements.txt`

---


## Creating a local Functions project

A Functions project is the equivalent of a function app in Azure(As they keep saying and it's true!). It can have multiple functions that all share the same local and hosting configurations(Also true!).

> `$ func init HTTPtriggerDemo`

Run the following command to add new function:

> `$ func new`

```
Select a template:
1. Azure Blob Storage trigger
2. Azure Cosmos DB trigger
3. Azure Event Grid trigger
4. Azure Event Hub trigger
5. HTTP trigger
6. Azure Queue Storage trigger
7. Azure Service Bus Queue trigger
8. Azure Service Bus Topic trigger
9. Timer trigger

The function "HttpTrigger" was created successfully from the "HTTP trigger" template.
```

To run function locally:

> `$ func host start`

HTTPTrigger can be accessed at below URL:

> HttpTrigger: [GET,POST]  http://localhost:7071/api/HttpTrigger

---

## Create Functions app in Azure

Now that you have run your function locally, you can create the function app, other required resources and storage account in Azure.

* Creating resource group

 An Azure resource group is a logical container into which Azure resources like function apps, databases, and storage accounts are deployed and managed.

> `$ az group create --name <ResourceGroupName> --location westindia`

Available regions: https://azure.microsoft.com/en-gb/global-infrastructure/regions/

* Create an Azure Storage Account

Functions uses a general-purpose account in Azure Storage to maintain state and other information about your functions

> `$ az storage account create --name <storage_name> --location westindia --resource-group <ResourceGroupName> --sku Standard_LRS`


* Create a function app in Azure

A function app provides an environment for executing your function code. It lets you group functions as a logical unit for easier management, deployment, and sharing of resources.

> `$ az functionapp create --resource-group myResourceGroup --os-type Linux \
--consumption-plan-location westindia  --runtime python \
--name <APP_NAME> --storage-account  <STORAGE_NAME>`


* Deploy the function app project to Azure

After the function app is created in Azure, you can use the func azure functionapp publish Core Tools command to deploy your project code to Azure.

> `$ func azure functionapp publish <APP_NAME> --build remote`


Copy the Invoke url value for your HttpTrigger, which you can now use to test your function in Azure. The URL contains a code query string value that is your function key. This key makes it difficult for others to call your HTTP trigger endpoint in Azure.

* Test the function in Azure

Use cURL to test the deployed function. Using the URL, including the function key, that you copied from the previous step, append the query string &name=<yourname> to the URL.

---

extend function by...

## Adding Azure Storage Queue output bindings

Binding to a function is a way of declaratively connecting another resource to the function; bindings may be connected as __input bindings__, __output bindings__, or both. Data from bindings is provided to the function as parameters.

Triggers and bindings let you avoid hardcoding access to other services. Your function receives data (for example, the content of a queue message) in function parameters. You send data (for example, to create a queue message) by using the return value of the function.

Ref: https://docs.microsoft.com/en-gb/azure/azure-functions/functions-add-output-binding-storage-queue-python

* Download the function app settings

> `$ func azure functionapp fetch-app-settings HTTPTrigDemoApp<APP_NAME>`

It will add settings to `local.settings.json` file. Which is already ignored and will not be version controlled. There is `production.example.json` for reference.

* Enable extension bundles

open `host.json` and `extensionBundle` settings.

```
{
    "version": "2.0",
    "extensionBundle": {
        "id": "Microsoft.Azure.Functions.ExtensionBundle",
        "version": "[1.*, 2.0.0)"
    }
}
```

After this one can add output bindings to the FunctionApp.


* Add an output binding

Update `function.json` and include queue type out binding.

```
{
    "type": "queue",
    "direction": "out",
    "name": "msg",
    "queueName": "outqueue",
    "connection": "AzureWebJobsStorage"
}
```

* Run Function locally

> `$ func host start`

and access at `http://localhost:7071/api/HttpTrigger?name=Jay`

Next, you use the Azure CLI to view the new queue and verify that a message was added.



* To publish again

> `$ func azure functionapp publish <APP_NAME> --build remote`

Remote build succeeded!
