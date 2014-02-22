renaming master branch in git
#############################
:date: 2012-08-08 11:29
:author: tas_devil
:category: blogs
:tags: git, git branch -M, github, linux
:slug: renaming-master-branch-in-httpgit-scm-comgit

I have ``master`` branch as default branch in `github`_ repository. I
need two more branches called, ``ics`` and ``froyo``, and I want to
rename my ``master`` branch to ``ics``.

.. raw:: html

   <div id="outline-container-1" class="outline-4">

**first create two new branches**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-1">

.. code-block:: identifier

    git branch froyo 
    git branch ics 

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-2" class="outline-4">

**now rename the =master= branch to =ics=**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-2">

.. code-block:: identifier

    git branch -M -a master froyo

**-M** will rename the branch even if the new branch name already
exists.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-3" class="outline-4">

**also I want to remove =master= branch from remote.**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-3">

.. code-block:: identifier

    git push origin :master

Now if I want to set the default branch as ``ics`` on github, then login
to `github`_. Visit the repository, go to the ``Admin`` tab. In the
``Settings`` column, Change the ``Default`` branch from ``master`` to
``ics``.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-4" class="outline-4">

**Tips**
^^^^^^^^

.. raw:: html

   <div class="outline-text-4" id="text-4">

#. **to clone specific branch from git repository**

   .. code-block:: identifier

       git clone -b BRANCH_NAME git@github.com:USER/REPOSITORY.git

   for example,

   .. code-block:: identifier

       git clone -b my-branch git@github.com:androportal/installer.git

#. **copy file from another branch**

   .. code-block:: identifier

       git co BRANCH_NAME FILE

   for example,

   .. code-block:: identifier

       git co froyo html2sphinx.sh

#. **to checkout particular branch from remotes**

   .. code-block:: identifier

       git co -b BRANCH remotes/origin/BRANCH

   for example,

   .. code-block:: identifier

       git co -b froyo remotes/origin/froyo

#. **to remove files from git which are already deleted from system**

   .. code-block:: identifier

       for file in $(git ls-files --deleted); do git rm $file; done

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _github: https://github.com
