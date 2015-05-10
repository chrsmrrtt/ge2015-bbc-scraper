# UK General Election 2015 Results - BBC Scraper

## Introducion
A simple Python3 web scraper that obtains constituency-level results of the 2015 UK General Election from the BBC website.

## Dependencies
This script has two module dependencies that are both available via pip: 1) requests; 2) BeautifulSoup4

## Output
The output is pipe-delimited with the following columns of data:

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

## Example
The results of this scrape as of 10 May 2015 can be found in the results.txt file.
