<html>
    <body>
    <table>

<?php
             $fp = fopen ( "/var/www/html/classement_BTC.csv" , "r" );
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