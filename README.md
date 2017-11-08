
# Logs Analysis Project

## Summary
Reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

#### Instructions
Program is writen in Python3 programing language. Run ```python3 psql_project.py``` in terminal.
For more details please see Installation section.

### Reporting tool functions
Reporting tool is based on python script with three main functions:
* ```get_most_popular_articles()```
    * Function will return the most popular three articles of all time.
* ```get_most_popular_authors()```
    * Function will return the most viewed author.
* ```get_lead_errors()```
    * Function will return days with more than 1% of requests lead to error.

## Links to GitHub Repository (Master Branch)
* GitHub Project Repository: [https://github.com/micond/psql_project](https://github.com/micond/psql_project "GitHub project repository")

## Installation
Installation instructions are for Linux debian based distributions.

1. Download the GitHub zip file or clone the repository onto your local workstation:
	* zip file [https://github.com/micond/psql_project/archive/master.zip](https://github.com/micond/psql_project/archive/master.zip "download zip file")
	* git clone [https://github.com/micond/psql_project.git](https://github.com/micond/psql_project.git "git clone repository")
2. Install [Python3](https://www.python.org/)
3. Install python library psycopg2 via pip install: ```pip install psycopg2```
   If pip not available: ```sudo apt-get install python-psycopg2```
4. For database replication please follow this UDACITY instrucionts [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91):
5. Open terminal and navigate to the psql_project.py file in your application's directory.
6. To run the application please run ```python3 psql_project.py``` in terminal.

## Tools / Techniques
- Python 3
- Postgresql
- VM Linux - Debian distribution

## List of Resources

- [Python 3](https://www.python.org/)
- [PEP8 style guide ](https://www.python.org/dev/peps/pep-0008/)
- [Postgresql](https://www.postgresql.org/)
- [Oracle - VirtualBox Linux - Debian distribution](https://www.virtualbox.org/)
- Recommended Linux Distributions [Ubuntu](https://www.ubuntu.com/) , [Mint](https://linuxmint.com/)

# Project Specification

####  submission:
https://review.udacity.com/#!/rubrics/277/view
