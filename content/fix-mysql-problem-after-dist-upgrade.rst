Fix MySQL problem after dist-upgrade
####################################
:date: 2013-09-20 12:05
:author: tas_devil
:category: blogs
:tags: error, Job failed, MySQL
:slug: fix-mysql-problem-after-dist-upgrade

Often after doing ``dist-upgrade`` on Ubuntu using a command,

.. code-block:: identifier

    sudo apt-get dist-upgrade

MySQL server fails to start throwing an error message,

.. code-block:: identifier

    sudo service mysql start

.. code-block:: identifier

    error:
    start: Job failed to start

Here is a simple solution to above problem.

.. raw:: html

   <div id="outline-container-1" class="outline-3">

Create a backup of your existing MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

.. code-block:: identifier

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

.. code-block:: identifier

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

remove files from ``/etc/mysql/``

.. code-block:: identifier

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
``/var/lib/mysql`` if they does not exist.

.. code-block:: identifier

    sudo mkdir /var/lib/mysql
    sudo cp -r ~/mysql-backup/* /var/lib/mysql

and fix the permissions.

.. code-block:: identifier

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

Now reinstall MySQL package.

.. code-block:: identifier

    sudo apt-get install mysql-server

This should fix the problem. Verify it using,

.. code-block:: identifier

    sudo service mysql start

.. raw:: html

   </div>

.. raw:: html

   </div>

