Installing CyanogenMod 7.2 on Idea Blade/ZTE blade/xcd35
########################################################
:date: 2012-07-08 19:01
:author: tas_devil
:category: android
:tags: android, cyanogenmod, dell xcd35, Idea blade, zte blade
:slug: installing-cyanogenmod-7-2-on-idea-bladezte-bladexcd35

This post is an update to
`how-to-install-cyanogeod-7-1-on-zte-blade-a-k-a-dell-xcd35`_, but
mainly focuses on **Idea Blade** in which we have attempted to install
CyanogenMod 7.2.

| 1) Download CyanogenMod Stable version from this `link`_.
|  2) and Google Apps from `here`_
|  3) Copy both the zip files in sdcard
|  4) The procedure remains same till installing ROM Manager
|  5) you can't directly install **cm-7.2.0-blade.zip** using ROM
manager because it will throw an error something like,
| 
`` E:failed to find "cache" partition to mount at "/cache" E:Can't mount /cache/recovery/log E:Can't open /cache/recovery/log E:failed to find "cache" partition to mount at "/cache" E:Can't mount /cache/recovery/last_log E:Can't open /cache/recovery/last_log E:Can't find misc E:failed to find "cache" partition to mount at "/cache"``

you can't even backup, restore or flash ROM etc. because **CWM** fails
to identify root access to the device.

6) to overcome this problem, please download following files,

    a) `flash\_image`_

    b) `recovery.img`_

7) and connect to \`ADB\` using USB(enable \`Android debugging mode\` on
the device)

| 8) unzip \`flash\_image.zip\` and push it to a location \`/sdcard/\`
of the device
|  `` unzip flash_image.zip adb push flash_image /sdcard/``

| 9) unzip **recovery-4.0.1.0-blade-gen2-en.zip** and push it to a
location \`/sdcard/\`
| 
`` unzip recovery-4.0.1.0-blade-gen2-en.zip adb push recovery.img /sdcard/``

| 10) now enter the ``adb shell`` by typing,
|  `` adb shell``

| to enter as a ``root``, type
|  `` su``

| 11) you need to copy the binary \`flash\_image\` to \`/system/bin/\`
of the device, but \`/system\` needs to be mounted as ``rw`` first, type
|  `` busybox mount -o remount,rw /system``

| 12) and copy \`flash\_image\` binary to \`/system/bin\`
|  `` busybox cp /sdcard/flash_image /system/bin``

| 13) now give all permission to that binary
|  `` cd /system/bin busybox chmod 777 flash_image``

| 14) now flash the recovery image using,
|  `` flash_image recovery /sdcard/recovery.img``

Now reboot and select **Reboot into Recovery** option in ROM manager and
boot again in recovery mode. You can now follow the same procedure for
installing ROM from sdcard.

**Update:**

If you accidentally push wrong 'recovery.img' and the device fails to
boot.

1) Press 'vol-UP' + 'power-button' till you get android logo splash
screen.

2) Attach phone using USB cable.

| 3) and type
|  `` fastboot flash recovery recovery.img``
|  from your GNU/linux system.

'fastboot' binary can be located in android-sdk path
"android-sdk-linux/platform-tools/fastboot".

| **versions:**
|  ----
|  1) z4root\_blade\_root - v2
|  2) transparent proxy - 3.08 beta
|  3) ROM Manager - v5.0.0.8

| **Refs:**
|  ----
|  1) `CWM Recovery Solution-Idea Blade`_

.. _how-to-install-cyanogeod-7-1-on-zte-blade-a-k-a-dell-xcd35: http://gnu-linux.org/how-to-install-cyanogeod-7-1-on-zte-blade-a-k-a-dell-xcd35/
.. _link: http://download.cyanogenmod.com/get/jenkins/2816/cm-7.2.0-blade.zip
.. _here: http://cmw.22aaf3.com/gapps/gapps-gb-20110828-signed.zip
.. _flash\_image: http://forum.xda-developers.com/attachment.php?attachmentid=1133742&d=1339840194
.. _recovery.img: http://forum.xda-developers.com/attachment.php?attachmentid=1133743&d=1339840194
.. _CWM Recovery Solution-Idea Blade: http://forum.xda-developers.com/showthread.php?t=1713419&gt
