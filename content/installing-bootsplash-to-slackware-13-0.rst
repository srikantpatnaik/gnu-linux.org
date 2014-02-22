Installing BootSplash on Slackware-13.0
#######################################
:date: 2011-12-26 20:18
:author: tas_devil
:category: blogs
:tags: bootsplash, GRUB, kernel, linux, patch, slackware
:slug: installing-bootsplash-to-slackware-13-0

**Introduction
**

In this tutorial, we will upgrade linux kernel 2.6.36 to 2.6.36.2.
And at the same time we will patch it with the bootsplash patch. We
are not going  in to details of kernel compilation here, you can
find excellent tutorial available out there.

Download bootsplash patch from http://x-softsi.com.br. In Slackware-13.0
GNU/Lnux, bootSplash theme path is /etc/bootsplash/.

The bootsplash Utility version is **bootsplash-3.1.tar.bz2**

**
 --------------------------------------------------
 Patching the Bootsplash
 --------------------------------------------------
**

    | tas\_devil@zyro:~$ tar -xjf linux-2.6.36.tar.bz2
    |  tas\_devil@zyro:~$ cd linux-2.6.36
    |  tas\_devil@zyro:~$ patch -p1 < bootsplash-3.1.11-2.6.36.patch
    |  patching file drivers/char/keyboard.c
    |  patching file drivers/char/n\_tty.c
    |  patching file drivers/char/vt.c
    |  patching file drivers/video/bootsplash/bootsplash.c
    |  patching file drivers/video/bootsplash/bootsplash.h
    |  patching file drivers/video/bootsplash/decode-jpg.c
    |  patching file drivers/video/bootsplash/decode-jpg.h
    |  patching file drivers/video/bootsplash/Kconfig
    |  patching file drivers/video/bootsplash/Makefile
    |  patching file drivers/video/bootsplash/render.c
    |  patching file drivers/video/console/bitblit.c
    |  patching file drivers/video/console/fbcon.c
    |  patching file drivers/video/console/fbcon.h
    |  patching file drivers/video/Kconfig
    |  patching file drivers/video/Makefile
    |  patching file drivers/video/vesafb.c
    |  patching file include/linux/console\_struct.h
    |  patching file include/linux/fb.h

**
 --------------------------------------------------
 Patching the kernel source(optional)
 --------------------------------------------------
**

    | tas\_devil@zyro:~$ patch -p1 < patch-2.6.36.2
    |  patching file Makefile
    |  patching file arch/arm/include/asm/assembler.h
    |  patching file arch/arm/include/asm/kgdb.h
    |  .
    |  .
    |  [output truncated]
    |  .
    |  .
    |  patching file sound/pci/hda/patch\_sigmatel.c
    |  patching file sound/pci/intel8x0.c
    |  patching file sound/soc/codecs/wm8900.c
    |  patching file sound/soc/codecs/wm8961.c

run the kernel menu configuration.

    | tas\_devil@zyro:~$ make menuconfig
    |  Graphics support --->
    |  Logo configuration --->
    |  [ ] Bootup logo
    |  Bootsplash configuration --->
    |  [\*] Bootup splash screen

    | Device Drivers --->
    |  Block devices --->
    |  <\*> RAM disk support
    |  Graphics support --->
    |  <\*>Support for frame buffer devices

save the configuration in file '.config'

run make

    | tas\_devil@zyro:~$ make
    |  root@zyro:~# make modules\_install
    |  root@zyro:~# make install

now create an initial ram disk image

    root@zyro:~# mkinitrd -k 2.6.36.2-smp -m ext4 -f ext4

this will create /boot/initrd.gz

**
 --------------------------------------------------
 Compiling Bootsplash utility
 --------------------------------------------------
**

    | tas\_devil@zyro:~$ tar -xjf bootsplash-3.1.tar.bz2
    |  tas\_devil@zyro:~$ cd bootsplash-3.1/Utilities
    |  tas\_devil@zyro:~$ make splash
    |  gcc -Os -Wall -I/usr/include/freetype2 -L/usr/lib splash.c -o
    splash
    |  gcc -Os -Wall -I/usr/include/freetype2 -L/usr/lib splashpbm.c -o
    splashpbm
    |  gcc -Os -Wall -I/usr/include/freetype2 -L/usr/lib
    fbresolution.c-o fbresolution
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o fbtruetype.o
    fbtruetype.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o
    fbtruetype-messages.o fbtruetype-messages.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o console.o console.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o ttf.o ttf.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o luxisri.o luxisri.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -L/usr/lib -o fbtruetype
    -L/usr/lib fbtruetype.o fbtruetype-messages.o console.o ttf.o
    luxisri.o -lfreetype -lm
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o fbmngplay.o
    fbmngplay.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o fbmngplay-messages.o
    fbmngplay-messages.c
    |  gcc -Os -Wall -I/usr/include/freetype2 -c -o mng.o mng.c
    |  .
    |  .
    |  [with some warnings of course]
    |  .
    |  .

switch to root user and copy splash binary to /usr/bin/

    root@zyro:~# cp -v splash /usr/bin/

now concatenate splash image with kernel initial ramdisk

    root@zyro:~# splash -s -f
    /etc/bootsplash/themes/slackware/config/bootsplash-1024x768.cfg >>
    /boot/initrd.gz

copy initrd.gz from /boot to /boot/initrd-tree/bootsplash

    root@zyro:/boot# cp initrd.gz /boot/initrd-tree/bootsplash

now make an initial ramdisk to support ext4 file system(optional)

    root@zyro:# mkinitrd -k 2.6.36.2-smp -m ext4 -f ext4

| **
 ------------------------------------------------------------
 Insert these lines in GRUB configuration file
 ------------------------------------------------------------
**
|  GRUB(legacy) entry

    | .
    |  .
    |  .
    |  title Slackware13.0-2.6.36.2-smp
    |  root (hd0,4)
    |  kernel /boot/vmlinuz root=/dev/hdb5 ro splash=silent vga=791
    |  initrd /boot/initrd.gz
    |  .
    |  .
    |  .

**
 REBOOT ...
**

| After rebooting, if you see the bootsplash, you can move forward to
|  insert progress bar in to the splash screen.

**
 ------------------------------------------------------------
 Modifying rc.0,rc.S, rc.M, rc.6(link to rc.0)
 ------------------------------------------------------------
**

| You need to append below lines at appropriate places so that the
|  status of progress bar matches with system boot process.

Insert below lines in /etc/rc.d/rc.0

    | #### Set the splash screen to verbose mode ####
    |  [[ -x /usr/bin/splash && -e /proc/splash ]] && echo "verbose" >
    |  /proc/splash &

Insert below lines in /etc/rc.d/rc.S

    | # Check for splash availability
    |  SPLASHSCREEN="no"
    |  [[ -x /usr/bin/splash && -e /proc/splash ]] && export
    SPLASHSCREEN="yes"

    | progressbar() {
    |  echo "show $(( 65534 \* $1 / 100 ))" > /proc/splash
    |  }

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && (progressbar 5 ; sleep 0.2;
    |  progressbar 10 ; sleep 0.2;
    |  progressbar 15 ; sleep 0.2;
    |  progressbar 20 ; sleep 0.2;
    |  progressbar 25 ; sleep 0.2;
    |  progressbar 30 ; sleep 0.2;
    |  progressbar 35 ) &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 40 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 45 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 50 &

    | ### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 55 &

Insert below lines in /etc/rc.d/rc.M

    | # Check for splash availability
    |  SPLASHSCREEN="no"
    |  [[ -x /usr/bin/splash && -e /proc/splash ]] && export
    SPLASHSCREEN="yes"
    |  progressbar() {
    |  echo "show $(( 65534 \* $1 / 100 ))" > /proc/splash
    |  }

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 60 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 65 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 70 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 75 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 80 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 85 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 90 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 95 &

    | #### Progress bar ####
    |  [ "$SPLASHSCREEN" = "yes" ] && progressbar 100 &

    #### Push the progress bar and Set the splash screen to verbose mode
    10 seconds later ####

    | if [ "$SPLASHSCREEN" = "yes" ]; then
    |  echo "show 65534" > /proc/splash &
    |  (sleep 10 ; echo "verbose") > /proc/splash &
    |  fi

**
 ----------------------------------------------------------
 Download links:
 ----------------------------------------------------------
**

| 1) Kernel source
|  http://www.kernel.org/
|  (Only if you want to upgrade your kernel version)

| 2) Bootsplash patch
|  http://x-softsi.com.br
|  (remember to download a patch according to your Kernel version you
are
|  upgrading to)

| 3) A bootsplash theme
|  http://kde-look.org/

| 4) BootSplash Utility
|  http://www.bootsplash.org/

**
**
