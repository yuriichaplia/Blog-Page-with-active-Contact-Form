# Blog Page with an active contact form
The upgraded version of the two previous projects that has an active contact form.

#### To get the form working you need to create .env file in the root folder with three variables:

- `TO_EMAIL` → the email address that will receive messages  
- `MY_EMAIL` → the email address used to send messages  
- `PASSWORD` → the app password for `MY_EMAIL`  

## Usage  

When you fill out the contact form (your **name, email, phone number, and message**) and click **Send**, the app will:  

- Send an email **from** `MY_EMAIL` **to** `TO_EMAIL`.  
- The email will contain the following details:  
  - **Name:** name provided in the form  
  - **Email:** email provided in the form  
  - **Phone Number:** phone number provided in the form  
  - **Message:** your message  

