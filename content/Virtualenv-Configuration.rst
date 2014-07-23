Virtaulenv configuration
########################

:date: 2014-07-17 10:45
:author: Amit Shrivastava
:pagetitle: Virtualenv
:keywords: Virtualenv, virtual environment
:tags: virtualization, Virtualenv
:description: Configuration and installation virtualenv in ubuntu
:slug:	virtualenv-configuration

Introduction 
============
It creates a virtual environment to isolate the working copy of the python which 
allow us to work on the specific project without affecting the system other projects. 
It helps in working on different version of the packages without affecting the other 
version. For example you can work on the python2.6 with isolated enviroment with 
python2.7 on your OS.

*Version* The latest version of the virtualenv 1.11.6 release on 16 May 14

Installation
============
You can use pip (python package index) or from source_ to install the virtualenv 

.. _source: https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.6.tar.gz

* Open your terminal and type below commands

::
        
        pip install install virtualenv

* Create virtualenv

::
        
        virtualenv myapp

- myapp will be your virtualenv which contain 4 directories
        1. bin
        2. include
        3. local
        4. lib           

- To enable virtualenv 

::


        source bin/activate


- you will find this on your terminal 

::

        
        (myapp)user:myapp$
        

- To disable virtualenv

::
        
        (myapp)user:myapp$ deactivate

- To create virtualenv with specific python version 

::
        
        virtualenv -p /usr/bin/python2.6 myapp 


Virtual wrapper
===============
It contain set of commands for virtualenv and intregate all your virtualenv at one place. It helps in managaing multiple virtualenv 

Installation
------------

::

        pip install virtualenvwrapper

        
- Set the home directory for virtual environments

::
        
        export WORKON_HOME=~/myvirtual
        source /usr/local/bin/virtualwrapper.sh


::
        
        mkvirtualenv app
        workon app
        rmvirtualenv app

- This  create all the virtualenv inside  directory myvirtual    
        


        
        
