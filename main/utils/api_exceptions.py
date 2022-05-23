"""
Useful classes which can be used to specify the Error type when something failed.

Classes:
    RestError
"""
class RestError(AssertionError):
    """Class which can be used to specify the Rest request has failed"""
    def __init__(self, status_code, request, response):
        """
        :param status_code: int  Status code returned by the service through the API
        :param request:     str  Full URL endpoint to which the request was sent
        :param response:    str  Response which contains info about the failure 
        """
        self.status_code = status_code
        self.request = request
        self.response = response        

    def __str__(self):
        """Return an error with speci format"""
        message = "{{exec_type}}: Status Code: {status_code}, "\
                  "Error: {{error}}, URI: {{uri}}".format(status_code=self.status_code)
        content = {
            "reason": self.response.reason,
            "error_msg": self.response.text
        }
        if self.status_code in [500, 520, 521, 522]:
            trace_id = self.response.headers.get('Atl-Traceid', None)
            if trace_id:
                message = "{{exec_type}}: Status Code: {status_code}, "\
                          "TraceID: {trace_id}, Error: {{error}}, URI: {{uri}}".format(status_code=self.status_code,
                                                                                   trace_id=trace_id)
        return message.format(exec_type=self.__class__.__name__, error=content, uri=self.response.url)
