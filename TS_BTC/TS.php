<!DOCTYPE html>
<html>
      
<head>
    <title>
        TS Before Tomorrow Comes
    </title>
</head>
  
<body>
<br>Le classement se met à jour tous les lundis à partir de 12h (nécessite la manip' top-booster en premier lieu)</br>
<br></br>
    <form method="post">          
        <input type="submit" name="button1"
                value="Sortir le classement"/>
    </form>
    <br></br>
    <?php
      
        if(isset($_POST['button1'])) {
            usleep(5000000);
            $fp = fopen ( "/var/www/html/affichage.csv" , "r" );
            while (( $data = fgetcsv ( $fp , 1000 , ";" )) !== FALSE ) {
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
