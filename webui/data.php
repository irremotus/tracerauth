<?php
	if (isset($_POST['data'])) {
		$type = 'mouse';
		if (isset($_POST['touch'])) {
			$type = $_POST['touch'];
		}
		if (isset($_POST['data'])) {
			$traces = $_POST['data'];
		}
		foreach ($traces as $trace) {
			echo $trace;
		}

		/*
		$a_configs = array();
		$filename = dirname(__FILE__)."/mysql_config.ini";
		if (file_exists($filename)) {
			$a_configs = parse_ini_file($filename);
		}
		if (!isset($a_configs["host"]) ||
			!isset($a_configs["user"]) ||
			!isset($a_configs["password"])) {
			return FALSE;
		}

		$mysqli = new mysqli($a_configs["host"], $a_configs["user"], $a_configs["password"], "tracer");
		if ($mysqli->connect_errno) {
			die("Error connecting to database");
		}

		if (!($stmt = $mysqli->prepare("INSERT INTO paths(istouch, path) VALUES(?, ?);"))) {
			die("Error writing to database");
		}

		$istouch = 0;
		if ($type) {
			$istouch = 1;
		}

		if (!$stmt->bind_param("is", $istouch, $path)) {
			die("Error binding parameters");
		}

		if (!$stmt->execute()) {
			die("Error executing insert");
		}
		 */

		echo "Success";
	} else {
		echo 'No data received';
	}
?>
