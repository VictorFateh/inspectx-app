<?php
// Check for empty fields
if(empty($_POST['name'])  		||
   empty($_POST['email']) 		||
   empty($_POST['phone']) 		||
   empty($_POST['message'])	||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
	echo "No arguments Provided!";
	return false;
   }
	
$name = strip_tags(htmlspecialchars($_POST['name']));
$email_address = strip_tags(htmlspecialchars($_POST['email']));
$phone = strip_tags(htmlspecialchars($_POST['phone']));
$message = strip_tags(htmlspecialchars($_POST['message']));
$date = date('Y-m-d H:i:s');
	
// Create the email and send the message
$to = 'victor@victorfateh.com'; // Add your email address inbetween the '' replacing yourname@yourdomain.com - This is where the form will send a message to.
$email_subject = "Inspect-X Contact Us:  $name";
// $email_body = 'InspectX Contact Us Page submission:\n\nName: $name\n\nEmail: $email_address\n\nPhone: $phone\n\nMessage:\n$message';
$email_body = '< table>
    <thead>
        <tr>
            <th class="empid">Time</th>
            <th class="fname">Name</th>
            <th class="lname">Phone</th>
            <th class="email">Email</th>
            <th class="age">Message</th>
        </ tr>
    </thead>
    <tbody>
        <tr>
            <td class="empid">$date</td>
            <td class="fname">$name</td>
            <td class="lname">$phone</td>
            <td class="email">$email_address</td>
            <td class="age">$message</td>
        </tr>
    </tbody>
</table>'

$headers = "From: support@inspect-x.com\n";
$headers .= "Reply-To: $email_address";	
mail($to,$email_subject,$email_body,$headers);
return true;			
?>
