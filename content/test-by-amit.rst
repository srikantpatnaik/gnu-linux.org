test by amit
############
:date: 2014-02-14 01:33
:author: tas_devil
:category: android
:tags: android, ant, avd, command line, sdk, terminal
:slug: test-by-amit

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

<div class="outline-3" id="outline-container-3-3">

Launching your app
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3-3">

To test your app, type

Syntax::

    adb shell am start -a android.intent.action.MAIN -n your-package-name/.your-main-activity-name

Example::

    adb shell am start -a android.intent.action.MAIN -n com.hello.android/.MainActivity

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

