Bridging FreeBSD and GNU/Linux using VirtualBox
###############################################
:date: 2011-11-12 17:24
:author: tas_devil
:category: blogs
:tags: br0, brctl, bridge, em0, FreeBSD, GNU/linux, network, opensuse, vboxnet, virtual Box
:slug: bridging-freebsd-and-gnulinux-using-virtualbox

**Introduction and Description:**

This article is small attempt to explain how to connect GNU/Linux and
FreeBSD using Virtual Box.

So here we are going to bridge GNU/Linux(Open-SUSE) and FreeBSD.
Remember that here BSD(guest) is installed inside Virtual Box running on
Open-SUSE(host).

**Prerequisite:**

I assume that you have successfully installed FreeBSD on the virtual
box and you know a bit of networking. Lastly you must have enabled
bridging in the kernel if you have recompiled it most recently (Bridging
is enabled by-default in most generic kernels)

So my host OS is OpenSUSE-11.3 and guest OS is FreeBSD
8.0-RELEASE(GENERIC). My Virtual Box version is: 3.2.6\_OSE r63112.

**Configuring Open-SUSE:**

Login as root and type::

	ifconfig -a

the output will be similar to this one::

        eth0            Link encap:Ethernet HWaddr 00:1B:FC:1E:AD:9C
                        UP BROADCAST MULTICAST MTU:1500 Metric:1
                        RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                        TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                        collisions:0 txqueuelen:1000
                        RX bytes:0 (0.0 b) TX bytes:0 (0.0 b)
                        Interrupt:25 Base address:0xc000

        lo              Link encap:Local Loopback
                        inet addr:127.0.0.1 Mask:255.0.0.0
                        UP LOOPBACK RUNNING MTU:16436 Metric:1
                        RX packets:53 errors:0 dropped:0 overruns:0 frame:0
                        TX packets:53 errors:0 dropped:0 overruns:0 carrier:0
                        collisions:0 txqueuelen:0
                        RX bytes:4552 (4.4 Kb) TX bytes:4552 (4.4 Kb)

If you have selected network adapter '**type: Bridge**\ ' in Virtual Box
then an additional entry will be:

    ::

        vboxnet0        Link encap:Ethernet HWaddr 0A:00:27:00:00:00
                        UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
                        RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                        TX packets:3228 errors:0 dropped:0 overruns:0 carrier:0
                        collisions:0 txqueuelen:1000
                        RX bytes:0 (0.0 b) TX bytes:212309 (207.3 Kb)


**Configuring FreeBSD:**

If you have entered the valid IP address for your guest OS which
FreeBSD's sysinstall obviously ask for, go to your BSD box(root) and
type::

``# ifconfig -a ``

the output will be similar to this one::


        em0:    flags=8843 metric 0 mtu 1500
            options=9b
            ether 08:00:27:f5:13:2f
            inet 192.168.1.14 netmask 0xffffff00 broadcast 192.168.1.255
            media: Ethernet autoselect (1000baseT )
            status: active

        lo0:    flags=8049 metric 0 mtu 16384
            options=3
            inet6 fe80::1%lo0 prefixlen 64 scopeid 0x2 
            inet6 ::1 prefixlen 128 
            inet 127.0.0.1 netmask 0xff000000

Yes in FreeBSD your first ethernet card is called *em0* and *lo0* is
your loop back device.

**Main configuration:**

If you have successfully reached here, I assure you the rest is cake
walk :)

In simple words a Bridge is a device which links two physical networks
together. In this case 'eth0' is actually a physical device(your
ethernet card on OpenSUSE), but 'em0' is virtual(on FreeBSD). Don't
worry, Virtual Box makes it look like real by adding an entry
``vboxnet0`` in ``ifconfig``. So when you type ``ifconfig -a`` (on
Open-SUSE), you see an additional entry of ``vboxnet0``.

Physical network do have their own IP addresses, so go to BSD box and
check if you have given ``em0`` its valid IP address. In my case ``em0``
have IP of 192.168.1.14(you can make out from the output above). If
``em0`` have valid IP, logout of the BSD(we are not going to touch it
until we setup the bridge)

Login as *root* to Open-SUSE. Now we have to create a bridge, and then
add the two interfaces(eth0 and vboxnet0) to it. Remember ``em0`` is the
name given by BSD to its NIC, in Linux term, it is called ``eth0``.
``em0`` get converted to ``vboxnet0`` in Linux because virtual Box
created it(which is running on Open-SUSE). we can't bridge ``eth0`` and
``em0`` in this case as ``em0`` is virtual NIC(in BSD term). Linux see's
``em0`` as ``vboxnet0``

so

  ``em0`` = ``vboxnet0``

if we create second NIC in Virtual Box, then BSD will see it as ``em1``
whereas Linux will see it as ``vboxnet1`` and so on 

.. raw:: html

	em1 = vboxnet1
	em2 = vboxnet2

    em(n) = vboxnet(n)

More practical scenario can be a real system with two NIC's(say ``eth0``
and ``eth1``). Both NIC's are connected to two separate networks. And we
have to *bridge* both the NIC's, eventually we will bridge the networks.

**Creating Bridge:**

type::

	brctl addbr br0

here ``br0`` is the name of our bridge. If you check by typing
``ipconfig -a``. You will have an additional entry like  ::

        br0       Link encap:Ethernet  HWaddr 00:1B:FC:1E:AD:9C  
                  inet addr:192.168.1.11  Bcast:192.168.1.255  Mask:255.255.255.0
                  UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                  RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                  TX packets:3239 errors:0 dropped:0 overruns:0 carrier:0
                  collisions:0 txqueuelen:0 
                  RX bytes:0 (0.0 b)  TX bytes:216180 (211.1 Kb)

Please ignore the IP address entry. We haven't assigned IP to our ``br0``

Now to add ``eth0`` to ``br0`` type::

	brctl addif br0 ethO

and then add ``vboxnet0`` to ``br0`` by typing::

	brctl addif br0 vboxnet0

And now... because we have connected the two ethernet cards together,
they now form one large subnet. We are actually on one subnet, namely
``br0``. We can forget about the fact that br0 is actually
[``eth0 + vboxnet0``\ ] in disguise; we will only deal with ``br0`` from
now on. Because we are only on one subnet, so we only need one IP
address for the bridge. This address will be assigned to ``br0``.
``eth0`` and ``eth1`` should not have IP addresses allocated to them ::

	 ifconfig eth0 0.0.0.0 # ifconfig vboxnet 0 0.0.0.0

and finally assign an IP to ``br0``::

	ifconfig br0 192.168.1.11

You can check your bridge status by typing::

	brctl show br0

and you are done !

check by pinging from each OS to other

on BSD type::

	ping 192.168.1.11

because the bridge is on Open-SUSE

on Linux type::

	ping 192.168.1.14

if pinging works, congrats, you have successfully bridge the gap between
GNU/linux and FreeBSD.

and now its up to you, if you want to grow your network by adding more
systems or bridges. Try out ssh, ftp, telnet, http etc. on your network.
Even physical systems are now capable to connect to your (virtual)BSD
with the IP address 192.168.1.14

*Good luck!*

**Ref:**

  1) bridge-utils-1.2 HOWTO, By: Lennert Buytenhek
  2) Linux Bridge+Firewall Mini-HOWTO version 1.2.0 By: Peter Breuer (ptb@it.uc3m.es)
  3) Filtering Bridges, By: Alex Dupre(ale@FreeBSD.org)
