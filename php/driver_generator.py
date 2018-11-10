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
        self.parser = "$parser = array(\n\t'int' => intval,\n\t'float' => floatval\n);\n"
        self.translater = "try{\n" \
                          "$requested_func = $_GET['data'];\n" \
                          "if(isset($_GET['args']) && !empty($_GET['args'])) {\n\t" \
                          "$args = explode('|', $_GET['args']);\n\t" \
                          "array_pop($args);\n\t" \
                          "for($i=0; $i < count($args); $i++) {\n\t\t" \
                          "$split = explode('#', $args[$i]);\n\t\t" \
                          "$args[$i] = $parser[$split[0]]($split[1]);\n\t" \
                          "}\n\t" \
                          "echo call_user_func_array($funcs[$requested_func], $args);\n" \
                          "} else {\n\t" \
                          "echo $funcs[$requested_func]();\n" \
                          "}\n}\n" \
                          "catch(Exception $e) {\n" \
                          "http_response_code(500);\n}"   # TODO maybe from file

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
