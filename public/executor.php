<?php
$uploaded_file = $_FILES['srt']['tmp_name'];
system('./engine.py ' . $uploaded_file, $retval);