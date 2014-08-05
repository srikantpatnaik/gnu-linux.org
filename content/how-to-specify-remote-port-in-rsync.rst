How to specify remote port in rsync
###################################
:date: 2012-08-23 12:14
:author: tas_devil
:category: blogs
:tags: --inplace, --progress, -rsh, linux, port, rsync
:slug: how-to-specify-remote-port-in-rsync

In connection to `my post`_, wherein my virtual machine can be accessed
via ssh on port ``2200`` of the physical system. Rsync takes port ``22``
as its default port. So if I want to sync any data on that virtual
system, I have to tell rsync on which port it should connect to.

The syntax would be ::

    rsync --rsh='COMMAND' FILE USER@HOST:~

if my remote port is ``2200``, then ::

    rsync --rsh='ssh -p2200' ubuntu.img andro@darkstar:~

``--rsh`` flag specifies the remote-shell command, here we are using the
command ``ssh`` with port as ``2200``.

Tip

If you want to see progress of file transfer, add
``--progress --inplace`` flags.

.. _my post: creating-a-qemu-system-image-and-working-with-it-using-ssh-login.html
