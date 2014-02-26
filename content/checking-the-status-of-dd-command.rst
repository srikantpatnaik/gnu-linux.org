Checking the status of dd command 
##################################
:date: 2013-01-18 09:10
:author: srikant
:category: blogs
:tags: dd, dd size, grep, linux
:slug: checking-the-status-of-dd-command

A simple way to find the status(size copied) of dd command. Assuming you are running a single instance of dd, for eg, say on
terminal 1 you are running this::

    dd if=/dev/zero of=output.img bs=8k count=128k

The above command will take around 15 secs to create a 1GB+ image, to
know the status of dd open a new terminal(say, terminal 2) and type::

    kill -USR1 `pgrep ^dd$`

This won't actually kill any job. You won't see any output for the
above command. This will spit the status of dd on the terminal where dd
is actually running(terminal 1). Its very handy while dd'ing large data's.
