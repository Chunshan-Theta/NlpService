

class responds():
    def __init__(self, content,code=200,headers={"Access-Control-Allow-Origin": "*"}):
        assert code.isdigit()
        assert type(headers) is dict
        self.code = code
        self.content = content
        self.headers = headers
    def toResponds():
        return self.content,self.code,self.headers
