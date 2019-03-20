if(isset($_POST['id'])){
	mysql_query("UPDATE 'recipes' SET 'likes' = 'likes' + 1 WHERE 'id'='".$_POST['id']."'");
	$query = mysql_query("SELECT FROM 'recipes' WHERE 'id'='".$_POST['id']."'");
	$results = mysql_fetch_assoc($query);
	echo json_encode($results);
}