<?php
	session_start();
	if (isset($_SESSION['id'])) {
		$id = $_SESSION['id'];
	} else {
		$id = rand(1000000000, 9999999999);
		$_SESSION['id'] = $id;
	}

	if (isset($_POST['data'])) {
		$type = 'mouse';
		$istouch = 0;
		if (isset($_POST['touch'])) {
			if ($_POST['touch'] == "1")
				$istouch = 1;
		}
		if (isset($_POST['data'])) {
			$traces = $_POST['data'];
		}
		$path = "";
		foreach ($traces as $trace) {
			$path .= "<" . $trace . ">";
		}

		$a_configs = array();
		$filename = "/var/www/tracer_mysql_config.ini";
		if (file_exists($filename)) {
			$a_configs = parse_ini_file($filename);
		} else {
			die("Could not find config file");
		}
		if (!isset($a_configs["host"]) ||
			!isset($a_configs["user"]) ||
			!isset($a_configs["pass"])) {
				die("Error in config file");
		}

		$mysqli = new mysqli($a_configs["host"], $a_configs["user"], $a_configs["pass"], "tracer");
		if ($mysqli->connect_errno) {
			die("Error connecting to database");
		}

		if (!($stmt = $mysqli->prepare("INSERT INTO paths(sessid, istouch, path) VALUES(?, ?, ?);"))) {
			die("Error writing to database");
		}

		if (!$stmt->bind_param("iis", $id, $istouch, $mysqli->real_escape_string($path))) {
			die("Error binding parameters");
		}

		if (!$stmt->execute()) {
			die("Error executing insert");
		}

		echo "1";
	} else {
		echo 'No data received';
	}
?>
