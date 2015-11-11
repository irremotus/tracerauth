<?php
	if (isset($_POST['points'])) {
		header("Content-Type: application/force-download");
		header("Content-Length: ".strlen($_POST['points']));
		header("Connection: close");
		echo $_POST['points'];
	} else {
		echo 'No data received';
	}
?>
