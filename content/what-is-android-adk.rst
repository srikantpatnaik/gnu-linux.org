What is Android ADK ?
#####################
:date: 2011-10-26 08:40
:author: srikant
:category: android
:tags: android, arduino, embedded, gingerbread, google io 2011, honeycomb, usb host
:slug: what-is-android-adk

This summer google announced in its third I/O about its ambitious
project, interfacing every single hardware in your house to android
device.

| The **Android Open Accessory Development Kit (ADK)** is USB
based implementation and connects to Arduino (open source hardware)  or
similar accessories .
| 

|image0|

The idea is to make android device to communicate with android accessory
(mostly Arduino device). The android accessory will act as USB host and
power(5V ,500mA) the android device(phone or tablet).This is very
simple.Android accessories will be specially designed to attach with
Android-powered devices and adhere to a simple protocol (Android
accessory protocol) that allows them to detect Android-powered devices
that support accessory mode.You can turn any device (light
bulb,fan,washing machine, treadmill,toys,coffee machine,TV,garage,BP
monitor etc ) to an Android accessory by adding a small embedded
(hardware & software) support to it.When your accessory is ready you
need to write corresponding app on android device to do meaningful job.

 

 

 

|image1|

 

More details can be found at
http://developer.android.com/guide/topics/usb/adk.html  .

Details on Arduino open hardware/software project can be found at
`arduino.cc`_ .

.. _arduino.cc: http://arduino.cc/

.. |image0| image:: http://gnu-linux.org/wp-content/uploads/2011/10/arduino-android.png
   :target: http://gnu-linux.org/wp-content/uploads/2011/10/arduino-android.png
.. |image1| image:: http://gnu-linux.org/wp-content/uploads/2011/10/PT_101006.jpg
   :target: http://gnu-linux.org/?attachment_id=
