Writing UDEV rules for flash drive
##################################
:date: 2012-01-01 16:06
:author: tas_devil
:category: blogs
:tags: drive, flash, udev
:slug: writing-udev-rules-for-flash-drive

According to Daniel Drake
(**http://www.reactivated.net/writing\_udev\_rules.html**), "udev is the
new way of managing ``/dev`` directories...". It creates ``/dev`` device
nodes corresponding to the device that are present in the system. It
relies on matching information provided by ``sysfs`` and rules provided
by user. It can directly listen to kernel events when the device is
plugged in/out using Netlink. In short, udev is a successor of ``devfs``
and hotplug ``sysfs`` which makes device visible to user space. Udev
depends on ``/proc`` and ``/sys`` file system and that must be mounted
beforehand.

What exactly happens is, when you plug or unplug any device, a kernel
sent a bunch of data using a Netlink socket. Udev listens to this
Netlink socket that the kernel uses for communication with the user
applications. So the udev daemon catches all this data and creates
device nodes or loads a module.

In this article, I am going to write an udev rules which will logs an
entry in ``/var/log/`` when I plug/unplug a flash drive. I will use a
shell script which will handle logs. This shell script will be triggered
by udev rules when any kernel event related to the flash drive is caught
by udev daemon.

By default whenever I plug in a flash drive, it takes a device node as
``/dev/sdb1``. But the naming changes when I plug two flash drives with
mine as a second one. This time the first flash drive takes a name as
``/dev/sdb1`` and my flash drive takes the name as ``/dev/sdc1``. All I
want is, my flash drive to be detected as ``/dev/my_flash`` every time I
plug it in any order.

So I will write a udev rules which will create a SYMLINK to the device node based upon device attributes.

I have to know the sysfs device path of the flash drive. This should be
in ``/sys/block``, as it's a block device.

login as a root and type:

    ::

        root@zyro:~# udevadm info -a -p /sys/block/sdb/

remember that my flash drive was detected as ``/dev/sdb1`` as a result
``/sdb/`` is the root device

*output:*

    ::

        Udevadm info starts with the device specified by the devpath and then
        walks up the chain of parent devices. It prints for every device
        found, all possible attributes in the udev rules key format.
        A rule to match, can be composed by the attributes of the device
        and the attributes from one single parent device.

        looking at device '/devices/pci0000:00/0000:00:13.5/usb1/1-9/1-9:1.0/host6/target6:0:0/6:0:0:0/block/sdb':
        KERNEL=="sdb"
        SUBSYSTEM=="block"
        DRIVER==""
        ATTR{range}=="16"
        ATTR{ext_range}=="256"
        ATTR{removable}=="1"
        ATTR{ro}=="0"
        ATTR{size}=="31690752"
        ATTR{alignment_offset}=="0"
        ATTR{discard_alignment}=="0"
        ATTR{capability}=="51"
        ATTR{stat}=="42 250 2336 127 0 0 0 0 0 80 127"
        ATTR{inflight}=="0 0"
        ATTR{events}=="media_change"
        ATTR{events_async}==""
        ATTR{events_poll_msecs}=="-1"

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1/1-9/1-9:1.0/host6/target6:0:0/6:0:0:0':
        KERNELS=="6:0:0:0"
        SUBSYSTEMS=="scsi"
        DRIVERS=="sd"
        ATTRS{device_blocked}=="0"
        ATTRS{type}=="0"
        ATTRS{scsi_level}=="0"
        ATTRS{vendor}=="Sony    "
        ATTRS{model}=="Storage Media   "
        ATTRS{rev}=="0100"
        ATTRS{state}=="running"
        ATTRS{timeout}=="30"
        ATTRS{iocounterbits}=="32"
        ATTRS{iorequest_cnt}=="0x35b"
        ATTRS{iodone_cnt}=="0x35b"
        ATTRS{ioerr_cnt}=="0x1"
        ATTRS{modalias}=="scsi:t-0x00"
        ATTRS{evt_media_change}=="0"
        ATTRS{dh_state}=="detached"
        ATTRS{queue_depth}=="1"
        ATTRS{queue_type}=="none"
        ATTRS{max_sectors}=="240"

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1/1-9/1-9:1.0/host6/target6:0:0':
        KERNELS=="target6:0:0"
        SUBSYSTEMS=="scsi"
        DRIVERS==""

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1/1-9/1-9:1.0/host6':
        KERNELS=="host6"
        SUBSYSTEMS=="scsi"
        DRIVERS==""

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1/1-9/1-9:1.0':
        KERNELS=="1-9:1.0"
        SUBSYSTEMS=="usb"
        DRIVERS=="usb-storage"
        ATTRS{bInterfaceNumber}=="00"
        ATTRS{bAlternateSetting}==" 0"
        ATTRS{bNumEndpoints}=="02"
        ATTRS{bInterfaceClass}=="08"
        ATTRS{bInterfaceSubClass}=="06"
        ATTRS{bInterfaceProtocol}=="50"
        ATTRS{modalias}=="usb:v054Cp0439d0100dc00dsc00dp00ic08isc06ip50"
        ATTRS{supports_autosuspend}=="1"

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1/1-9':
        KERNELS=="1-9"
        SUBSYSTEMS=="usb"
        DRIVERS=="usb"
        ATTRS{configuration}==""
        ATTRS{bNumInterfaces}==" 1"
        ATTRS{bConfigurationValue}=="1"
        ATTRS{bmAttributes}=="80"
        ATTRS{bMaxPower}=="200mA"
        ATTRS{urbnum}=="1805"
        ATTRS{idVendor}=="054c"
        ATTRS{idProduct}=="0439"
        ATTRS{bcdDevice}=="0100"
        ATTRS{bDeviceClass}=="00"
        ATTRS{bDeviceSubClass}=="00"
        ATTRS{bDeviceProtocol}=="00"
        ATTRS{bNumConfigurations}=="1"
        ATTRS{bMaxPacketSize0}=="64"
        ATTRS{speed}=="480"
        ATTRS{busnum}=="1"
        ATTRS{devnum}=="6"
        ATTRS{devpath}=="9"
        ATTRS{version}==" 2.00"
        ATTRS{maxchild}=="0"
        ATTRS{quirks}=="0x0"
        ATTRS{avoid_reset_quirk}=="0"
        ATTRS{authorized}=="1"
        ATTRS{manufacturer}=="Sony"
        ATTRS{product}=="Storage Media"
        ATTRS{serial}=="7B4211105063000914"

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1':
        KERNELS=="usb1"
        SUBSYSTEMS=="usb"
        DRIVERS=="usb"
        ATTRS{configuration}==""
        ATTRS{bNumInterfaces}==" 1"
        ATTRS{bConfigurationValue}=="1"
        ATTRS{bmAttributes}=="e0"
        ATTRS{bMaxPower}=="  0mA"
        ATTRS{urbnum}=="111"
        ATTRS{idVendor}=="1d6b"
        ATTRS{idProduct}=="0002"
        ATTRS{bcdDevice}=="0300"
        ATTRS{bDeviceClass}=="09"
        ATTRS{bDeviceSubClass}=="00"
        ATTRS{bDeviceProtocol}=="00"
        ATTRS{bNumConfigurations}=="1"
        ATTRS{bMaxPacketSize0}=="64"
        ATTRS{speed}=="480"
        ATTRS{busnum}=="1"
        ATTRS{devnum}=="1"
        ATTRS{devpath}=="0"
        ATTRS{version}==" 2.00"
        ATTRS{maxchild}=="10"
        ATTRS{quirks}=="0x0"
        ATTRS{avoid_reset_quirk}=="0"
        ATTRS{authorized}=="1"
        ATTRS{manufacturer}=="Linux 3.0.8-smp ehci_hcd"
        ATTRS{product}=="EHCI Host Controller"
        ATTRS{serial}=="0000:00:13.5"
        ATTRS{authorized_default}=="1"

        looking at parent device '/devices/pci0000:00/0000:00:13.5':
        KERNELS=="0000:00:13.5"
        SUBSYSTEMS=="pci"
        DRIVERS=="ehci_hcd"
        ATTRS{vendor}=="0x1002"
        ATTRS{device}=="0x4386"
        ATTRS{subsystem_vendor}=="0x1043"
        ATTRS{subsystem_device}=="0x81ef"
        ATTRS{class}=="0x0c0320"
        ATTRS{irq}=="19"
        ATTRS{local_cpus}=="f"
        ATTRS{local_cpulist}=="0-3"
        ATTRS{modalias}=="pci:v00001002d00004386sv00001043sd000081EFbc0Csc03i20"
        ATTRS{dma_mask_bits}=="32"
        ATTRS{consistent_dma_mask_bits}=="32"
        ATTRS{enable}=="1"
        ATTRS{broken_parity_status}=="0"
        ATTRS{msi_bus}==""
        ATTRS{companion}==""

        looking at parent device '/devices/pci0000:00':
        KERNELS=="pci0000:00"
        SUBSYSTEMS==""
        DRIVERS==""

the output is list of attributes from a single parent device. We can use
as many attributes from a single parent but we can't mix match
attributes from multiple parent device.

Create a file in ``/etc/udev/rules.d/`` as ``10-local.rules``. As a
note, all udev rules are kept in ``/dev/udev/rules.d/`` directory and
the rules file must have a .rules suffix.

All default rules are kept in ``/etc/udev/rules.d/50-udev.rules``. Files
in ``/etc/udev/rules.d/`` as parsed in lexical order. So I am going to
write all my rules in 10-local.rules. This file will be read before udev
default rules file.

I will use attributes from the following parent device:

    ::

        looking at parent device '/devices/pci0000:00/0000:00:13.5/usb1/1-9':
        KERNELS=="1-9"
        SUBSYSTEMS=="usb"
        DRIVERS=="usb"
        ATTRS{configuration}==""
        ATTRS{bNumInterfaces}==" 1"
        ATTRS{bConfigurationValue}=="1"
        ATTRS{bmAttributes}=="80"
        ATTRS{bMaxPower}=="200mA"
        ATTRS{urbnum}=="1805"
        ATTRS{idVendor}=="054c"
        ATTRS{idProduct}=="0439"
        ATTRS{bcdDevice}=="0100"
        ATTRS{bDeviceClass}=="00"
        ATTRS{bDeviceSubClass}=="00"
        ATTRS{bDeviceProtocol}=="00"
        ATTRS{bNumConfigurations}=="1"
        ATTRS{bMaxPacketSize0}=="64"
        ATTRS{speed}=="480"
        ATTRS{busnum}=="1"
        ATTRS{devnum}=="6"
        ATTRS{devpath}=="9"
        ATTRS{version}==" 2.00"
        ATTRS{maxchild}=="0"
        ATTRS{quirks}=="0x0"
        ATTRS{avoid_reset_quirk}=="0"
        ATTRS{authorized}=="1"
        ATTRS{manufacturer}=="Sony"
        ATTRS{product}=="Storage Media"
        ATTRS{serial}=="7B4211105063000914"

My selected attributes are:
 
`SUBSYSTEMS=="usb" ATTRS{idVendor}=="054c" ATTRS{idProduct}=="0439" ATTRS{serial}=="7B4211105063000914"`

each rules is constructed using a series of key-values pairs. In the
above case, key-value(SUBSYSTEMS) is compared with value(usb) and so on.

Now I have decide my basic device attributes, lets monitor the kernel
events. This can be done using:

    ::
       root@zyro:~# udevadm monitor

This command will wait for any kernel event. Now if I remove the flash
drive, it will display all events related to key-value pair

``ACTION=="remove"``. In the same way, if I plug the flash device again,
it will log all the entry related to ``ACTION="add"``.

So there will an additional attributes in

	`/etc/udev/rules.d/10-local.rules`

	`ACTION=="add" ACTION=="remove"`

*file: /etc/udev/rules.d/10-local.rules*

    ::

        KERNEL=="sd[a-d][0-9]", SUBSYSTEMS=="usb", ATTRS{idVendor}=="054c", ATTRS{idProduct}=="0439", ATTRS{serial}=="7B4211105063000914", SYMLINK+="myflash"
        ACTION=="add", SUBSYSTEM=="block", ENV{DEVLINKS}=="/dev/myflash", RUN+="/usr/bin/flash_log.sh add"
        ACTION=="remove", SUBSYSTEM=="block", ENV{FSTAB_NAME}=="/dev/myflash", RUN+="/usr/bin/flash_log.sh remove"

The key-value pair ``KERNEL=="sd[a-d][0-9]`` is regular expression which
will match entries related to sd\*

The key-value pair ``SYMLINK+="myflash"`` will create a SYMLINK to
device node. note that the operator "+=" will create an additional
SYMLINK the same device if it already exist.

The key-value pair ``SUBSYSTEM=="block"`` in second and third line will
match the subsystem name with a block device.

The key-value pair ``ENV{DEVLINKS}=="/dev/myflash"`` will match only if
the device line ``/dev/myflash`` is present.

The entry ``RUN+="/usr/bin/flashlog.sh add"`` will run a shell script if
the kernel event matches. The shell script will log an entry to
``/var/log/flashdrive.log`` every time the flash drive is plugged in or
out

Once the udev rules and script are in place, we need to reload udev
rules to to the the new rules can take effect. This can be done by using
a command

    ::

        # udevadm control --reload-rules

*file: flashlog.sh*

    ::

        #------------------- FLASHLOG.SH -------------------------------
        #!/bin/bash
        #script: flash_log.sh

        usb_add() {
        echo -e "myflash attached on $(date)" >> /var/log/flashdrive.log
        }

        usb_remove() {
        echo -e "myflash removed on $(date)" >> /var/log/flashdrive.log
        }

        case "$1" in
        'add')
        usb_add
        ;;
        'remove')
        usb_remove
        ;;
        *)
        echo -e "usage $0 add|remove"
        esac
        exit 0

        #---------------------- END ----------------------------

If something is not working fine, we can always experiment with
key-value entries.

There is much more to explore with udev, I suggest you go through
udev,udevadm, amd udevd man-page for additional information and
commands.

**References:**

| 1) `http://www.reactivated.net/writing\ *\_udev\_*\ rules.html`_
|  2) https://www.linux.com/news/hardware/peripherals/180950-udev

.. _`http://www.reactivated.net/writing\ *\_udev\_*\ rules.html`: http://www.reactivated.net/writing_udev_rules.html
