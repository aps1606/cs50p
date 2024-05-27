import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r".+src=\".+embed/(.*?)\".*",s):
        link = matches.group(1)
        return "https://youtu.be/" + link


if __name__ == "__main__":
    main()




'''
Psuedo/notes

Regex:
- only portion we from below is xvFZjo5PgG0
- check pattern to get portion in between: src=" and the following double quotation marks (so use non-greedy) 

The input could be:

<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" 
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

OR

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>


Additionally, the specific YT links in the above could be 1 of 3 types below:
 - http://youtube.com/embed/xvFZjo5PgG0
 - https://youtube.com/embed/xvFZjo5PgG0
 - https://www.youtube.com/embed/xvFZjo5PgG0








'''