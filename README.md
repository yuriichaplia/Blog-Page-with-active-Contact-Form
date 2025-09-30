# Blog Page with an active contact form
The upgraded version of the two previous projects that has an active contact form.

#### To get the form working you need to create .env file in the root folder with three variables:
+ TO_EMAIL=email_to_receive_messages<br>
+ MY_EMAIL=email_to_send_messages_from<br>
+ PASSWORD=app_password_for_my_email

#### When you fill the contact form with details (e.g. your email, name, message etc) and click send button, if the operation has been successful you will get a message from MY_EMAIL to TO_EMAIL with following details: 
Name: name_provided_in_contact_form
Email: email_provided_in_contact_form
Phone number: phone_number_provided_in_contact_form
Message: your message
