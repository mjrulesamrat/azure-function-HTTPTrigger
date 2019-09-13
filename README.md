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

