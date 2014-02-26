Grub Rescue commands 
#####################
:date: 2013-05-31 11:27
:author: camitr
:category: blogs
:tags: GRUB, grub-rescue, ubuntu grub rescue
:slug: grub-rescue-commands

The grub rescue> prompt comes when grub is missing. Some times if you
have dual boot system and you  delete any partition contains win 7. To
rewrite the partition table when you reboot, you can stuck with this
grub rescue prompt. Here you find no commands works, So dont panic
follow these steps, and you will get your lost child :D

Step 1. List the partition you have on the disk::

	grub-rescue> ls

Step 2. The above command display some partition and from these
partition find out which has /boot/grub,Which contains several .mod
files::

	grub-rescue> ls (hd0,5)/boot/grub

If you will find some files, it means this disk contains the grub
file, else search in other partitions

Step 3. set this partition ::

	grub-rescue> set prefix=(hd0,5)/boot/grub

Step 4. Now insert module on kernel using insmod (install loadable kernel module) command::

	grub-rescue> insmod normal

Step 5. Restart the machine::

	grub-rescue>normal

Now after the machine boot in linux update and install your grub .Open a terminal and type below commands::

	sudo update-grub

::

	sudo grub-install /dev/sda


