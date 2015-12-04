<?php
	session_start();
	if (isset($_SESSION['id'])) {
		$id = $_SESSION['id'];
	} else {
		$id = random_int();
		$_SESSION['id'] = $id;
	}

	if (isset($_POST['data'])) {
		$type = 'mouse';
		if (isset($_POST['touch'])) {
			$type = $_POST['touch'];
		}
		if (isset($_POST['data'])) {
			$traces = $_POST['data'];
		}
		$path = "";
		foreach ($traces as $trace) {
			$str .= $trace . "|";
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

		$istouch = 0;
		if ($type) {
			$istouch = 1;
		}

		if (!$stmt->bind_param("iis", $id, $istouch, $path)) {
			die("Error binding parameters");
		}

		if (!$stmt->execute()) {
			die("Error executing insert");
		}

		echo "Success";
	} else {
		echo 'No data received';
	}
?>
