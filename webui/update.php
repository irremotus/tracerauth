<?php
	if (isset($_GET['key']) && strlen(getenv('TRACER_UPDATE_KEY')) > 0 && hash('sha256', $_GET['key']) == getenv('TRACER_UPDATE_KEY')) {
		system('/var/www/dotracerupdate.sh');
		echo 'Updated';
	} else {
		echo 'Did not update';
	}
?>
