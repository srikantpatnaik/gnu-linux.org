what is Emacs?
##############
:date: 2012-08-25 08:43
:author: tas_devil
:category: what is
:tags: elisp, emacs, GNU, GNU/Emacs, IDE, linux, lisp, text editor, XEmacs
:slug: what-is-emacs

Well a straight answer to this question is "*GNU/Emacs is a text
editor*\ " which can be easily extended and customized. But I would say
its an **Operating system** in which one can do anything from managing
other processes, files, folders, check mails, browse web and even listen
to music apart from just editing text and writing codes. For developers
and coders it acts as an full fledged `IDE`_.

People often complain that `Emacs`_ has lots of key-bindings which can
be frustrating sometimes, but trust me after a while once you get used
to it, you will discover that you have started working faster and in a
much managed way. Be it a task like writing a `blog`_, or a programming
code, Emacs has support for almost all programming languages in the
world with common support such as *syntax highlighting*, *code
indentation*, *auto-completion* and many more.

.. raw:: html

   <div class="outline-3" id="outline-container-1">

Key features
~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

#. **buffer**: If one is used to work with multiple files at a same
   time(tabs), then emacs *buffer* is something similar. What puts emacs
   *buffer* stand apart from normal tabs is that these *buffers* don't
   just holds files, but also shell, scratchpads, output logs from emacs
   or some other programs. One can switch between these *buffers* easily
   with **C-x b** which stands for "hold down **Control key** and press
   **x**, released both keys and press **b**". If you think this
   key-binding is cumbersome, then you can install an emacs
   extension(its just an .el file) called `CycleBuffer`_ and switch
   buffers with function keys[F11,F12].
#. **ring**: In any text editor you have used so far, we can only
   cut/copy paste one buffer at a time, which means when we copy
   something that will overwrite any existing buffer. Emacs goes a
   different way, means when we copy something, emacs stores it as an
   array or a ring, and we can cycle through in a circular fashion and
   can select particular item.
#. **tramp**: Using this mode, you can edit remote file by calling it in
   your local buffer.
#. **mark ring**: You can mark points in buffers and visit it later
   using **C-<SPC> C-<SPC>**.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="outline-3" id="outline-container-2">

help in GNU/Emacs:
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-2">

a. If you want to get started with GNU/Emacs, is has built-in self
tutorial which can be called using **C-h t**.

b. for detailed manual type **C-h r**

.. raw:: html

   </div>

.. raw:: html

   </div>

.. _IDE: http://en.wikipedia.org/wiki/Integrated_development_environment
.. _Emacs: http://www.gnu.org/software/emacs/
.. _blog: https://github.com/punchagan/org2blog
.. _CycleBuffer: http://www.emacswiki.org/CycleBuffer
