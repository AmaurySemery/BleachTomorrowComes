<html>
    <body>
    <table>

<?php
             shell_exec ('/var/www/html/');
             shell_exec ('python3 TS_script.py');
             echo "Waiting for 5 seconds...<br/>";
             usleep(5000000);
             $fp = fopen ( "/var/www/html/affichage.csv" , "r" );
             while (( $data = fgetcsv ( $fp , 1000 , "," )) !== FALSE ) {
             $i = 0;
             echo "<tr>";
             foreach($data as $row) {
             echo "<td>" . $row . "</td>";
             $i++ ;
             }
             echo "/<tr>";
             }
             fclose ( $fp );
             ?>
             </table>
</body>
</html>