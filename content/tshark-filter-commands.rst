Tshark filter commands
######################
:date: 2013-12-16 15:10
:author: camitr
:category: blogs
:tags: bandwidth monitor, network anysis, network monitoring, tcpdump, tshark, wireshark
:slug: tshark-filter-commands

Tshark is the command-line version of wireshark. It provide many useful
commands and capture filters that can be used on terminal which provides
an efficient way to analyse the incoming traffic and capture the traffic
in pcap . Let me give you a brief about the terminology we use in
Tshark.

**pcap**: Packet Capture (Pcap) is a protocol for capturing of data It
has api written in c. The capturing file is save with file extension
.pcap

**capture filter**: Filters are use to capture some specific type of
information from the traffic.

| Type of capture filters:
|  a. IP based: It can be for specific IP, Network IP, SRC IP or DST IP
|  b. PORT based: To capture the traffic for particular port

all the filters work with different ranges and exceptions.

**Examples**

1. Time duration capture:

::

     # tshark  -i eth0 -a duration:10 -w traffic.pcap

| -i to choose the interface on your machine.
|  -a for duration which is in seconds.
|  -w to write the capture packets in the file.

2. Filter with specific IP:

::

    # tshark -i eth0  host 192.168.1.100

3. Filter with Network IP:

::

    # tshark -i eth0 net 192.168.1.0/24

4. Filter with specific Source:

::

    # tshark -i eth0 src net 192.168.1.0/24

| capture only source packets coming from specific IP.
|  use dst filter for capturing only destination packets. We can also
use the combination of both filters.

5. Filter with port

::

    # tshark -i eth0 host 192.168.1.1 and port 80

capture port 80 traffic for the specific IP.
