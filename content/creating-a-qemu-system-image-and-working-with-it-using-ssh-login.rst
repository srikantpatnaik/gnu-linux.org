Creating a qemu system image and working with it using ssh login
################################################################
:date: 2012-08-23 07:49
:author: tas_devil
:category: blogs
:tags: -vnc none, linux, qemu, qemu-system, redir, ssh
:slug: creating-a-qemu-system-image-and-working-with-it-using-ssh-login

In this post I will create a Qemu image and work with it remotely using
ssh login.

.. raw:: html

   <div id="outline-container-1" class="outline-3">

Steps
~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

#. Download and install qemu from this `link`_.
#. Create a raw image, install `ubuntu 12.04`_ from an ISO image.
#. Boot from an installed image and redirect its port ``22`` to port
   ``2200`` of ``localhost``.
#. Create snapshot of an image.
#. Booting snapshot image.
#. Tips.
#. References.

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-1" class="outline-4">

**1. Download and install qemu**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-1">

If you are having Debian based distro, ubuntu may be, then you can
install qemu using the command ::


    sudo apt-get install qemu-system

this will install all qemu-system binaries for all major cpu
architectures. If you are having RPM based distro(like fedora etc.),
first login as root and type ::

    yum install qemu

else you can also compile the latest stable `source`_. Please refer the
README for compilation instructions.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-2" class="outline-4">

**2. Creating and installing image**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-2">

We need to first create a raw qemu image using command ::


    qemu-img create -f raw IMAGE_NAME.img SIZE

for example, if I want to create an image of ``32G`` with name as
``ics-testing.img`` then ::

    qemu-img create -f raw ics-testing.img 32G

Once the image is created, we can use it as a raw disk image and install
an OS. In this case I will install `ubuntu
12.04 <http://releases.ubuntu.com/12.04/ubuntu-12.04-desktop-amd64.iso>`__
(AMD64) from an iso image.

The syntax would be ::

    qemu-system-ARCH -vnc none,ipv4 -hda IMAGE_NAME -cdrom /PATH/TO/ISO/FILE -m MEMORY -enable-kvm

for example, if my system arch is ``x86-64`` and my iso location is
``/home/devils/iso/ubuntu-12.04-desktop-amd64.iso`` with memory as
``4G``. Also I want to enable kernel based virtualisation ::

    qemu-system-x86_64 -vnc none,ipv4 -hda ics-testing.img \
    -cdrom /home/devils/iso/ubuntu-12.04-desktop-amd64.iso \
    -m 4096 -enable-kvm

this will pop up a qemu window. Proceed with the installation and reboot
the system.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-3" class="outline-4">

**3. Booting an installed image**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-3">

Once the installation is complete, boot the image by typing ::

    qemu-system-x86_64 -vnc none,ipv4 -hda ics-testing.img \
    -m 4096 -enable-kvm

now configure the system, its package manager and user's account.
Install Openssh-server and enable ssh logins. If everything is
configured, start qemu using ::

    qemu-system-x86_64 -vnc none,ipv4 -hda ics-testing.img \
    -m 4096 -enable-kvm \
    -redir tcp:2200::22

The ``-redir tcp:2200::22`` redirects TCP traffic on the host port
``2200`` to the guest machine (QEMU) port ``22``. This will allow us to
SSH into the machine later by connecting to ``localhost`` on port
``2200``.

``-vnc none`` will disble the vnc server.

-  ssh into qemu

   You can ssh into the running qemu system using a command ::

       ssh -p PORT USER@IP-Address or HOSTNAME

   for example, if I want to connect to port ``2200`` of ``localhost``
   with username as ``qemu-user``, then ::

       ssh -p 2200 qemu-user@localhost

   as port ``2200`` on ``localhost`` is open and is binded with port
   ``22`` of qemu system, so we will use ``-p 2200`` as one of the
   parameter.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-4" class="outline-4">

**4. Creating snapshots of an image**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-4">

Now as the image is configured and working, we can also create a
snapshots of that image and work on it keeping an original image intact.

syntax::

    qemu-img create -f qcow2 -b ORIGINAL_IMAGE_NAME SNAPSHOT_IMAGE_NAME

for example if my original image name is ``ics-testing.img`` and my
snapshot image name is ``snapshot.img``, then ::


    qemu-img create -f qcow2 -b ics-testing.img snapshot.img

``-f`` flag will specify image format. In this case it is ``qcow2``
which is most versatile qemu-image format. Please refer man-pages for
more detail.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-5" class="outline-4">

**5. Booting snapshot image**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-5">

You can use the snapshot image using ::


    qemu-system-x86_64 -vnc none -hda snapshot.img \
    -m 4096 -enable-kvm \
    -redir tcp:2200::22

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-6" class="outline-4">

**6. Tips**
^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-6">

a. You can also specify number of CPU cores using ``-smp`` flag. For
example, if you want to assign 4 cores of your physical system to qemu,
then specific it as ``-smp 4``. ``smp`` stands for
`Symmetric-multiprocessing`_.

b. If you run qemu over the snapshot image, it will corrupt the snapshot
image.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-1-7" class="outline-4">

**7. Refs.**
^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1-7">

#. `Qemu`_
#. `Ubuntu 12.04`_
#. `Creating snapshots`_

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _link: http://wiki.qemu.org/Main_Page
.. _ubuntu 12.04: http://releases.ubuntu.com/12.04/
.. _source: http://wiki.qemu.org/download/qemu-1.2.0-rc0.tar.bz2
.. _Symmetric-multiprocessing: http://en.wikipedia.org/wiki/Symmetric_multiprocessing
.. _Qemu: http://wiki.qemu.org/Main_Page
.. _Ubuntu 12.04: http://releases.ubuntu.com/12.04/
.. _Creating snapshots: http://wiki.qemu.org/Documentation/CreateSnapshot
