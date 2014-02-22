Hack android pattern lock
#########################
:date: 2013-06-19 10:22
:author: tas_devil
:category: android
:tags: android, pattern unlock
:slug: hack-android-pattern-lock

.. raw:: html

   <div id="outline-container-1" class="outline-2">

How to bypass pattern lock on Android if you have made too many attempts
------------------------------------------------------------------------

.. raw:: html

   <div class="outline-text-2" id="text-1">

*Note*: This is tested on Aakash(AllWinner A13) but you may find the
scripts and reference useful

*Situation*: The attempt to unlock pattern was exceeded, so with no
Internet connection and no ``adb`` access how to delete the database
entries

*Solution*:

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-1" class="outline-3">

Downloading and burning an image on SD-card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-1">

-  Buy one 8 GB SD-card and download GNU/Linux image for Aakash from
   `here`_.
-  Extract that image using the command:: 

       tar -xvjf 12.10-lxde-bootLogo-0secUboot-expeyes-scilab-on-cloud-sleep1.img.bz2

-  You need to burn that extracted image to SD-card. Insert the SD-card
   in to the SD-card slot slot of your laptop/PC and run this command::


       sudo dd if=12.10-lxde_with_scilab_on_cloud_cleaned.img of=/dev/sdb bs=1024

   assuming your SD-card was detected as ``/dev/sdb``

-  Or you can use a simplified GUI `ddMaker`_ tool for burning an image.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-2" class="outline-3">

Booting with GNU/Linux image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-2">

-  Insert the SD-card in to the SD-card slot of the tablet and hold the
   *power* button until you see Aakash's boot-splash screen.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-3" class="outline-3">

Installing required dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-3">

-  You need to edit the ``settings.db`` file. This is sqlite's database
   file. You may need to install ``sqlite3`` on the tablet(GNU/Linux
   side). You can install it using ``apt-get``. On the terminal type::


       sudo apt-get install sqlite3

   give the password as ``123``

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-4" class="outline-3">

Mounting the NAND partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-4">

-  login as ``root`` ::

       sudo -s

   give the password as ``123``

-  Now you need to mount ``/dev/nande`` partition in which
   ``settings.db`` file resides.
-  Make a temporary directory for mounting NAND partition::

       mkdir -p /root/nande

   and mount the ``nande`` partition using the command::

       mount /dev/nande /root/nande

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-5" class="outline-3">

Update sqlite database
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-5">

-  Now change the directory in which ``settings.db`` file resides::

       cd nande/data/com.android.providers.settings/databases

   Make copy of 'settings.db' in case you mess up with the content of a
   file::

       cp -v settings.db settings.db-original

   and use the database file ::

       sqlite3 settings.db

   You will get an sqlite3 prompt saying::


       sqlite

-  Now update the database::

       update secure set value=0 where name='lock_pattern_autolock';

       update secure set value=0 where name='lockscreen.lockedoutpermanently';

   quit sqlite3 interface::

       .quit

-  Also remove the gesture key file::

       rm /data/system/gesture.key

-  Unmount the NAND partition::

       cd /root
       umount /dev/nande

-  poweroff the tablet::


       poweroff

-  Remove the SDcard and boot into Android

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-6" class="outline-3">

Using automated scripts
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-6">

-  If you decide to use the automated scripts from `github`_, you may
   also need to install ``python-pysqlite2``. This is python interface
   library for ``sqlite3``. The command to install is::


       sudo apt-get install python-pysqlite2

-  Copy both the scripts to ``/root`` directory of the tablet(GNU/Linux
   side) and execute the shell script ``pattern_unlock.sh``::

       cd unlock_android_pattern
       bash ./pattern_unlock.sh

-  Shutdown the tablet, remove the SD-card and restart it again. Your
   pattern lock mush have disappeared by now.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-7" class="outline-3">

Additional commands(sqlite3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1-7">

-  View description of table::

       pragma table_info([table_name])

   for example::


       pragma table_info([secure])

-  list all the tables in the database::

       .tables

FOR EDUCATIONAL PURPOSE ONLY!. We do not hold any responsibility if you
brick your phone/tablet.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _here: http://www.it.iitb.ac.in/AakashApps/repo/GNU-Linux-on-Aakash/12.10-lxde-bootLogo-0secUboot-expeyes-scilab-on-cloud-sleep1.img.bz2
.. _ddMaker: https://github.com/androportal/ddMaker
.. _github: https://github.com/psachin/bash_scripts/tree/master/unlock_android_pattern
