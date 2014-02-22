Installing GRUB 0.97 (Legacy)
#############################
:date: 2011-10-26 09:31
:author: tas_devil
:category: blogs
:tags: compiling grub legacy from source, grub legacy, MBR backup, patching grub
:slug: installing-grub-0-97-legacy

| Most GNU/Linux Distributions now ships with GRUB-2 which is a huge
improvement over GRUB Legacy. This post is for those who still want to
install GRUB 0.97.
|  Assumption:
|  Some familiarity with GNU/Linux is required. If the readers are
newbie's, I would expect at least *common sense* from them.
| 

| Request:
|  Please read this file completely before you attempt real
installation.

| Warning:
|  Playing with MBR(Master Boot Record) can be fatal, but real fun lies
there. Before starting the procedure, backup your MBR.

 

| ----------
|  **Backing up MBR**
|  ----------
|  *SYNTAX:*

    dd if=/dev/root\_partition\_of\_hdd of=/path/to/mbr bs=512 count=1

*EXAMPLES:*

-  dd if=/dev/hda of=/home/user/mbr.img bs=512 count=1

-  dd if=/dev/sda of=/home/greg/bckp/mbr\_of\_sda.img bs=512 count=1

| ----------
|  **Restoring MBR**
|  ----------
|  *SYNTAX:*

    dd if=/path/to/mbr of=/dev/root\_partition\_of\_hdd

*EXAMPLES:*

-  dd if=/home/user/mbr.img of=/dev/hda

-  dd if=/home/greg/bckp/mbr\_of\_sda.img of=/dev/sda

| \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
|  **INSTALLATION PROCEDURE STARTS HERE**
| 
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
|  Note:
|  I got GRUB-0.97(source) and other patches from Slackware 13.0 DVD.
This version of GRUB does not contains below updates, and should be
patched manually. If your root partition is formatted with Ext4
file-system, GRUB-0.97 does not contain support for Ext4 fs. Also note
that patches should be applied in following order to avoid error.

| ----------
|  **EXTRACTING**
|  ----------

    | tar -xzf grub-0.97.tar.gz
    |  gunzip grub-0.97-x86\_64.patch.gz
    |  gunzip gcc4.diff.gz
    |  gunzip ext2-support-256byte-inodes.diff.gz
    |  gunzip ext4-support.diff.gz

| ----------
|  **patching**
|  ----------
|  *
 Note: '--dry-run' does not really apply patch, this is to avoid
 spoiling the source files before applying real patch.
*
|  ..........

    cd grub-0.97

    | patch --dry-run -p1 < ../grub-0.97-x86\_64.patch
    |  patch -p1 < ../grub-0.97-x86\_64.patch

    | patch --dry-run -p1 < ../gcc4.diff
    |  patch -p1 < ../gcc4.diff

    | patch --dry-run -p1 < ../ext2-support-256byte-inodes.diff
    |  patch -p1 < ../ext2-support-256byte-inodes.diff

    | patch --dry-run -p1 < ../ext4-support.diff
    |  patch -p1 < ../ext4-support.diff

| ----------
|  **Configure & Install**
|  ----------

    | ./configure
    |  make
    |  make check
    |  make install
    |  grub-install /dev/hdb

Now you can edit /boot/grub/menu.lst and reboot the system

------------------ INSTALLATION PROCEDURE ENDS HERE ------------------

| \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
|  **Reclaiming GRUB (IN CASE OF EMERGENCY)**
| 
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

| Boot from LIVE-CD/DVD
|  -----

    $ sudo grub

    > find /boot/grub/stage1

    | (hd0,0)
    |  (hd0,4)

    > root (hd0,0)

    > setup (hd0) *---> to install GRUB to MBR.*

    > setup (hd0,4) *---> to install GRUB to /dev/hda5*

    > quit

--------------- EOF ---------------
