'''
在 HTTP 协议中，状态码是一个三位数字，每个状态码的开头数字代表不同的含义。通常，状态码分为五个类别，根据开头数字的不同，含义如下：
1xx：信息性状态码，通常不会直接显示给用户，而是用于指示某些更进一步的操作。例如，100 Continue 表示服务器已收到了请求的头部，并且客户端应继续发送请求的其余部分。
2xx：成功状态码，表示请求已成功被服务器接收、理解、并接受。例如，200 OK 表示请求已成功。
3xx：重定向状态码，表示需要客户端采取进一步的操作才能完成请求。例如，301 Moved Permanently 表示请求的资源已被永久移动到新位置。
4xx：客户端错误状态码，表示客户端发送的请求有错误，服务器无法处理。例如，400 Bad Request 表示请求有语法错误。
5xx：服务器错误状态码，表示服务器在处理请求时发生了错误。例如，500 Internal Server Error 表示服务器遇到了一个未预料到的错误。
'''


class HTTPResponse:
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        return {'code': self.code, 'message': self.message, 'data': self.data}


class SuccessResponse(HTTPResponse):
    def __init__(self, data):
        super().__init__(200, "Success", data)


class BadRequestResponse(HTTPResponse):
    def __init__(self, data):
        super().__init__(400, "Bad Request", data)


class UnauthorizedResponse(HTTPResponse):
    def __init__(self, data):
        super().__init__(401, "Unauthorized", data)


class ForbiddenResponse(HTTPResponse):
    def __init__(self, data):
        super().__init__(403, "Forbidden", data)


class NotFoundResponse(HTTPResponse):
    def __init__(self, data):
        super().__init__(404, "Not Found", data)


class InternalServerErrorResponse(HTTPResponse):
    def __init__(self, data):
        super().__init__(500, "Internal Server Error", data)
