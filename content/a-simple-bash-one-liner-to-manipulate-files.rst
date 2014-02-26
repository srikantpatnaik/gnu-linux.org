a simple bash one liner to manipulate files
###########################################
:date: 2013-01-19 23:54
:author: srikant
:category: blogs
:tags: bash, linux commands
:slug: a-simple-bash-one-liner-to-manipulate-files

I had to do create a single file from bunch of csv files, and also
append serial numbers as first field in the resultant file after
removing the duplicate entries.

| Sample content of one of the csv file.

|  xx:yy:xx:tt:rr:pp

|  xx:yy:xx:tt:rr:xx

|  xx:yy:xx:tt:rr:xx

|  .................

There were more than 20 such files with each having approx 50 MAC
addresses. So I need to concatenate all those entries and put them
something like this:

|  1,xx:yy:xx:tt:rr:pp

|  2,xx:yy:xx:tt:rr:xx

|  3,xx:yy:xx:tt:rr:uu

|  ...................

I know this is not a perfect way to do, but I can't think of better.
I'm more lazy than it seems.
It works though. Please suggest modifications::

    seq `cat *.csv | uniq | wc -l` > 1.txt ; cat *.csv | uniq | paste -d " " 1.txt - > final.txt ;rm 1.txt

