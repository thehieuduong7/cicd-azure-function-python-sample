import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
    logging.info("Python HTTP trigger processed a request.")

    number_query_value = req.params.get("number")

    if not number_query_value:
        return func.HttpResponse("Please provide a number in the query string.", status_code=400)

    try:
        number = int(number_query_value)
        response = f"The number {number} is {'Even' if number % 2 == 0 else 'Odd'}."
        return func.HttpResponse(response, status_code=200)
    except ValueError:
        return func.HttpResponse(f"Unable to parse {number_query_value}", status_code=400)
