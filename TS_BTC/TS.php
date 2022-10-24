<!DOCTYPE html>
<html>
      
<head>
    <title>
        TS Before Tomorrow Comes
    </title>
</head>

<style>
    @keyframes spin3D{
        from {transform: rotateY(0deg)}
        to {transform: rotateY(360deg)}
    }
    @keyframes spinning{
        from {transform: rotate(0deg)}
        to {transform: rotate(360deg)}
    }
    .tooltip{
        display: inline;
        position: relative;
    }
    .tooltip:hover:after{
        background: #333;
        background: rgba(0,0,0,.8);
        border-radius: 5px;
        bottom: 26px;
        color: #fff;
        content: attr(title);
        left: 20%;
        padding: 5px 15px;
        position: absolute;
        z-index: 98;
        width: 220px;
    }
    .tooltip:hover:before{
        border: solid;
        border-color: #333 transparent;
        border-width: 6px 6px 0 6px;
        bottom: 20px;
        content: "";
        left: 50%;
        position: absolute;
        z-index: 99;
    }
    a span{	
        display:none;
        color:rgb(255, 182, 182);
        background:rgba(51,51,51,0.75);
        padding:5px;
        border-radius:4px;
        box-shadow: 0px 0px 10px rgb(255, 182, 182);
        -moz-border-radius:4px;
        -webkit-border-radius:4px;
        width:100px;
        text-align:center;
        position: absolute;
        z-index:10;
    }
    a { 
        display: inline-block;
    }
    a:hover span{ 
        display:block; 
    }
    span.blue{
        background: #282828;
        border: 2px solid rgb(255, 182, 182);
    }
    body{
        background: #282828 url('https://toria.fr/btc/background.jpg') top left fixed;
        width: 710px; 
        height: auto; 
        text-align: justify; 
        margin: auto; 
        background-color: #2d2d6e; 
        display: flex; 
        flex-direction: row;
    }
    header, footer{
        width: 100%;
        padding: 10px 10px;
        background: #282828;
        box-shadow: 0px 0px 15px rgb(255, 182, 182);
    }
    header{
        border-top: 2px solid rgb(255, 182, 182);
        border-right: 2px solid rgb(255, 182, 182);
        border-left: 2px solid rgb(255, 182, 182);
        border-bottom: 2px solid rgb(255, 182, 182);
        height: 120px;
        width: 710px;
    }
    header h1{
        font-size: 50px;
        width: 100%;
        margin: 0 auto;
        text-align: center;
        text-shadow: 0px 0px 15px rgb(71, 17, 17);
        color: rgb(255, 182, 182)
    }
    section{
        border-top: 2px solid rgb(255, 182, 182);
        border-right: 2px solid rgb(255, 182, 182);
        border-left: 2px solid rgb(255, 182, 182);
        border-bottom: 2px solid rgb(255, 182, 182);
        display: flex;
        flex-flow: row wrap;
        justify-content: center;
        padding-bottom: 20px;
        margin: 20px auto;
        box-shadow: 0px 0px 10px #bbb;
        background-color: #fff;
        height: 90px;
        width: 710px;
    }
    section h2{
        margin: 20px 0;
        width: 90%;
    }
    section h3{
        text-align: center;
        margin: 20px 0;
        width: 80%;
    }
    section > div{
        width: 90%;
    }
    .enrobage{
        border-top: 2px solid rgb(255, 182, 182);
        border-right: 2px solid rgb(255, 182, 182);
        border-left: 2px solid rgb(255, 182, 182);
        border-bottom: 2px solid rgb(255, 182, 182);
        display: block;
        text-align: left;
        padding: 10px;
        margin: 10px auto 30px auto;
        color: #fff;
        background-color: #282828;
        box-shadow: 0px 0px 10px rgb(255, 182, 182);
        border-radius: 5px;
    }
    .enrobage h2{
        text-align: center;
        vertical-align: middle;
        height: 50px;
        width: 710px;
        color: rgb(255, 182, 182);
        font-style: bold;
        font-size: 200%;
        text-shadow: 0px 0px 15px rgb(71, 17, 17);
        border-bottom: 3px solid rgb(255, 182, 182);
    }
    .enrobage a{
        display: block;
        text-align: center;
        color: rgb(255, 182, 182);
        background-color: #282828;
    }
    .enrobage a:hover{
        color: #783da2;
    }
    
</style>

<div class="body">
<div class="enrobage">
    <header>
        <h1>Classement TopSites</h1>
    </header>
    <div class="section">
    <br>Le classement se met à jour tous les lundis à partir de 12h (nécessite la manip' top-booster en premier lieu)</br>
    <h3><a href="http://toria.fr/top-booster/index.php">Lien vers top-booster</a></h3>
    <br></br>
        <center><form method="post">  
            <input type="submit" name="button2"
                    value="Mettre à jour les logs"/>        
            <input type="submit" name="button1"
                    value="Sortir le classement"/>
        </form></center>
        </div>
        <div class="enrobage">
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
        if(isset($_POST['button2'])) {
            usleep(5000000);
            $output = shell_exec('sh TS.sh');
            echo "<pre>$output</pre>";
        }
    ?>
        </div>
        </div>
    </div>
</html>
