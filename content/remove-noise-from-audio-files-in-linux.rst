Remove noise from audio files in Linux !
########################################
:date: 2011-12-11 18:46
:author: srikant
:category: blogs
:tags: audacity, audacity in ubuntu, audio editor, cross platform audio editor, how to remove noise, noise reduction in linux, remove noise
:slug: remove-noise-from-audio-files-in-linux

Have you ever felt that your favourite song has noise in the background,
or you downloaded an old song which in turn recorded from a old cassette
player resulting in annoying background noise.

|song loaded in audacity|

To remove such constant noise from your songs or recordings we have a
great cross platform tool called `Audacity`.

**Steps to follow:**

1. Install 'Audacity' from package manager.Go to file->open and select
the audio file.

2. File will be imported and will be shown in a timeline.Play the song
and choose the region where noise appears.

[caption id="attachment\_1335" align="alignnone" width="300"
caption="audacity zoom button"]\ |press zoom on audacity|\ [/caption]

3. Select the zoom tool at the top to pan into that region.Then choose
text select tool (just below the zoom tool) to select the region you
find noise.

[caption id="attachment\_1336" align="alignnone" width="300"
caption="select-noise-portion"]\ |select-noise-portion|\ [/caption]

4. Keeping the noise selected, goto Effect -> Noise Removal... and click
on 'Get Noise Profile' .The dialog box will disappear.

5. Now select entire song using ' Cntl + a ' or region of audio you want
to remove noise.

[caption id="attachment\_1337" align="alignnone" width="300"
caption="noise-profile"]\ |image3|\ [/caption]

6. Now again goto Effect -> Noise Removal... and press OK .It will show
a dialog popup stating 'Removing Noise'.

7. By this step you are done.You can hit play button and enjoy noise
free audio ,but you want to export it to mp3/wav to save in your local
machine. For that just goto File -> Export and choose the format and
bitrate you want and select OK.

Enjoy editing :)

 

.. |song loaded in audacity| image:: http://gnu-linux.org/wp-content/uploads/2011/12/zoom.png
.. |press zoom on audacity| image:: http://gnu-linux.org/wp-content/uploads/2011/12/zoom2-300x168.png
   :target: http://gnu-linux.org/wp-content/uploads/2011/12/zoom2.png
.. |select-noise-portion| image:: http://gnu-linux.org/wp-content/uploads/2011/12/select-noise-portion-300x168.png
   :target: http://gnu-linux.org/wp-content/uploads/2011/12/select-noise-portion.png
.. |image3| image:: http://gnu-linux.org/wp-content/uploads/2011/12/noise-profile-300x168.png
   :target: http://gnu-linux.org/wp-content/uploads/2011/12/noise-profile.png
