# Slack-API-Outgoing-Webhook
Use this program to extract any link in a channel by setting up an outgoing webhook

## How it works 
1. Set up an outgoing webhook in your slack workspace
2. Put the token which you get for the webhook in place of TOKEN_ID in get/views.py
3. Host this project on a URL. (P.S. You can use ngrok for the same) 
4. Give this 'URl/get' to the URL required in the webhook settings.
5. Also put the domain name in the ALLOWED_HOSTS list in slack/settings.py
6. Run the server by running this command in a terminal in the project directory.
```
python manage.py runserver
```
7. Now go to the url 'URL/get' and watch the project work.
