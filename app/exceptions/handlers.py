import xmltodict
from fastapi import Request, Response


class SOAPException(Exception):
    def __init__(self, message: str, status_code: int, request_body: str = None):
        self.message = message
        self.status_code = status_code
        self.request_body = request_body


async def soap_exception_handler(request: Request, exc: SOAPException):
    response_data = {
        "soap:Envelope": {
            "@xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
            "soap:Body": {
                "Fault": {
                    "faultcode": "soap:Client",
                    "faultstring": exc.message,
                    "statusCode": exc.status_code,
                    "request": {
                        "method": request.method,
                        "url": str(request.url),
                        "headers": dict(request.headers),
                        "body": exc.request_body
                    }
                }
            }
        }
    }
    response_xml = xmltodict.unparse(response_data, pretty=True)
    return Response(content=response_xml, media_type="text/xml", status_code=exc.status_code)
