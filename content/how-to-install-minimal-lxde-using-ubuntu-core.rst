How to install minimal lxde on ubuntu core ?
############################################
:date: 2012-12-10 16:47
:author: srikant
:category: blogs
:tags: armhf ubuntu, core ubuntu, lxde, minimal linux
:slug: how-to-install-minimal-lxde-using-ubuntu-core

For embedded development and testing, lxde is proved to be lightweight
and configurable desktop environment. Let's see how to install a minimal
lxde desktop on an ARM emulator setup.

.. raw:: html

   <div class="document">

Steps to perform

#. Download ubuntu 12.04 core image from `link`_

#. Now extract the core file system to some directory by issuing
   following command::


       sudo tar -xvpzhf /tmp/ubuntu-core-12.04.1-core-armhf.tar.gz

#. chroot into the directory with the help of qemu-arm-static and
   update `/etc/apt/sources.list` with universe & multiverse repositories, a sample content is as
   follows::

       deb http://ports.ubuntu.com/ubuntu-ports/ precise main universe multiverse restricted
       deb-src http://ports.ubuntu.com/ubuntu-ports/ precise main universe multiverse restricted

#. Now do apt-get update and followed by installation of following
   packages::

       apt-get install vim.tiny sudo ssh net-tools ethtool wireless-tools lxde xinit xorg network-manager iputils-ping rsyslog alsa-utils

That's it. You have successfully installed core minimal lxde without
any overheads of lubuntu. The entire setup should not take more than 400MB.

 

.. _link: http://cdimage.ubuntu.com/ubuntu-core/releases/12.04/release/ubuntu-core-12.04.1-core-armhf.tar.gz
