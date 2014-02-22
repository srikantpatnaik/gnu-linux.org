Configuring Huawei-EC152 modem [TataPhoton+]
############################################
:date: 2011-10-26 08:07
:author: tas_devil
:category: blogs
:tags: linux, slackware, tata photon on linux, usb modswitch, wvdial
:slug: configuring-huawei-ec152-modem-tataphoton

| Finally I managed to configure **Huawei EC-152 [TataPhoton+]** modem
on slackware-13(linux-2.6.36.2). It requires **usb\_modeswitch** package
which does the smart work of switching the device mode. These device
when plugged in, will mount as a CD-ROM, and when ejected it will switch
to the modem mode. This technique avoid any extra drivers CD to be
shipped with a device as a result all the respective drivers(for Windows
& Mac) are inside the device itself. For Windows it comes with own
dialer and an *autorun* file for ease of installation.
| 
|  Latest Linux distributions like Fedora, Ubuntu and Mandriva etc.
includes **usb\_modeswitch** package by default. User can directly
plug-in the device, the usb\_modeswitch package will take care of
switching the device mode and you can dial-up the internet using
distribution's network manager.

I am using Slackware-13 with linux kernel-2.6.36.2 (Slackware-13.37 is
released). Usb\_modeswitch, wvdial(and wvstream) are not included in
Slackware by default, so you have to download its source or binaries,
depend on the distribution you are using.

For those who are using Slackware distro's, Wvdial depends on wvstream,
both are available at `slackbuilds.org`_. Others will have to search for
binaries from their distribution's website. I think the package manager
will do the same and install all the three packages with the respective
dependencies.

More information on usb\_modeswitch can be found on
`www.draisberghof.de`_ This website provide excellent introduction to
usb modeswitch, detailed explanation on how to install, use, hardware
support and troubleshooting. Users can download the package in tar-ball
or binary format.

In this short tutorial, I will describe, how I managed to configure and
use Huawei EC-152, Tataphoton+ modem. The procedure described is far
more generic apart for installing wvdial and wvstream packages using
*slackbuild script*.

**------------------- TUTORIAL STARTS HERE -----------------**

| Below is the output from ``/var/log/messages`` before installing
usb-modeswitch package, as you can see there is no trace of the device
identified as 'modem'. The device is identified as **HUAWEI Mobile**
|  with respective ``idVendor`` and ``idProduct``. As mentioned earlier
it is detected as scsi CD-ROM by usb-storage module.

``/var/log/messages``

    | kernel: usb 6-1: new full speed USB device using ohci\_hcd and
    address 2
    |  kernel: usb 6-1: New USB device found, idVendor=12d1,
    idProduct=1446
    |  kernel: usb 6-1: New USB device strings: Mfr=1, Product=2,
    SerialNumber=4
    |  kernel: usb 6-1: Product: HUAWEI Mobile
    |  kernel: usb 6-1: Manufacturer: HUAÃ¿WEI TECHNOLOGIES
    |  kernel: usb 6-1: SerialNumber:
    Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿
    |  kernel: scsi4 : usb-storage 6-1:1.0
    |  kernel: scsi 4:0:0:0: CD-ROM HUAWEI Mass Storage 2.31 PQ: 0 ANSI:
    0
    |  kernel: sr 4:0:0:0: Attached scsi generic sg1 type 5

you can see similar output if your device is not switching

-  usb-modeswitch-1.1.7(dated:2011-02-27)
-  usb-modeswitch-data(dated:2011-02-27)
-  device\_reference.txt(gzipped) from 2011-02-27 (for ref)

 

-  tcl(for the wrapper script to work)
-  libusb-0.1.12 (already installed in slackware-13)

 

*for usb-modeswitch:*

    | root# tar -xvjf usb-modeswitch-1.1.7.tar.bz2
    |  root# cd usb-modeswitch-1.1.7
    |  root# sudo make install

this will install the udev script, wrapper script, config files,
man-pages and compile all the binaries.

*for usb-modeswitch-data*

    | root# tar -xvjf modeswitch-data-20110227.tar.bz2
    |  root# cd modeswitch-data-20110227
    |  root# sudo make install

this will copy ``usb-modeswitch.d/*`` in ``/etc/``\ (not in case of
*Slackware*), you have to do it manually. This will also copy udev rules
in ``/lib/udev/rules.d/`` and **usb-modeswitch** file(bash script) in
``/lib/udev/``

If all goes well, you can see similar entry in your
``/var/log/messages`` after plugging the device.

    | kernel: usb 6-2: new full speed USB device using ohci\_hcd and
    address 7
    |  kernel: usb 6-2: New USB device found, idVendor=12d1,
    idProduct=1446 <------
    |  kernel: usb 6-2: New USB device strings: Mfr=1, Product=2,
    SerialNumber=4
    |  kernel: usb 6-2: Product: HUAWEI Mobile
    |  kernel: usb 6-2: Manufacturer: HUAÃ¿WEI TECHNOLOGIES
    |  kernel: usb 6-2: SerialNumber:
    Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿
    |  kernel: scsi15 : usb-storage 6-2:1.0
    |  usb\_modeswitch: switching 12d1:1446 (HUAÿWEI TECHNOLOGIES:
    HUAWEI Mobile)
    |  kernel: usb 6-2: USB disconnect, address 7
    |  kernel: usb 6-2: new full speed USB device using ohci\_hcd and
    address 8
    |  kernel: usb 6-2: New USB device found, idVendor=12d1,
    idProduct=140b
    |  kernel: usb 6-2: New USB device strings: Mfr=1, Product=2,
    SerialNumber=4
    |  kernel: usb 6-2: Product: HUAWEI Mobile
    |  kernel: usb 6-2: Manufacturer: HUAÃ¿WEI TECHNOLOGIES
    |  kernel: usb 6-2: SerialNumber:
    Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿
    |  kernel: option 6-2:1.0: GSM modem (1-port) converter detected
    |  kernel: usb 6-2: GSM modem (1-port) converter now attached to
    ttyUSB0
    |  kernel: option 6-2:1.1: GSM modem (1-port) converter detected
    |  kernel: usb 6-2: GSM modem (1-port) converter now attached to
    ttyUSB1
    |  kernel: option 6-2:1.2: GSM modem (1-port) converter detected
    |  kernel: usb 6-2: GSM modem (1-port) converter now attached to
    ttyUSB2
    |  kernel: scsi19 : usb-storage 6-2:1.3
    |  usb\_modeswitch: switched to 12d1:140b (HUAÿWEI TECHNOLOGIES:
    HUAWEI Mobile) <------
    |  kernel: scsi 19:0:0:0: CD-ROM HUAWEI Mass Storage 2.31 PQ: 0
    ANSI: 0
    |  kernel: sr 19:0:0:0: Attached scsi generic sg1 type 5
    |  kernel: scsi 19:0:0:1: Direct-Access HUAWEI SD Storage 2.31 PQ: 0
    ANSI: 2
    |  kernel: sd 19:0:0:1: Attached scsi generic sg2 type 0
    |  kernel: sd 19:0:0:1: [sdb] Attached SCSI removable disk

The device has switched its Product ID from *0x1446* to *0x140b*. If
your device is not switching it's mode, don't worry you have to manually
probe the device.

| type(syntax):
| 
`` usb_modeswitch -v ur_idVendor -p ur_idProduct -V ur_targetVendor -P ur_targetVendor -s -M MsgContent``

You can download *device\_reference.txt* file from
`www.draisberghof.de <http://www.draisberghof.de/usb_modeswitch>`__.
Search for matching *idVendor* and *idProduct*. This file is pretty
descriptive and contains explanation to other flags. You must try all
possible configuration that is matching your *idVendor* and *idProduct*.

Example:

    root# **usb\_modeswitch -v 0x12d1 -p 0x1446 -V 0x12d1 -P 0x140b -s
    20 -M
    55534243123456780000000000000011062000000100000000000000000000**

    | output
    |  Looking for target devices ...
    |  No devices in target mode or class found
    |  Looking for default devices ...
    |  Found devices in default mode or class (1)
    |  Accessing device 004 on bus 002 ...
    |  Using endpoints 0x08 (out) and 0x87 (in)
    |  Using endpoints 0x08 (out) and 0x87 (in)
    |  Inquiring device details; driver will be detached ...
    |  Looking for active driver ...
    |  OK, driver found ("usb-storage")
    |  OK, driver "usb-storage" detached

    | SCSI inquiry data (for identification)
    |  -------------------------
    |  Vendor String: HUAWEI
    |  Model String: Mass Storage
    |  Revision String: 2.31
    |  -------------------------

    | USB description data (for identification)
    |  -------------------------
    |  Manufacturer: HUAÿWEI TECHNOLOGIES
    |  Product: HUAWEI Mobile
    |  Serial No.: ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    |  -------------------------
    |  Setting up communication with interface 0 ...
    |  Using endpoint 0x08 for message sending ...
    |  Trying to send message 1 to endpoint 0x08 ...
    |  OK, message successfully sent
    |  Resetting response endpoint 0x87
    |  Error resetting endpoint: -71
    |  Resetting message endpoint 0x08
    |  Error resetting endpoint: -71

    | Checking for mode switch (max. 20 times, once per second) ...
    |  Waiting for original device to vanish ...
    |  Original device can't be accessed anymore. Good.
    |  Searching for target devices ...
    |  Searching for target devices ...
    |  Searching for target devices ...
    |  Searching for target devices ...
    |  Searching for target devices ...
    |  Found correct target device

    Mode switch succeeded. Bye.

If you still have problem, read the troubleshooting section of
usb\_modeswitch main page. If you think none of configuration is
matching your device, you can post your query to usb\_modeswitch
`forum`_. You can also report new configuration in the forum.

 

*Configure ``/etc/usb-modeswitch.conf`` accordingly:*

``/etc/usb-modeswitch.conf``

    | # Configuration for the usb\_modeswitch package, a mode switching
    tool for USB
    |  # devices providing multiple states or modes. This file is
    evaluated by the
    |  # wrapper script "usb\_modeswitch\_dispatcher" in /usr/sbin. To
    enable an
    |  # option, set it to "1", "yes" or "true" (case doesn't matter).
    Everything else
    |  # counts as "disable"

    | # Disable automatic mode switching globally (e.g. to access the
    original
    |  # install storage)

    DisableSwitching=0

    | # Enable logging (results in a extensive report file in /var/log,
    named
    |  # "usb\_modeswitch\_" (and probably others)

    EnableLogging=1

    | # This is the ID the USB device shows after having been plugged
    in. The
    |  # program needs this; if not found -> no action.

    DefaultVendor= 0x12d1 DefaultProduct= 0x1446

    | # These are the IDs of the USB device after successful mode
    switching. They
    |  # are optional, but I recommend to provide them for better
    analysis. You
    |  # definitely need them if you enable CheckSuccess (see below)

    TargetVendor= 0x12d1 TargetProduct= 0x140b

    | # Check continuously if the switch succeeded for max seconds.
    |  # First, an interface access test: most devices vanish after
    switching and
    |  # can't be accessed anymore. Second, a recount of target devices:
    one more
    |  # than at the initial count, at the same bus with a higher device
    number ->
    |  # device switched fine. It's safe to give a higher value than
    needed;
    |  # checking stops as soon as the target device is found

    CheckSuccess=20

    | # A hex string containing the "message" sequence; it will be sent
    as a USB
    |  # bulk transfer

    MessageContent="55534243123456780000000000000011062000000100000000000000000000"

    | # Some devices just need to be detached from the usb-storage
    driver to
    |  # initiate the mode switching. Using this feature instead of
    removing the
    |  # whole usbstorage module keeps other storage devices working.

    DetachStorageOnly=0

    # Some Huawei devices can be switched by a special control message.

    HuaweiMode=1

also edit file in ``/etc/usb_modeswitch.d/*`` which matches your
*idVendor:idProduct*

``/etc/usb_modeswitch.d/12d1:1446``

    | ########################################################
    |  # Huawei, EC 152

    | DefaultVendor=0x12d1
    |  DefaultProduct=0x1446

    | TargetVendor=0x12d1
    |  TargetProduct=0x140b

    CheckSuccess=20

    MessageContent="55534243123456780000000000000011062000000100000000000000000000"

    ########################################################

 

**Configuring and running wvdial**

download both packages for slackbuild.org and install them

    | root# sh ./wvdial.SlackBuild
    |  root# cd /tmp/SBo
    |  root# pkginstall \*.tgz

Running wvdial for the first time:

    | root# **wvdialconf /etc/wvdial.conf**
    |  Editing \`/etc/wvdial'.

    Scanning your serial ports for a modem.

    | ttyS0: ATQ0 V1 E1 -- failed with 2400 baud, next try: 9600 baud
    |  ttyS0: ATQ0 V1 E1 -- failed with 9600 baud, next try: 115200 baud
    |  ttyS0: ATQ0 V1 E1 -- and failed too at 115200, giving up.
    |  Modem Port Scan: S1 S2 S3
    |  WvModem: Cannot get information for serial port.
    |  ttyUSB0: ATQ0 V1 E1 -- OK
    |  ttyUSB0: ATQ0 V1 E1 Z -- OK
    |  ttyUSB0: ATQ0 V1 E1 S0=0 -- OK
    |  ttyUSB0: ATQ0 V1 E1 S0=0 &C1 -- OK
    |  ttyUSB0: ATQ0 V1 E1 S0=0 &C1 &D2 -- OK
    |  ttyUSB0: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 -- OK
    |  ttyUSB0: Modem Identifier: ATI -- Manufacturer: +GMI: HUAWEI
    TECHNOLOGIES CO., LTD
    |  ttyUSB0: Speed 9600: AT -- OK
    |  ttyUSB0: Max speed is 9600; that should be safe.
    |  ttyUSB0: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 -- OK
    |  WvModem: Cannot get information for serial port.
    |  ttyUSB1: ATQ0 V1 E1 -- failed with 2400 baud, next try: 9600 baud
    |  ttyUSB1: ATQ0 V1 E1 -- failed with 9600 baud, next try: 9600 baud
    |  ttyUSB1: ATQ0 V1 E1 -- and failed too at 115200, giving up.
    |  WvModem: Cannot get information for serial port.
    |  ttyUSB2: ATQ0 V1 E1 -- OK
    |  ttyUSB2: ATQ0 V1 E1 Z -- OK
    |  ttyUSB2: ATQ0 V1 E1 S0=0 -- OK
    |  ttyUSB2: ATQ0 V1 E1 S0=0 &C1 -- OK
    |  ttyUSB2: ATQ0 V1 E1 S0=0 &C1 &D2 -- OK
    |  ttyUSB2: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 -- OK
    |  ttyUSB2: Modem Identifier: ATI -- Manufacturer: +GMI: HUAWEI
    TECHNOLOGIES CO., LTD
    |  ttyUSB2: Speed 9600: AT -- OK
    |  ttyUSB2: Max speed is 9600; that should be safe.
    |  ttyUSB2: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 -- OK

    | Found a modem on /dev/ttyUSB0.
    |  /etc/wvdial: Can't open '/etc/wvdial' for reading: No such file
    or directory
    |  /etc/wvdial: ...starting with blank configuration.
    |  Modem configuration written to /etc/wvdial.
    |  ttyUSB0: Speed 9600; init "ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0"
    |  ttyUSB2: Speed 9600; init "ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0"

Now configure ``/etc/wvdial.conf``

``/etc/wvdial.conf``

    | [Dialer Defaults]
    |  Modem = /dev/ttyUSB0
    |  Modem Type = USB Modem
    |  Init1 = ATZ
    |  Init2 = ATQ0 V1 E1 S0=0&C1 &D2 +FCLASS=0
    |  Init3 = AT+CRM=1
    |  Stupid Mode = 1
    |  ISDN = 0
    |  Phone = #777
    |  Username = internet
    |  Password = internet
    |  Baud = 230400

and run wvdial (as root)

    | # **wvdial**
    |  --> WvDial: Internet dialer version 1.61
    |  --> Cannot get information for serial port.
    |  --> Initializing modem.
    |  --> Sending: ATZ
    |  ATZ
    |  OK
    |  --> Sending: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    |  ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    |  OK
    |  --> Sending: AT+CRM=1
    |  AT+CRM=1
    |  OK
    |  --> Modem initialized.
    |  --> Sending: ATDT#777
    |  --> Waiting for carrier.
    |  ATDT#777
    |  CONNECT
    |  --> Carrier detected. Starting PPP immediately.
    |  --> Starting pppd at Mon May 2 11:41:09 2011
    |  --> Pid of pppd: 3586
    |  --> Using interface ppp0
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> local IP address 14.99.xxx.yyy
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> remote IP address 172.29.xxx.yyy
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> primary DNS address 121.242.190.180
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]
    |  --> secondary DNS address 121.242.190.210
    |  --> pppd: È¦[06][08]0¦[06][08]è¬[06][08]

    CTRL+C

now copy DNS address to ``/etc/resolve.conf``

    root# **cp -v /etc/ppp/resolve.conf /etc/resolve.conf**

Now fire up ur favorite browser to check the connection...

*complete session log*

    | kernel: usb 6-1: new full speed USB device using ohci\_hcd and
    address 2
    |  kernel: usb 6-1: New USB device found, idVendor=12d1,
    idProduct=1446
    |  kernel: usb 6-1: New USB device strings: Mfr=1, Product=2,
    SerialNumber=4
    |  kernel: usb 6-1: Product: HAWK Mobile
    |  kernel: usb 6-1: Manufacturer: HUAÃ¿WEI TECHNOLOGIES
    |  kernel: usb 6-1: SerialNumber:
    Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿
    |  kernel: scsi4 : usb-storage 6-1:1.0
    |  kernel: scsi 4:0:0:0: CD-ROM HUAWEI Mass Storage 2.31 PQ: 0 ANSI:
    0
    |  kernel: Gr 4:0:0:0: Attached scsi generic sg1 type 5
    |  usb\_modeswitch: switching 12d1:1446 (HUAÿWEI TECHNOLOGIES:
    HUAWEI Mobile)
    |  kernel: usb 6-1: USB disconnect, address 2
    |  kernel: usb 6-1: new full speed USB device using ohci\_hcd and
    address 3
    |  kernel: usb 6-1: New USB device found, idVendor=12d1,
    idProduct=140b
    |  kernel: usb 6-1: New USB device strings: Mfr=1, Product=2,
    SerialNumber=4
    |  kernel: usb 6-1: Product: HUAWEI Mobile
    |  kernel: usb 6-1: Manufacturer: HUAÃ¿WEI TECHNOLOGIES
    |  kernel: usb 6-1: SerialNumber:
    Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿Ã¿
    |  kernel: scsi8 : usb-storage 6-1:1.3
    |  usb\_modeswitch: switched to 12d1:140b (HUAÿWEI TECHNOLOGIES:
    HUAWEI Mobile)
    |  kernel: usbcore: registered new interface driver usbserial
    |  kernel: USB Serial support registered for generic
    |  kernel: usbcore: registered new interface driver
    usbserial\_generic
    |  kernel: usbserial: USB Serial Driver core
    |  kernel: USB Serial support registered for GSM modem (1-port)
    |  kernel: option 6-1:1.0: GSM modem (1-port) converter detected
    |  kernel: usb 6-1: GSM modem (1-port) converter now attached to
    ttyUSB0
    |  kernel: option 6-1:1.1: GSM modem (1-port) converter detected
    |  kernel: usb 6-1: GSM modem (1-port) converter now attached to
    ttyUSB1
    |  kernel: option 6-1:1.2: GSM modem (1-port) converter detected
    |  kernel: usb 6-1: GSM modem (1-port) converter now attached to
    ttyUSB2
    |  kernel: usbcore: registered new interface driver option
    |  kernel: option: v0.7.2:USB Driver for GSM modems
    |  kernel: scsi 8:0:0:0: CD-ROM HUAWEI Mass Storage 2.31 PQ: 0 ANSI:
    0
    |  kernel: Fr 8:0:0:0: Attached scsi generic sg1 type 5
    |  kernel: scsi 8:0:0:1: Direct-Access HUAWEI SD Storage 2.31 PQ: 0
    ANSI: 2
    |  kernel: sd 8:0:0:1: Attached scsi generic sg2 type 0
    |  kernel: sd 8:0:0:1: [sdb] Attached SCSI removable disk
    |  kernel: PPP generic driver version 2.4.2
    |  pappy[3045]: pppd 2.4.4 started by root, uid 0
    |  pppd[3045]: Using interface ppp0
    |  pppd[3045]: Connect: ppp0 /dev/ttyUSB0
    |  pppd[3045]: CHAP authentication succeeded
    |  pppd[3045]: CHAP authentication succeeded
    |  kernel: PPP BSD Compression module registered
    |  kernel: PPP Deflate Compression module registered
    |  pppd[3045]: local HP address 14.97.xxx.yyy
    |  pppd[3045]: remote IP address 172.29.xxx.yyy
    |  pppd[3045]: primary DY'S address 121.242.190.180
    |  pppd[3045]: secondary DNS address 121.242.190.210
    |  kernel: r8169 0000:02:00.0: eth0: link down
    |  kernel: r8169 0000:02:00.0: eth0: link up
    |  kernel: r8169 0000:02:00.0: eth0: link down
    |  kernel: r8169 0000:02:00.0: eth0: link up
    |  kernel: r8169 0000:02:00.0: eth0: link down
    |  pppd[3045]: Terminating on signal 15
    |  pppd[3045]: Connect time 37.8 minutes.
    |  pppd[3045]: Sent 2052416 bytes, received 17654252 bytes.
    |  pppd[3045]: Connection terminated.
    |  pppd[3045]: Exit.

Below is the log from /var/log/messages when device is unplugged

    | kernel: usb 6-1: USB disconnect, address 3
    |  kernel: option1 ttyUSB0: GSM modem (1-port) converter now
    disconnected from ttyUSB0
    |  kernel: option 6-1:1.0: device disconnected
    |  kernel: option1 ttyUSB1: GSM modem (1-port) converter now
    disconnected from ttyUSB1
    |  kernel: option 6-1:1.1: device disconnected
    |  kernel: option1 ttyUSB2: GSM modem (1-port) converter now
    disconnected from ttyUSB2
    |  kernel: option 6-1:1.2: device disconnected

**---------------------- EOF -----------------------**

Happy Hacking !

.. _slackbuilds.org: http://slackbuilds.org/
.. _www.draisberghof.de: http://www.draisberghof.de/usb_modeswitch.
.. _forum: http://www.draisberghof.de/usb_modeswitch/bb/
