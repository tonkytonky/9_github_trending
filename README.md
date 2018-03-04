# Github Trends

This is the script for dumping information about recently created GitHub 
repositories. It returns defined number of the most popular repositories 
sorted by the number of stars and the number of open issues for which of them.


# Usage

To run the script you need Python 3.5 or higher to be installed. 

Example:
```bash
$ python github_trendinf.py -n 3 -d 7
issues: 1, link: https://github.com/nswbmw/node-in-debugging
issues: 7, link: https://github.com/wahyd4/work-in-australia
issues: 4, link: https://github.com/llSourcell/Learn_Machine_Learning_in_3_Months
```
`-n NUMBER` - number of repositories to get  
`-d DAYS` - number of days for which to get repositories


# Project Goals

The code is written for educational purposes. 
Training course for web-developers - [DEVMAN.org](https://devman.org)
