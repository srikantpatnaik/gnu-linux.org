Mount Android phone on your local machine over Wifi !
#####################################################
:date: 2011-12-13 16:08
:author: srikant
:category: android
:tags: android, android wifi mount, file transfer android, fuse filesystem, fuser, mount sdcard, sshdroid, sshfs
:slug: mount-android-phone-on-your-local-machine

Have you ever tried to copy a movie or song from your PC but you forgot
your data cable.This happens very often.We don't carry accessories all
the time.The best solution to this is accessing your phone over
Wifi(Internet is not required) .

Using \ `sshfs`_ package one can mount remote file systems on local
machines with the help of fuse filesystem.

Steps to follow :

1. First install *sshfs* from your distribution archives. For debian
based system just type

    sudo apt-get install sshfs

2. Then add present user to fuse group.In place of user1 use your
username .

    sudo adduser user1 fuse

3. Create a directory where you want to mount your phone's SD card.

    mkdir my-phone

4. Connect your phone with wifi and know its IP address.Make sure that
your phone and PC both are in same network.

It needs *sshdroid* package to be installed on your android phone.

5. Now run this command in your terminal.

    sshfs -o idmap=user root@192.168.1.3:/mnt/sdcard  my-phone

Accept the certificate and enter the root password of your phone.For
*sshdroid* its 'admin'.

6. Now go to my-phone directory and you can see your phone's SD card's
contents there.

7. To umount just use

    fusermount -uz my-phone

 

Enjoy wireless mounting.

 

     

 

.. _sshfs: http://fuse.sourceforge.net/sshfs.html
