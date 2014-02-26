Extract the packets from pcap file to csv
#########################################
:date: 2013-12-16 16:56
:author: camitr
:category: blogs
:tags: network monitoring, tcpdump, tshark, tshark filter
:slug: extract-the-packets-from-pcap-file-to-csv

The previous post gives details for various commands of tshark to
capture the traffic. In this post I will use Tshark command to extract
the .pcap file to csv and which can be use to either post the data to
your database server for some graph based analysis or to be spreed
sheet ::

	 tshark -r traffic.pcap -T fields -e ip.src -E separator=, -E occurrence=f traffic.csv

-r: to read the .pcap file.
-T fields: different fields which are needed to capture.
-E separator: if there are multiple fields extracting separator is used to differentiate.

-E occurrence: Which occurrence is used for the field which has multiple occurrence, 'f' is for first
 and it store the fields inside the .csv file.

Multiple fields ::

	tshark -r traffic.pcap -T fields -e ip.src -e frame.len -e ip.proto -E separatorr=, -E occurrence=f > traffic.csv

It extracts multiple fields from .pcap file.
