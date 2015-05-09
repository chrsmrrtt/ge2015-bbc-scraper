# ge2015-bbc-scraper
A simple Python3 web scraper that obtains constituency-level results of the 2015 UK General Election from the BBC website.

This script has two module dependencies that are both available via pip: 1) requests; 2) BeautifulSoup4

The output is pipe-delimited with the following columns:

* Constituency name
* Constituency nation
* Constituency code (useful for matching to other datasets)
* Constituency turnout percentage
* Candidate party short name
* Candidate party long name
* Candidate name
* Candidate vote count
* Candidate vote share percentage
* Candidate net vote share percentage gain/loss

The results of this scrape as of 10 May 2015 can be found in the results.txt file.