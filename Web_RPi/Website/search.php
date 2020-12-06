<?php

require 'vendor/autoload.php';

use Website\SQLiteConnection;

$pdo = (new SQLiteConnection())->connect();
if ($pdo == null)
	echo 'Whoops, could not connect to the SQLite database!';

public function getAmount($PlateNumber) {
	$stmt = $this->pdo->prepare('SELECT PlateNumber,
					Amount
					FROM CarDosier
					WHERE PlateNumber = :PlateNumber;');

	$stmt->execute(['amount' => $amount]);

	while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
		$amont = 'amount' => $row['PlateNumber']
	}
	return $amount;
}
?>
