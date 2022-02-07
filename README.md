
A tool to retrieve the player ratings of any number of tournament disc golfers


### Introduction


Player ratings are calculated by the [Professional Disc Golf Association](https://www.pdga.com) using scores from recent tournaments.
The precise algorithm is proprietary but likely involves weighted averaging of individual round ratings obtained by linear regression.

The utility of this repo is the ability to simultaneously gather ratings (generally in the vicinity of a rating update) without having to visit invidual URL's.
The use case for which this software was designed involved selecting a team of disc golfers based on highest rating.


### Method
For an input list of player names and numbers, use the `requests` and `BeautifulSoup` modules in Python to web scrape data and save into a text file.



#### Input

A text file in which each row is of the form:  

`[PLAYER_NAME]: [PDGA_NUMBER]`  

The file must be located same directory as the other scripts. 
A sample input file is shown below and also included in the repo (`sample-players.txt`).  If desired, it may be editted to the particular players of interest.

![input](./sample-players.png)

`[PLAYER_NAME]` is not required to match the name the PDGA associates with `[PDGA_NUMBER]` so a nickname may be used if desired.
As an example, the official name of PDGA number 37817 is 'Eagle Wynne McMahon' rather than 'Eagle McMahon' as is listed in the sample input file.





#### Output
A text file where each row has columns of player name, PDGA number, and current playing rating.

If an individual on the input list is not an active PDGA member (probably because their yearly registration has lapsed), a value of `EXPIRED` is assigned.
An example of typical output is also included in the repo (`sample-players-ratings-02-06-2022.txt`) and also displayed below.

![output](./sample-players-ratings-02-06-2022.png)

The output file may be given an arbitrary name but a default name is generated for convenience.


A text file was selected for both easy viewing and importing into other software for subsequent analysis.

