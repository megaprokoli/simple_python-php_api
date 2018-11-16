import os


class DriverGenerator:

    def __init__(self, filename="python_driver.php", path="php_code/"):
        self.filename = filename if len(filename.split('.')) > 1 else filename + ".php"
        self.path = path if path[-1] == "/" else path + "/"

        self.start = "<?php\nerror_reporting(0);\n"
        self.end = "?>"
        self.includes = list()
        self.functions = list()
        self.func_prefix = "$funcs = array(\n"
        self.func_suffix = ");\n"
        self.translater = self.load_code("driver_body.php")
        self.parser = self.load_code("parser.php")

    def load_code(self, file):
        code = ""

        with open(os.path.dirname(__file__) + "/php_code/" + file, 'r') as file:
            for line in file:
                code += line
        return code

    def set_includes(self, includes):
        if not isinstance(includes, list):
            includes = [includes]
        for inc in includes:
            self.includes.append("include('{}');\n".format(inc))

    def set_functions(self, funcs):
        if not isinstance(funcs, list):
            funcs = [funcs]
        for func in funcs:
            self.functions.append("'{}' => {},\n".format(func, func))

    def build(self):
        # TODO check if all is set
        content = ""
        content += self.start

        for inc in self.includes:
            content += inc

        content += self.parser
        content += self.func_prefix

        for func in self.functions:
            content += func

        content += self.func_suffix
        content += self.translater
        content += self.end

        with open(self.path + self.filename, 'w') as file:
            if not file.writable():
                return False

            for char in content:
                file.write(char)

        return True
