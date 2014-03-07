Add swap on ZTE Blade without swapper2
######################################
:date: 2013-10-01 12:47
:author: tas_devil
:category: android
:tags: swap, swapper2, zte blade
:slug: add-swap-on-zte-blade-without-swapper2

Idea Blade/ZTE Blade comes with 167 MB usable memory. Their is no way
you can install CyanogenMod9/10 in such a low RAM. However I took a
chance and installed CM9 and it slogs like hell. Swapper2 can be used to
add swap, but it adds another memory and space constraint. `drewhill77`_
came up with an excellent way to add swap without installing swapper2.
This is a simple way using which a swap is added in typical UNIX system.

In this post I will follow *drewhill77's* steps but I will confine it to
ZTE Blade. I assume CyanogenMod9 is pre-installed on the device. A
swap-file will be created on SD-card instead of using a partition.
Unlike *swapper2* which limits swap-file size to 256MB, this file-size
can be extended as long as size of the SD-card permits. Following
procedure may also work for other devices, provided they are rooted.
User should be familiar with shell commands and should be able to do
some system level jobs.

*drewhill77* have used terminal manager to execute all commands but I
prefer *adb* over it. Usage of `adb`_ is beyond the scope of this post.
After you enter the device shell using **adb** using::

    adb shell

Change to root
~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

First and foremost thing is to have root access to the device. In
CyanogenMod, a pre-installed *SuperUser* app with grant root access to
all applications as well as to file-system ::

    su

will give root access. The prompt will change from ``$`` to ``#``.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-2" class="outline-3">

Create a swap-file
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-2">

Create a swap-file with the name ``swapfile.swp`` on SD-card ::


    dd if=/dev/zero of=/mnt/sdcard/swapfile.swp bs=1048576 count=256

*count* is the size of swapfile in MB. I prefer 256 MB.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-3" class="outline-3">

Make swap and turn it on.
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3">

Once swapfile is created, which should not take more than a couple of
minutes. Convert it into swapfile(previously it was just a bunch of
zero's). And finally inform system to use it as a swap file or add it to
existing swap if is already exist ::

    mkswap /mnt/sdcard/swapfile.swp
    swapon /mnt/sdcard/swapfile.swp

Once swap is added, its time to confirm it using ``free`` command ::

    free -m

+---------+------------+----------+----------+-----------+-------+
| total   | used       | free     | shared   | buffers   |       |
+---------+------------+----------+----------+-----------+-------+
| Mem:    | 171296     | 165552   | 5744     | 0         | 104   |
+---------+------------+----------+----------+-----------+-------+
| -/+     | buffers:   | 165448   | 5848     |           |       |
+---------+------------+----------+----------+-----------+-------+
| Swap:   | 262136     | 114888   | 147248   |           |       |
+---------+------------+----------+----------+-----------+-------+

The swap will be added as seen in *Swap* column.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-4" class="outline-3">

Swappiness
~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-4">

Now the swap is added and it is in use but the kernel will not use it at
the fullest if *swappiness* is not set properly. *Swappiness* decides
how aggressively you want the kernel to use swap. It's value ranges from
0 to 100. The lower value means kernel will try to avoid using swap
whereas for higher value it will use swap as much as possible. For most
systems, the default value is set to 60. One can check the value of
swappiness by reading the file ``/proc/sys/vm/swappiness`` ::

    cat /proc/sys/vm/swappiness

Change the value using::

    echo 70 /proc/sys/vm/swappiness

or using::


    sysctl -w vm.swappiness=70

Go ahead and change swappiness from 60 to 100::

    echo 100 /proc/sys/vm/swappiness

and verify the value from the file ``swappiness``.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-5" class="outline-3">

Make all the changes persistent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-5">

Now that the swap is been created & added to the system and the
swappiness is set, it's time to make all the changes persistent on every
boot. The swapfile on the SD-card will remain as it is, but ``swapon``
should be run and desired value of swappiness is to be set. Some shell
scripts should do these jobs. *drewhill77* has already uploaded shell
scripts for variety of purpose.

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-5-1" class="outline-4">

swapon
^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-5-1">

As swapfile should be added to system after a boot, it is better to add
this command to system's init. The best place is the
``/data/local/userinit.d/`` directory. If you scan the content of
``/etc/init.d/90userinit`` file, it looks for user init files under the
directory ``/data/local/userinit.d/``. Create the directory if it does
not exist::

    mkdir -p /data/local/userinit.d

and add the shell script ``99swapon`` with below lines.


    #!/system/bin/sh
    sleep 75
    swapon /mnt/sdcard/swapfile.swp
    sysctl -p

Line 1 is the *shebang* line which identifies the file as a shell
script.

Line 2 is the ``sleep`` command with sleep interval of 75 seconds before
it executes line 3 which actually adds swap. SD-card is always mounted
at the end. As a result it is safe to add swap with some intervals after
system boots. Make the file executable::


    chmod +x /data/local/userinit.d/99swapon

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-5-2" class="outline-4">

swappiness
^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-5-2">

The second thing is to set default *swappiness* value. It can be done
from ``/etc/sysctl.conf`` file. ``/etc`` is write protected and it has
to be remounted as writable before creating a file::

    busybox mount -o remount,rw /system

and add below line in the file ``/etc/sysctl.conf``. Create a new file
if does not exist::

    vm.swappiness=100

.. raw:: html

   <div class="figure">

|58MB of free RAM after adding swap.|

58MB of free RAM after adding swap.

.. raw:: html

   </div>

Reboot the phone and you should have swap added with swappiness of 100.
Read last section of `drewhill77`_ post for a brief note on swapping.


.. _drewhill77: http://androidforums.com/boost-mobile-warp-all-things-root/610449-ram-swapping-without-swapper2.html
.. _adb: http://developer.android.com/tools/help/adb.html

.. |58MB of free RAM after adding swap.| image:: http://gnu-linux.org/uploads/2013/10/running_apps.png
