import json


class PhpArray(list):

    def __init__(self, str, ls):
        super().__init__(ls)
        self.str = str

    def __str__(self):
        return json.dumps(self)

    @staticmethod
    def create(str):    # TODO associative arrays
        try:
            ls = json.loads(str)
            return PhpArray(str, ls)
        except ValueError:
            return None
