<?php
	if (isset($_POST['data'])) {
		$type = 'mouse';
		if (isset($_POST['touch'])) {
			$type = $_POST['touch'];
		}
		foreach ($traces as $traces) {
			
		}
	} else {
		echo 'No data received';
	}
?>
