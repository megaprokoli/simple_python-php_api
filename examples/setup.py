from php.driver_generator import DriverGenerator

gen = DriverGenerator("python_driver", "C:/xampp/htdocs/php_api")

gen.set_includes(["lib.php"])
gen.set_functions(["return_str", "add"])
success = gen.build()

if success:
    print("setup complete")
else:
    print("setup failed")
