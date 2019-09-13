# Azure Functions HTTPTrigger Demo

## Prerequisites

### Install Azure Functions core tools
> https://docs.microsoft.com/en-gb/azure/azure-functions/functions-run-local#linux


### Install Azure CLI
> https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest#install


### Have an active subsciption with Azure


## Running Project locally:

### Create a virtual environment

To run and test project locally one requires a virual environment installed locally. Currently Azure functions supports Python3.6 version. So, let's create one with Python3.6.

> `$ virtualenv -p python3.6 venv_demo`

Activae virtual environment

> `$ . venv_demo/bin/activate`

Install requirements:
> `$ pip install -r requirements.txt`

...


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
