How to add swap to existing Linux installation ?
################################################
:date: 2012-12-10 18:14
:author: srikant
:category: blogs
:tags: linux, mkswap, sdcard, swap, swapon
:slug: how-to-add-swap-to-existing-linux-installation

.. raw:: html

   <div class="document">

| In many embedded devices such as beagleboard, pandaboard, olimex etc
Linux boots
|  entirely from sdcard, many times we run out of RAM and obviously
forget to add
|  swap space during installation. The simplest way would be resizing
the existing rootfs
|  partition and make a new partition of desired space to accommodate
swap.

Add following lines to ``/etc/rc.local`` assuming you have similar nodes
in ``/dev/`` for sdcard

.. code:: literal-block

    mkswap /dev/mmcblk0p3
    swapon /dev/mmcblk0p3

| Here mmcblk0p3 is the newly created partition from existing ext4/ext3
rootfs partition. This
|  is a dirty but quick hack to add swap to your existing image.

.. raw:: html

   </div>

 
