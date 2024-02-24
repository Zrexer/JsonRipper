from rich import print as printer 
import json


class JsonRipper(object):
    def __init__(self, __data = None):
        self.data = __data
    
    def console_log(self):
        printer(json.dumps(self.data, indent=4).replace("true", "True").replace("false", "False"))

    def parse(self, default: bool = True) -> str:
        if default == True:
            return json.dumps(self.data, indent=4)
        else:
            return json.dumps(self.data, indent=4).replace("true", "True").replace("false", "False")

