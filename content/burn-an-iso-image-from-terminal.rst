burn an iso image from terminal
###############################
:date: 2012-03-25 20:01
:author: tas_devil
:category: blogs
:tags: burnfree, iso, linux, terminal, wodim
:slug: burn-an-iso-image-from-terminal

 

Now you can burn an ISO image directly from your terminal, no need for
any GUI tool.

The utility is called **wodim**, its derived from the tool **cdrecord**.
To check for devices, on you system, simply type ::

 wodim --devices
 

This will show an output some thing similar to this ::

`` wodim: Overview of accessible drives (1 found) : ------------------------------------------------------------------------- 0  dev='/dev/sr0'    rwrw-- : 'TEAC' 'DV-W28S-WT' -------------------------------------------------------------------------``

this shows that you are having an optical recorder at ``/dev/sr0``.

 

SYNTAX::

`` wodim -v -sao dev= driveropts=burnfree </path/to/iso/image-file>``

EXAMPLE::

	 wodim -v -sao dev=/dev/sr0 driveropts=burnfree ~/iso-images/fedora-16.iso

 **sao** is session at once (no multi-sessions), this is default
option during burning an ISO image. also **burnfree** turns on the
buffer underrun technology.

for more info, visit the man page, `man wodim`
