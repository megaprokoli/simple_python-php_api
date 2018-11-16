
function nothing($str) {
	return $str;
}

$parser = array(
	"str" => nothing,
	"int" => intval,
	"float" => floatval,
	"obj" => unserialize,
	"array" => json_decode
);