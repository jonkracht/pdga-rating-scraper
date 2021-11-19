# pdga_rating_scraper

## Purpose
A Python script to grab disc golfers' player ratings from pdga.com, the website of the Professional Disc Golf Association.


## Use
The user must specify the players for whom ratings are to be obtained within the "get_player_info" function.  At present, the player name/player numbers pairs are hard-coded but other data entry methods should be straight-forward (ex. reading from a text file or csv).  Data is collected within a dictionary, optionally printed to the standard out and saved as a text file.  


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

(Players with an inactive PDGA membership and therefore no publicly-viewable player rating are assigned the rating of 'EXPIRED'.)
