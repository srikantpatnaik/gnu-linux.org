Using proxy authentication in android
#####################################
:date: 2013-01-29 11:25
:author: srikant
:category: android
:tags: android, ICS, proxy, proxy authentication, squid
:slug: using-proxy-authentication-in-android

I will suggest two solutions,  first one, download opensource app
ProxyDroid from `here`_ and try your luck. There are many such proxy
authentication apps on Google play too, to try those you should connect
to some direct internet source using 3G/2G dongle or wifi hot spot from
any compatible phone. Second solution is bit complex. In a GNU/Linux
machine(assuming its IP to be 192.168.1.2) install squid3 proxy
server(say on your laptop) Then open\ **/etc/squid3/squid.conf** file as
sudo and add these lines at the end of the file after updating
<proxy-host>, <proxy-port> and username:password field.

::

    http_port hostmachine-ip:3128
    http_port hostmachine-ip:3128
    cache_peer "proxy-host" parent "proxy-port" 0 no-query default login=username:password
    # No direct access
    never_direct allow all

Save and close the above file. Restart the squid3 sever by

::

    sudo service squid3 restart

Now connect your Wifi(your Wifi & above squid3 machine should be under
same proxy), long press on connected Wifi and select modify network(from
ICS onwards only), Then enable Show advance options -> Proxy settings
(select manual) Add your squid3 server's detail here (for above example
it would be) Proxy hostname 192.168.1.2 Proxy port 3128 Bypass proxy for
127.0.0.1,localhost Then add your static IP/Gateway/DNS as usual, and
for Network prefix give 16 (if your subnet mask is 255.255.0.0, if not
make sure to find one) Save settings, disable and enable WiFi to make it
active. The only disadvantage is you need to engage a machine to use
this feature.

.. _here: http<code>://w</code><code>ww.appszoom.com/android_applications/communication/proxydroid_xtmc_download.html
