from php.driver_generator import DriverGenerator

gen = DriverGenerator("python_driver", "/opt/lampp/htdocs/api_test")

gen.set_includes(["lib.php"])
gen.set_functions(["return_str", "add"])
success = gen.build()

if success:
    print("setup complete")
else:
    print("setup failed")
