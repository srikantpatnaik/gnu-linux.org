Fix MySQL problem after dist-upgrade
####################################
:date: 2013-09-20 12:05
:author: tas_devil
:category: blogs
:tags: error, Job failed, MySQL
:slug: fix-mysql-problem-after-dist-upgrade

Often after doing ``dist-upgrade`` on Ubuntu using a command::

    sudo apt-get dist-upgrade

MySQL server fails to start throwing an error message::

    sudo service mysql start

    error:
    start: Job failed to start

Here is a simple solution to above problem ::

.. raw:: html

   <div id="outline-container-1" class="outline-3">

Create a backup of your existing MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

Use command ::

    sudo cp -r /var/lib/mysql ~/mysql-backup

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-2" class="outline-3">

Remove existing MySQL package and related files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-2">


    sudo apt-get purge mysql-server-5.1 mysql-common

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-3" class="outline-3">

Remove configuration files if any
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3">

remove files from ``/etc/mysql/`` ::

    sudo rm /etc/mysql/ -R

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-4" class="outline-3">

Restore and fix permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-4">

After a purge, you can restore back your backup files to
``/var/lib/mysql`` if they does not exist ::

    sudo mkdir /var/lib/mysql
    sudo cp -r ~/mysql-backup/* /var/lib/mysql

and fix the permissions::

    sudo chown root:root /var/lib/mysql/ -R

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-5" class="outline-3">

Reinstall MySQL
~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-5">

Now reinstall MySQL package ::

    sudo apt-get install mysql-server

This should fix the problem. Verify it using::

    sudo service mysql start


