How to install cyanogeod 7.1 on zte blade a.k.a dell xcd35 ?
############################################################
:date: 2011-10-26 03:59
:author: srikant
:category: android
:tags: android, android 2.3.7, ClockworkMod, cyanogenmod 7.1, dell xcd35, gingerbread, ROM Manager, zte blade
:slug: how-to-install-cyanogeod-7-1-on-zte-blade-a-k-a-dell-xcd35

The cyanogenmod ROMs are getting more popular than stock ROMs(one which
comes with default android). The reason is simple.They have latest
versions,have good community support and above all they have additional
features,like DSP equalizer,full customization options,CPU Clock speed
control etc.The list of supported devices can be found at this
**`link`_**.

In today's hack i'll will show you steps you need to follow in order to
install cyanogenmod successfully on your Dell XCD-35 (a.k.a ZTE
Blade,San Francisco Orange) .

Please note that,this may break your warranty and you may loose your
data.I assume you understand the risk of doing this.Unless you're very
sure,please don't proceed.We are not responsible for any damage done to
your device.

 

*Steps to follow :*

 

#. Root your device. Rooting means getting administrative permissions
   for your device.Usually every android device is locked by the
   vendor.Without sufficient knowledge one can break the device with
   rooting.So careful.The only 'apk' which worked for me for rooting
   this device is '**`z4root\_blade\_perm\_root\_v2.apk`_**\ '
   .(download this file,and extract the zip file to get '.apk').
#. Then install free version of ROM manager from android market.
#. Open the app ROM manager and choose first option 'Flash ClockworkMod
   Recovery'.Which will download 'recovery-clockwork-xxxx.img' file(3.7
   MB).
#. Then from your PC's browser download the latest cyanogenmod
   image(update-cm-7.1.0-Blade-signed.zip).In my    case it is this
   link[\ **`download`_**\ ].Place the zip file i.e cyanogenmod image
   zip      file(around 90 MB) in your SD Card (don't create any
   folder).Also no need to format your SD Card or deleting your previous
   data.
#. Now choose the 2nd option i.e 'Reboot into Recovery' from your
   android phone.The screen will go   blank and phone will restart.
#. Once the device boots into the ClockworkMod Recovery, use the side
   volume buttons to move up   and down, home button to select and back
   button to go back. In 'ClockworkMod Recovery' mode touchscreen will
   not work.This mode is useful to    install/remove/backup any stock or
   custom ROMs.
#. Select \ **backup and restore**\  to create a backup of current
   installation.In my case it was android 2.2.    (optional step)
#. Then select option to **Wipe data/factory reset**\ ,then \ **clear
   cache partition**\ .It will take few seconds    and will show you the
   progress.
#. Then select option **Install zip from sdcard**\ .This will show you
   contents of your sdcard.Then \ **Choose zip from sdcard**\ ,after
   that carefully choose the 'update-cm-7.1.0-Blade-signed.zip'.
#. Once the installation finishes,go back using 'back key' and choose
   '**reboot system now**\ ' option.Your phone should now reboot to
   cyanogenmod 7.1 (Android version 2.3.7).During first boot,it will
   take some time.A blue color animation will greet you.That's it.You're
   done.

.. raw:: html

   <div style="text-align: center;">

[caption id="attachment\_1182" align="aligncenter" width="480"
caption="ROM-manager"]\ |image0|\ [/caption]

.. raw:: html

   </div>

.. raw:: html

   <div>

The cyanogenmod doesn't contain any google proprietary apps.You need to
download the zip file(~ 6.7 MB) from
this\ **`link <http://cmw.22aaf3.com/gapps/gapps-gb-20110828-signed.zip>`__**
,and install it by rebooting your phone in ClockworkMod Recovery again
and by following  step number 9 and 10 there after.(No need to repeat
any other step).

.. raw:: html

   </div>

.. raw:: html

   <div>

The installation of google apps can be done during installing
cyanogenmod also(i.e before rebooting during step 10) ,but it didn't
worked in my case.So i installed only cyanogenmod first,then again
repeated step 9 and 10 to install google apps.

.. raw:: html

   </div>

.. raw:: html

   <div>

Feel free to ask any doubts.

.. raw:: html

   </div>

.. raw:: html

   <div>

Don't panic if it doesn't boot,or power key doesn't respond during
boot.Remove the battery and insert it again.Probably you will not need
this step.You may want to use information in cyanogenmod site from the
given
**`link <http://wiki.cyanogenmod.com/wiki/ZTE_Blade:_Flashing_CyanogenMod>`__**.

.. raw:: html

   </div>

.. raw:: html

   <div>

Happy Hacking. :)

.. raw:: html

   </div>

.. raw:: html

   <div>

[gallery]

.. raw:: html

   </div>

 

 

 

.. _link: http://www.cyanogenmod.com/devices
.. _z4root\_blade\_perm\_root\_v2.apk: http://gnu-linux.org/wp-content/uploads/2012/03/z4root_blade_perm_root_v2.apk_.zip
.. _download: http://download.cyanogenmod.com/get/update-cm-7.1.0-Blade-signed.zip

.. |image0| image:: http://techkhabri.com/wp-content/uploads/2011/10/ROM-manager.png
   :target: http://gnu-linux.org/wp-content/uploads/2011/10/ROM-manager.png
