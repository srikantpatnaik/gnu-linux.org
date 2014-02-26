RED5 installation on ubuntu 12.04
#################################
:date: 2013-05-28 15:55
:author: camitr
:category: blogs
:tags: red5, red5 installation, streaming video, ubuntu red5
:slug: red5-installation-on-ubuntu-12-04

Red5 is open source streaming server under Apache licencing. Most of
the video conferencing tools like BigBlueButton Open Meeting uses RED5
for the video streaming server.
In this post I will explain the latest version red5-1.0 installation
on ubuntu 12.04. We can also install red5 using the source by compiling
it using ant.

Step 1. Update the repo ::

	 sudo apt-get update

Step 2. Install the package. It contain all the basic libs and java
required for the red5::


	 sudo apt-get install red5-server

It will take some time depends on your internet speed.

Step 3. After Installation is complete open browser and type url http://localhost:5080  ::

	|red5|>

You will find red5 page. Now you need to install the packages to run the
demos and to use the red5 server as streaming server.

Step 4. Download the demos ::

	$ wget http://www.red5.org/downloads/red5/1\_0/red5-1.0.0-RC1.zip

Step 5. unzip the file and change the directory::
	
	unzip red5-1.0.0-RC1.zip -d red5
	cd red5

Step 6. Copy the demos and installer to working directory of red5::
	
	 sudo cp -R webapps/root/demos /var/lib/red5/webapps/root/demos
	 sudo cp -R webapps/installer /var/lib/red5/webapps/installer

Step 7. Change the ownership to red5::

	 sudo find /var/lib/red5/webapps/ -type d -exec chown \_red5 {} \\;

Step 8. Now click on install link which you find on the page open by
above link.

Step 9. Install all the packages listed. It will take some time depends
on the internet speed.

Step 10. Go back to home page and click on demos to check the demos.
click on view video link you will find a new page and then click on
**connect** find it on the right of the page and to left you will see
list of default videos.

|red5|

If the default video starts your installation is successful. If you find
the connection error like

 163) Connections: true \| true
 (80550) connected?: true
 (80684) NetConnection.onStatus:
 description = No scope "oflaDemo" on this server.
 code = NetConnection.Connect.Rejected
 level = error


$ wget
http://red5.googlecode.com/svn-history/r3990/snapshots/oflaDemo-r3989-java6.war

unzip the war file::
	
	 unzip oflaDemo-r3989-java6.war

restart the server::

	sudo service red5-server restart

Refresh the page and you will find the running video. 

Enjoy!!!!

.. |red5| image:: http://gnu-linux.org/wp-content/uploads/2013/05/red5-300x216.png
   :target: http://gnu-linux.org/wp-content/uploads/2013/05/red5.png

