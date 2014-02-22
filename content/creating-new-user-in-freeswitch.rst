Creating new user in FREESWITCH 
################################
:date: 2013-12-23 12:43
:author: camitr
:category: blogs
:tags: freeswitch, freeswitch installation, freeswitch user create
:keywords: freeswitch, freeswitch installation, freeswitch user create
:slug: creating-new-user-in-freeswitch
:description: Freeswitch on Linux


If you successfully install the FREESWITCH. In this post I will explain
how to create the new user or modify the existing user.

| Step 1. Locate the conf directory inside the freeswitch installed
directory.
|  Step 2. change directory to default/

::

     # cd conf/directory/default

| This directory contain xml file related to default user extension to
be used.
|  Step 3. To create a new user cp any of the file and name it with your
desired extension.

::

     # cp 1000.xml 9999.xml

Step 4. Make the changes to new file as per your extension.

::

     # vim 9999.xml 
      change the following tags 
            user id="9999"
    choose your password.
            param name="password" value="123"
    If you want to change call group make changes in variable tag or default can also work.

::

     For new group make changes in make changes in default.xml
    # vim conf/directory/default.xml 
    the file is self descriptive.

Step 5. Make change Regex in dialplan

::

     # vim conf/dialplan/default.xml 
    locate  tag line # 257 
    change the regex with your extension number in my case I included 9999

::

     expression="^(10[012][0-9]|9999)$"

Step 6. Reload the xml file using fs\_cli terminal

::

    # fs_cli
    freeswitch@internal> reload xml

::

    Its done .... 
    Now  test your new extension using your softphone.

