# romiseBot

This reddit bot searches within the /CPSC470z subreddit for the activation phrase "Yo romiseBot:". This isn't case sensitive. 

It parses through the user's text and sends the strings to http://anagramica.com/best/:string in order to find the best word that can be found within the string. The robot will capitalize every other letter in the string and then send it as a reply to the user. 

This camel-casing of every other letter can be turned off with the case sensitive flag "-stahpPlsNoMore".

