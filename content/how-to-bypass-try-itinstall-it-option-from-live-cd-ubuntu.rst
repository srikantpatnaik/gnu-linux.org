How to bypass 'try it/install it' option from Live CD Ubuntu ?
##############################################################
:date: 2011-12-08 12:42
:author: srikant
:category: blogs
:tags: kubuntu live boot, live cd, no boot splash, remove try it option, ubuntu customization
:slug: how-to-bypass-try-itinstall-it-option-from-live-cd-ubuntu

The purpose to eliminate the 'try it /Install it' option is to make it
easy to run.User don't have to wait for the pop up to select the Live
option anymore.All he need to do is insert the disc and reboot the
machine.After boot it will directly drop him to desktop.

This procedure will work for both Ubuntu and Kubuntu.I have chosen
Kubuntu here.

 

Download the latest Ubuntu iso file

1. Mount it using option ::

    sudo  mkdir /mnt/kubuntu && mount -o loop kubuntu-11.10.iso

2.  Create a directory at::

    sudo /mnt/kubuntu-rw .

3. Copy the content of /mnt/kubuntu to /mnt/kubuntu-rw .To edit some
files.We can't edit files inside the mounted content at /mnt/kubuntu::

    sudo cp -R  /mnt/kubuntu  /mnt/kubuntu-rw

4. Goto /mnt/kubuntu-rw/isolinux directory::

    cd  /mnt/kubuntu-rw/isolinux

5. Change the permission of file isolinux.cfg to u+w ::

     sudo chmod u+x isolinux.cfg

6. Edit the file isolinux.cfg. Replace all the content of the file with
given code::
   

    ::

        default live

    ::

         label live

    ::

         say Booting an Ubuntu Live session...

    ::

         kernel /casper/vmlinuz append file=/cdrom/preseed/ubuntu.seed boot=casper initrd=/casper/initrd.lz quiet splash --

     

7.  Change the permissions of isolinux.bin file .

     

    ::

        sudo chmod u+w isolinux.bin

     

8.  Create the iso file back from edited content of kubuntu-rw.Just go
up by two directories.

    cd ../../

    Then run this command.This will create the new iso file in /mnt directory::

    #. ::

           sudo mkisofs -r -V "Ubuntu Live session" -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o kubuntu-11.04-no-option.iso kubuntu-rw 

 

Now you are done . Burn the iso in the CD/DVD or boot in the virtualbox
to enjoy hassle free Live session.

Happy hacking :)

     
