Running videos from Linux console
#################################
:date: 2013-01-19 22:31
:author: srikant
:category: blogs
:tags: console video, framebuffer, linux, mplayer, vlc
:slug: running-videos-from-linux-console

Simply play all your videos from console with mplayer or cvlc.

::

    sudo mplayer -vo fbdev2 -zoom -x 1024 -y 600 someVIdeo.ogv

Mplayer is simple to setup and can be run as root, as framebuffer device
(/dev/fb0) needs roots permission. On the other hand vlc can be setup
for frame buffer by changing the video device to Linux framebuffer in
vlc preferences -> video(in X session of course). Though there might be
a command line flag to set it during playback but I couldn't find it.
Yes, I'm lazy. Vlc won't work as root(smart huh..). Any way I chmod
/dev/fb0 to 777 and run as normal user. It worked. Same could be done
with mplayer too.

So you can run it on your console(tty sessions) as

::

    cvlc someVideo.ogv

I can dump my entire X window as soon as some one help me with tabbed
browsing on console. There are some players like links2 and netsurf-fb
but still they haven't attained critical mass. Directfb seems promising
but it failed to solve my web browsing problem.
