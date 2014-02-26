improve performance by reducing swappiness in ubuntu
####################################################
:date: 2012-12-14 11:28
:author: Srikant Patnaik
:category: blogs
:tags: RAM, swap, swappiness, ubuntu
:slug: improve-performance-by-reducing-swappiness-in-ubuntu

A simple lag in your computer is noticeable and annoying. When your
RAM is hosting inactive data (for eg: Openoffice, unused tabs from
browser, media player paused etc) it tends to move it to swap partition
which is in most cases a hard drive which is much slower than your RAM.
The free'd RAM is used for active processes.

This all seems smart & obvious, but if you check your RAM usage by::

    free -m

you will notice that almost half of the RAM is available, and if you
observe carefully you will find that your swap is used after some
percentage of RAM is used. To control the swap usage *swappiness* value
is used. To check extent of swap usage for your machine just issue::

    cat /proc/sys/vm/swappiness

This will print 60 for default ubuntu installation. The value can be
anything between 0 to 100. `0` means no swap usage and 100 means use extensively.
A value of 20 will works well for machine with 2 GB or more RAM. To set value permanently, open
the following file ::

	gksudo gedit /etc/sysctl.conf

and enter this value at the end of the page::

	vm.swappiness=10

save the file and reboot your machine.
