Installation:


1. Install dependencies
2. Start postgresql service and make a database named pizza
3. Modify your settings.py to connect to database
4. Crate superuser
5. Make migrations
6. You will have to populate da db with custom data by hand as the admin app on the frontend is not functional
7. Install ngrok / or disable cors restrictions
8. If you have installed ngrok, start connection: ngrok http 8000
9. Copy and paste the url under 'Forwarding' from the ngrok connection into the pizza/src/api/base_url
10. Log into django admin at least one time to let the browser know you trust the source (a page will load asking if you trust ngrok port forwarding) 
