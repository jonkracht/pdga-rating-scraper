
A Python script to grab any number of disc golfers' player ratings from [pdga.com](https://www.pdga.com), the website of the Professional Disc Golf Association.


## Use
The user must specify the players for whom ratings are to be obtained within the "get_player_info" function.
At present, the player name/number pairs are hard-coded.
Implementing another means of entering this information (text file, csv, etc.) should be straight-forward.
The 'requests' and 'BeautifulSoup' modules are used for the web scraping.
Data is saved to a text file and structured in the form of a table whose columns are player name, PDGA number, and player rating
Players with an inactive PDGA membership and therefore no publicly-viewable player rating are assigned the rating of 'EXPIRED'.


## Sample output:

Ratings as of 11-07-2020

Adam            82453           964  
Betsy           91988           EXPIRED  
Charles         74699           976  
Denise          16027           983  
Eric            79228           1008  
Flora           77244           936  
Greg            48559           1001  
Hilda           73385           EXPIRED  
Ivan            109496          871  


## Future work
* Define players of interest by contents of a text file or .csv file, rather than hardcoded
