<?php
	if (isset($_POST['points'])) {
		$type = 'mouse';
		if (isset($_POST['inputtype'])) {
			$type = $_POST['inputtype'];
		}
		header('Content-Disposition: attachment; filename="'.$type.'_points.dec"');
		header("Content-Type: application/force-download");
		header("Content-Length: ".strlen($_POST['points']));
		header("Connection: close");
		echo $_POST['points'];
	} else {
		echo 'No data received';
	}
?>
