import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    # if name is passed along the request json body
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # Add name to the queue defined as msg above
        msg.set(name)
        return func.HttpResponse(
            json.dumps({
                "method": req.method,
                "url": req.url,
                "message": f"Hello {name}!",
                "headers": dict(req.headers),
                "params": dict(req.params)                
            })
        )
    else:
        return func.HttpResponse(
            json.dumps({
                "error": "Please pass a name on the query string or in the request body"
            }),
             status_code=400
        )
