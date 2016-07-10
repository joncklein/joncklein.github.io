
# open the file - and read all of the lines.
changes_file = 'change.txt'
# use strip to strip out spaces and trim the line.
my_file = open(changes_file, 'r')
data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data)), 'Total lines'

#sperate lines on the 72 dashes
sep = 72*'-'

#commit class to hold the elements
class Commit:
    'class for commits'
   
   #intialise and declare the necessary variables
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

#lists and counts necessary to find interesting information
commits = []
current_commit = None
index = 0
authors = []
author = []
num_changes = []
#loop where the magic happens 
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        #split line into the different sections
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        #add to list
        authors.append(current_commit.author)
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        num_changes.append(current_commit.comment_line_count)
        current_commit.changes = data[index+2:data.index('',index+1)]
        
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

from collections import Counter

#retrieve and print information
print 'Total commits: ',(len(commits)), 'commits'
print 'Authors by number of commits', tuple(Counter(authors).most_common())
print 'list of authors: ',list((set(authors)))
print 'Lines changed during each commit',dict(Counter (num_changes))



