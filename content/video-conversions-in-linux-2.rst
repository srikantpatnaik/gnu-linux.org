Video conversion in Linux
#########################
:date: 2011-11-22 12:31
:author: srikant
:category: blogs
:tags: Arista transcoder, convert to avi, ffmpeg, mencoder, mp4 converter in linux, ogv converter, Transmageddon, video converter ubuntu, Winff
:slug: video-conversions-in-linux-2

Converting videos is as simple as watching them on Linux.

I will list few GUI based applications to convert,but i personally don't
use them.

#. \ `Arista Transcoder`_\ 
#. \ `Transmageddon`_\ 
#. \ `Winff`_\ 

.. raw:: html

   <div>

.. raw:: html

   <div>

What I suggest is \ **ffmpeg **.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

ffmpeg is a command line tool which can convert almost any video
format.Most of the GUI based converters use this as backend.On any Linux
installation just install it from their respective package repositories
or download it from the this `link`_.

.. raw:: html

   </div>

I will not go in detail here,but will show some simple examples.To move
seamlessly I also recommend you to install two more packages

-  ffmpeg2theora
-  mencoder

Let's see few examples :

#. \ **Converting .mpg to .avi**\ 

    ffmpeg -i input.mpg out.avi

 

2.  **Converting .wav to .mp3**

.. raw:: html

   <div>

    ::

        ffmpeg -i input.wav -ab 128 output.mp3

::

       3. Extract audio from video file

    ::

        ffmpeg -i input.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 output.mp3

::

       4. Converting and optimizing .ogv format

    ::

        ffmpeg2theora --optimize -F 2 -v 10 Kicad_tut2.ogv -o awesome.ogv

        Options :
        -F 2 -> force to 2 fps
        -v 10 -> makes video quality 100%
        --optimize -> help u reduce size
        -o -> output video 

    ::

::

       5. Cutting a certain duration from movie clip

    ::

        ffmpeg -i MOV00114.MPG -sameq -ss 00:00:00 -t 00:08:00 outfile.mpg

    ::

        Options :

    ::

        -sameq -> same quality

::

There are tons of other options available with *ffmpeg* and
*mencoder*.Please use *man pages*

for more detailed information and examples. I'll keep on adding more
examples in due

course of time.Please add your comments/suggestions so that i can make
this page more reachable.

.. raw:: html

   </div>

.. _Arista Transcoder: http://www.transcoder.org/
.. _Transmageddon: http://www.linuxrising.org/
.. _Winff: http://winff.org/html_new/
.. _link: http://ffmpeg.org/download.html
