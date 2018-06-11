<?php
require_once '../../vendor/autoload.php';
// Check for empty fields
if(empty($_POST['name'])  		||
   empty($_POST['email']) 		||
   empty($_POST['phone']) 		||
   empty($_POST['car'])	||
   empty($_POST['location']) ||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
	echo "No arguments Provided!";
	return false;
   }
	
$name = strip_tags(htmlspecialchars($_POST['name']));
$email_address = strip_tags(htmlspecialchars($_POST['email']));
$phone = strip_tags(htmlspecialchars($_POST['phone']));
$car = strip_tags(htmlspecialchars($_POST['car']));
$location = strip_tags(htmlspecialchars($_POST['location']));
$date = date('Y-m-d H:i:s');

values = [
    [$date, $name, $email_address, $phone, $car, $location],
];
$body = new Google_Service_Sheets_ValueRange([
  'values' => $values
]);
$params = [
  'valueInputOption' => $valueInputOption
];
$result = $service->spreadsheets_values->update($spreadsheetId, $range,
    $body, $params);

printf("%d cells updated.", $result->getUpdatedCells());


return true;			
?>
