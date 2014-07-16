Firefox Market Place Installation 
#################################

:date: 2014-07-16 11:20
:author: Amit Shrivastava
:pagetitle: Firefox market place installation
:keywords: Firefox, market place, zamboni
:tags: Firefox, Market place, zamboni, firefox apps,M2crypto, virtualenv, python2.6
:description: zambuni installation on the ubuntu
:slug:	firefox-market-place-installation
 
 


Introduction
============
You can install your own market place and host your firefox apps on it. `Zamboni` is one of the code base for the market place.
There is the official documentation for the its installation, But my documentation is specific for the proxy base network and on the Ubuntu 12.04 OS. 

Required Packages
=================
* Python2.6
* Virtualenv
* mysql server 
* Redis 

Required Libraries
==================
* run the command to install the libraries. 

::
        
        sudo apt-get install libxml2-dev libxslt1-dev libmysqlclient-dev libssl-dev swig openssl  pngcrush redis-server

 

Clone the zamboni source 
========================

::

        git clone --recursive git://github.com/mozilla/zamboni.git

Creating virtualenv
===================

* To know more about virtualenv click here virtualenv_ 
* To configure python2.6 on ubuntu 12.04 click here python2.6_

.. _virtualenv: http://gnu-linux.org/virtualenv
.. _python2.6:  http://gnu-linux.org/python2.6

::
        
      virtualenv -p /usr/bin/python26 zamboni

      
Installation and build of packages
==================================

::
        
        make update_deps

* During this process you will face some problem while clone some packages from the git hub. 

* In the clone directory of zamboni you will find the directory name requirements, It contain the file which the script use while installating and cloning the packages. 
* During the cloning of the amo-validator and app-validator you will find the error inside the proxy environment.
* clone these repo seprately using the https link and again run `make update_deps`

::


        inside zamboni/zamboni/src
        git clone https://github.com/mozilla/amo-validator.git
        cd amo-validator/jetpack
        git clone https://github.com/mozilla/app-validator.git

* During this `make` the first file runs is prod.txt which clone number of required packages and other python and django packages. 

* The other error you may get while running the complied.txt file during the compilation of the `M2crypto` packages.

::

        error
        SWIG/_m2crypto_wrap.c:6116:1: error: unknown type name ‘STACK’
        ... snip a very long output of errors around STACK...
        SWIG/_m2crypto_wrap.c:23497:20: error: expected expression before ‘)’ token
        result = (STACK * ) pkcs7_get0_signers(arg1,arg2,arg3);
        error: command 'gcc' failed with exit status 1

* Solution is to comment the M2crypto in the compiled.txt inside the requirements dirctory. 


  ::

        DEB_HOST_MULTIARCH=i386-linux-gnu pip install -I --exists-action=w "https://alioth.debian.org/anonscm/git/collab-maint/m2crypto.git"

        pip install --no-deps -r requirements/dev.txt

* After this uncomment the M2crypto and recompile the code using `make update_deps`        
* Again an error comes if you dont have the `npm` install it and recompile the source

To know more about npm_

.. _npm: http://gnu-linux.org/npm


* You may also get error while npm runs

 ::
        
        Error: SSL Error: SELF_SIGNED_CERT_IN_CHAIN

        Solution: npm config set ca ""

* recompile the source code, If nothing goes wrong it will succesfully build. 

# Second step is to create the mysql database.  

* Create the database

::
        
        mysqladmin -uroot create zamboni

# Make sure there is no password for the mysql 

::

        mysqladmin -u root -pCURRENTPASSWORD password ''

# Now just run command to install landfill database

::
        
        ./manage.py install_landfill

# Update the database

::
        
        make update_db

# Run the server


::

    cd zamboni
    ./manage.py runserver
    or 
    ./manage.py runserver 0.0.0.0:8000  to run from your ip address

# Open browser

::
        
        http://localhost:2600/services/monitor
        or 
        http://yourip:8000/services/monitor 


        
