<!DOCTYPE html>
<html>
      
<head>
    <title>
        TS Before Tomorrow Comes
    </title>
</head>
  
<body>
    <form method="post">
        <input type="submit" name="button1"
                value="Mouliner le programme"/>
          
        <input type="submit" name="button2"
                value="Sortir le classement"/>
    </form>
    <?php
      
        if(isset($_POST['button1'])) {
            $Commande = shell_exec("cd /var/www/html && python3 TS_script.py");
            echo "$Commande";
        }
        if(isset($_POST['button2'])) {
            usleep(5000000);
            $fp = fopen ( "/var/www/html/affichage.csv" , "r" );
            while (( $data = fgetcsv ( $fp , 1000 , "," )) !== FALSE ) {
            $i = 0;
            echo "<tr>";
            foreach($data as $row) {
            echo "<div>" . $row . "</div>";
            $i++ ;
            }
            echo "<tr>";
            }
            fclose ( $fp );
        }
    ?>
      
    
    </body>
</html>
