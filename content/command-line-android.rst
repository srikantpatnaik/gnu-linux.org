Command-line Android
####################
:date: 2013-02-24 01:24
:author: tas_devil
:category: android
:tags: android, ant, avd, command line, sdk, terminal
:slug: command-line-android

We often use *Eclipse* for Android programming. Of-course creating an
Android project is simple and easy for a beginner and advance user using
Eclipse. Eclipse creates a file hierarchy needed for an Android project.
Also building and running an ``apk`` is even simpler. But for those who
don't want to switch to GUI or who want to stick to the terminal for
Android programming, read on ..

.. raw:: html

   <div class="outline-2" id="outline-container-1">

Creating an Android project
---------------------------

.. raw:: html

   <div class="outline-text-2" id="text-1">

Provided you have an *android-sdk* in your path.

**Syntax**

.. code:: src

    android create project \
        --name project-name \
        --target target-API \
        --path path-to-your-project \
        --package package-name \
        --activity name-of-your-main-activity

**Example**

.. code:: src

    android create project \
        --name HelloAndroid \
        --target android-15 \
        --path . \
        --package com.hello.android \
        --activity MainActivity

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="outline-2" id="outline-container-2">

Building an apk
---------------

.. raw:: html

   <div class="outline-text-2" id="text-2">

Building an apk is also simple, type

.. code:: src

    android update project --path . --target android-15 --subprojects

which will create a necessary ``build.xml`` file required for ``ant``,
and run

.. code:: src

    ant debug

this will create an *unsigned-debug* apk inside the *bin* directory of
your project.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="outline-2" id="outline-container-3">

Testing your app
----------------

.. raw:: html

   <div class="outline-text-2" id="text-3">

.. raw:: html

   </div>

.. raw:: html

   <div class="outline-3" id="outline-container-3-1">

Starting emulator
~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3-1">

Start the AVD using,

**Syntax**

.. code:: src

    emulator -avd name-of-your-avd

**Example**

.. code:: src

    emulator -avd test

If you want to list all your virtual disks, type

.. code:: src

    android list avd

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="outline-3" id="outline-container-3-2">

Installing an apk
~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3-2">

To install an apk, visit your project directory and run

**Syntax**

.. code:: src

    adb install path-to-your-apk

**Example**

.. code:: src

    adb install bin/com.hello.android.MainActivity.apk

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="outline-3" id="outline-container-3-3">

Launching your app
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3-3">

To test your app, type

**Syntax**

.. code:: src

    adb shell am start -a android.intent.action.MAIN -n your-package-name/.your-main-activity-name

**Example**

.. code:: src

    adb shell am start -a android.intent.action.MAIN -n com.hello.android/.MainActivity

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

