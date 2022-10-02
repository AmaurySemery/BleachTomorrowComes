phpinfo()
<!-- <?php

$ch = curl_init();
$timeout = 5; // set to zero for no timeout
curl_setopt ($ch, CURLOPT_URL, 'https://www.before-tomorrow-comes.fr/memberlist');
curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
$file_contents = curl_exec($ch);
curl_close($ch);
$lines = array();
$lines = explode("\n", $file_contents);

// display file line by line
foreach($lines as $line_num => $line) {
echo "Line # {$line_num} : ".htmlspecialchars($line)."<br />\n";
}

?> -->