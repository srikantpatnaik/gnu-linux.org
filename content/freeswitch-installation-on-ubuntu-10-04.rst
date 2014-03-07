Freeswitch installation on ubuntu 10.04
#######################################
:date: 2013-07-09 15:07
:author: camitr
:category: blogs
:tags: freeswitch, freeswitch installation, softphone, ubuntu freeswitch
:slug: freeswitch-installation-on-ubuntu-10-04

Freeswitch is open source telephony platform for audio,video and
messaging system. In this post I will install freeswitch version 1.5.1b
on ubuntu 10.04.

**Install required libraries** ::

  # apt-get install git-core build-essential autoconf automake libtool libncurses5 libncurses5-dev make libjpeg-dev pkg-config unixodbc unixodbc-dev zlib1g-dev

  # apt-get install libcurl4-openssl-dev libexpat1-dev libssl-dev libtiff4-dev libx11-dev unixodbc-dev python2.6-dev zlib1g-dev libzrtpcpp-dev libasound2-dev libogg-dev libvorbis-dev libperl-dev  libgdbm-dev libdb-dev python-dev uuid-dev bison autoconf g++ libncurses-dev

Download the source of Freeswitch ::

  # cd /usr/share/src
  # git clone git://git.freeswitch.org/freeswitch.git

**Configuring and build the freeswitch from the source** ::

  # cd freeswitch
  # ./bootstrap.sh ### this script will take some time depends on you system speed.
  # ./configure
  # make
  # make all install cd-sounds-install cd-moh-install

Your freeswitch installation is complete. Now go to the freeswitch
directory to run the service.

**Run Freeswitch service** ::

 # cd /usr/local/freeswitch/bin
 # ./freeswitch

you will find the terminal like image below.

|Screenshot from 2013-07-09 14:42:51|

To run the freeswitch in background ::

# ./freeswitch -nc

Now can enjoy the free calling on your local network using softphone



Twinkle freeswitch softphone for linux. you can install it using the
synaptic package manager.

.. |Screenshot from 2013-07-09 14:42:51| image:: http://gnu-linux.org/uploads/2013/07/Screenshot-from-2013-07-09-144251-300x168.png
   :target: http://gnu-linux.org/uploads/2013/07/Screenshot-from-2013-07-09-144251.png
