Working with chroot environment
###############################
:date: 2013-02-25 11:59
:author: tas_devil
:category: blogs
:tags: chroot, chroot jail, chrooting, jail environment, linux
:slug: working-with-chroot-jail-environment

.. raw:: html

   <div id="outline-container-1" class="outline-3">

**What is chroot ?**
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

As its man page says, "*it is used to run commands or an interactive
shell with special root directory*\ ". It provides an environment to
test new packages in a secured way without touching an actual system. It
can be called as a virtual system with a new as an root(/) directory.

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-2" class="outline-3">

**Why chroot environment ?**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-2">

Suppose I have a new package to test and compile with many dependencies.
Also I may have to compile each and every dependent package till my
requirement for the test-package is met. This process can make my
development machine highly unstable or sometime unusable, this is
certainly not I want. The best way I can deal with this is to create a
virtual machine, I can use `Qemu`_ or `Virtual Box`_ for that or I can
make a ``chroot`` environment in a separate directory and start working.
``chroot`` environments are also used to host web-servers, so if at all
the web-server is compromised, not all the services are hampered and the
physical is still safe.

An advantage of having a ``chroot`` environment is the file-system is
totally isolated from the physical host. **chroot** has a separate
file-system inside the file-system, the difference is its uses a newly
created root(/) as its root directory.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-3" class="outline-3">

**Building a chroot environment**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3">

For ``chroot``, we need to create a file-system. The file hierarchy
within the directory is same as any other Linux file-system such as
``/root``, ``/usr``, ``/etc``, ``/bin``, ``/opt`` etc. We can make a
Debian chroot environment using **debootstrap** or ``rootstock``, both
are available for Ubuntu systems. In this post I will use debootstrap to
create a chroot environment.

Install **debootstrap** using,

.. code:: src

    sudo apt-get install debootstrap

We can specify a system architecture, a suite(release name) and a mirror
to download from in the ``debootstrap`` parameter.

The syntax is as follows,

.. code:: src

    debootstrap --arch ARCHITECTURE SUITE YOUR-ROOT-DIRECTORY MIRROR

for example, if I want arch to be ``i686`` of Ubuntu 12.04(precise) and
my root directory is **precise-chroot/** with mirror as
http://archive.ubuntu.com/ubuntu, then create directory for chroot

.. code:: src

    mkdir precise-chroot 

and create a chroot environment using debootstrap

.. code:: src

    debootstrap --arch i686 precise precise-chroot http://archive.ubuntu.com/ubuntu

this will create a chroot environment for Ubuntu 12.04, from the mirror.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-4" class="outline-3">

**Chrooting**
~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-4">

Once all the file are downloaded, we can chroot into precise-chroot/
directory using

.. code:: src

    sudo chroot precise-chroot /bin/bash

where ``precise-chroot`` is the root directory, and the shell is
``/bin/bash``. You will be landed with the root prompt. Now you can
setup the package manager and update it. This will work same as any
other Linux environment.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-5" class="outline-3">

**References**
~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-5">

-  visit the manual page, ``man chroot``
-  Guide to `rootstock`_
-  Why FreeBSD prefers `jail`_ instead of ``chroot``?

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _Qemu: http://wiki.qemu.org/Main_Page
.. _Virtual Box: https://www.virtualbox.org/
.. _rootstock: http://technoreview.net/2011/10/using-rootstock.html
.. _jail: http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/jails-intro.html
