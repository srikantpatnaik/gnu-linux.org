Now don't reboot your linux system even after kernel update !
#############################################################
:date: 2012-03-24 18:03
:author: tas_devil
:category: news
:tags: admins, ELF, ksplice, linux kernel, no reboot
:slug: now-dont-reboot-your-linux-system-even-after-kernel-update

 

It's good news for system admin's, they don't have to reboot the system
after applying an important patch to the kernel. Thanx to **Ksplice**,
an Open source extension of linux kernel which allows admins to apply
patches to running kernel.

What ksplice does is, it only takes an unified diff of a patch, and
applies it to running kernel. It does this work in the memory. It
determines the change to be done on source code by analyzing the
Executable and Linking Format(ELF) object layer and not on C source
code. Ksplice freezes all the processors in the system and make sure it
is the only  process running at the time of patch. After applying a
patch, it resumes the processors and points all the functions to the
newly updated data and structures in the memory.

To use Ksplice you don't even need a special compiled kernel. You can
try Ksplice on ubuntu and fedora by visiting this `link`_

.. _link: http://www.ksplice.com/pricing
