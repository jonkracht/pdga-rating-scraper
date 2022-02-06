### Motivation
A tool to automatically retrieve the current player ratings for a list of tournament disc golfers from the website of the Professional Disc Golf Association ([pdga.com](https://www.pdga.com)).

### Method
Use Python modules `requests` and `BeautifulSoup` to web scrape.



### Input
A text file in which each row is of the form:  `[PLAYER_NAME]: [PDGA_NUMBER]`.  The file must be located in this repo.  A template textfile (`sample-players.txt`) is included in this repo and, if desired, can be modified to the actual players of interest.

### Output
A text file where each row has columns of player name, player PDGA numbers, and current playing rating.
If the person of interest is not an active PDGA member (i.e. their registration has lapsed), a value of `EXPIRED` listed in the rating column.
An example of typical output is also included (`sample-players-ratings-02-06-2022.txt`).

