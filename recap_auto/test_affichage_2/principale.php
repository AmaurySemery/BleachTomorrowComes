<html>
 <head>
 <title>Fiche technique</title>
 <meta charset="utf-8">
 <!-- importer le fichier de style -->
 <link rel="stylesheet" href="style.css" media="screen" type="text/css" />
 </head>
 <body>
 <div id="container">


 <!-- tester si l'utilisateur est connecté -->

 <form action="verification.php" method="POST">
 <a href='principale.php?deconnexion=true'><span>Déconnexion</span></a>
 

            <h1>Jauges</h1>
			<label><b>PV</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="PV" required>
            <p></p>
			<label><b>EP</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="EP" required>
            <p></p>
			<label><b>ES</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>

            <h1>Répartition</h1>
            <label><b>Pouvoir</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Base</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Evolution</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
            <label><b>Techniques physiques</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Mains nues</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Armes CàC</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
            <label><b>Armes distance</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Techniques spirituelles</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Energie</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
            <label><b>Kekkai</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Habileté</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Vitesse</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
            <label><b>Résistance</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Science</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Reiatsu</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
            <label><b>Camouflage</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Détection</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Aura</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
            <label><b>Soin</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Régénération</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<label><b>Guérison</b></label>
            <input type="int" placeholder="Entrer le nom d'utilisateur" name="ES" required>
            <p></p>
			<input type="submit" value="Ajouter">
            <?php
 session_start();
 if(isset($_GET['deconnexion']))
 { 
 if($_GET['deconnexion']==true)
 { 
 session_unset();
 header("location:login.php");
 }
 }
 else if($_SESSION['username'] !== ""){
 $user = $_SESSION['username'];
 // afficher un message
 echo "<title>Bonjour $user, vous êtes connecté !</title>";
 }
 ?>
		</form>
        </div>
 </body>
</html>