try {
	$requested_func = $_GET["data"];

	if(isset($_GET["args"]) && !empty($_GET["args"])) {
		$args = explode("|", $_GET["args"]);
		array_pop($args);

		for($i=0; $i < count($args); $i++) {
			$split = explode("#", $args[$i]);
			$args[$i] = $parser[$split[0]]($split[1]);
		}
		$return_val = call_user_func_array($funcs[$requested_func], $args);

	} else {
		$return_val = $funcs[$requested_func]();
	}

	if(gettype($return_val) == "array") {
		$return_val = json_encode($return_val);
	} else if(gettype($return_val) == "object") {
		$return_val = serialize($return_val);
	}
	echo $return_val;
}catch(Exception $e) {
	http_response_code(500);
}