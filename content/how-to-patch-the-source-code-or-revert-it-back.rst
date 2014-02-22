How to patch the source code or revert it back?
###############################################
:date: 2013-06-21 12:47
:author: tas_devil
:category: blogs
:tags: kernel, patch, revert, source code
:slug: how-to-patch-the-source-code-or-revert-it-back

We often have the situation of testing or applying someones patch or to
remove the changes made by a patch. It may happen that a patch is not
correctly applied and result into to dirty source code. This simple bit
of information will help you to carefully apply the patch to your source
code and also revert the changes back to original state if required. I'm
using linux kernel version **3.0.42+** as example and Elan Touch Screen
patch file(patch-linux-3.0.42+\_elan\_ts.patch).

Unpack and change directory to your linux kernel version you want to
apply the patch for. I this case my kernel version is 3.0.42+

.. code-block:: identifier

    cd linux-3.0.42+

I have a patch file in the ~/Downloads directory. Patch files generally
ends with ``.patch``. This helps in differentiating them as patches.

It is always recommended to do a dry run before actually applying a
patch.

.. code-block:: identifier

    patch -p1 --dry-run < ~/Downloads/patch-linux-3.0.42+_elan_ts.patch

#. Here ``-p1`` stands for verbosity. For more information, please refer
   comment by *Yogesh* `here`_.
#. ``--dry-run`` will not actually apply a patch, but gives you an
   output as if the patch is really applied.

if ``--dry-run`` applies a patch without any error message, you can go
ahead an apply a real patch.

.. code-block:: identifier

    patch -p1 < ~/Downloads/patch-linux-3.0.42+_elan_ts.patch

Now if you want to remove a patch just add the flag ``-R``. For example,

.. code-block:: identifier

    patch -R -p1 < ~/Downloads/patch-linux-3.0.42+_elan_ts.patch

Remember you have to give full path to your patch file when you apply or
revert a patch. If you plan to apply or revert a patch it is recommended
to apply/revert one patch at a time. In this way you can carefully
manage you patches.

Hope this was helpful.

Linux kernel has an excellent documentation on the topic
`applying-patch`_.

.. _here: http://www.cyberciti.biz/faq/appy-patch-file-using-patch-command/
.. _applying-patch: https://www.kernel.org/doc/Documentation/applying-patches.txt
