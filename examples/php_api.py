from php.php_interface import PhpInterface

interface = PhpInterface("http://localhost/api_test/python_driver.php")
print(interface.call("add", [("int", 3), ("int", 5)]))
print(interface.call("return_str"))

