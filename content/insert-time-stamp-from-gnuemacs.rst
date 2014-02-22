Insert time-stamp from GNU/Emacs
################################
:date: 2013-02-24 00:07
:author: tas_devil
:category: blogs
:tags: defun, GNU/Emacs, time-stamp
:slug: insert-time-stamp-from-gnuemacs

Often you need to insert a *time-stamp* within a file while working in
GNU/Emacs. One way of doing it is to type

.. code:: src

    C-u C-! date

which will print a string something like

.. code:: src

    Sun Feb 24 00:11:59 IST 2013

What if you want to print a formatted time string ? and to bind that
action with specific key strokes to use within GNU/Emacs ?

Open your **~/.emacs** file and add following code to it.

.. code:: src

    (defun insert-current-time()
      ''insert the current time''
      (interactive ''*'')
      (insert (format-time-string ''%l.%M %p''))
      )

    (global-set-key ''\C-x\C-t'' 'insert-current-time)

reload **~/.emacs** file using

.. code:: src

    M-x eval-buffer

now you can print the time any where within a file by typing

.. code:: src

    C-x C-t

or by using the function ``insert-current-time``

Note that the above code will print the time as

.. code:: src

    12.41 AM

if you want to print a entire time-stamp, replace line starting with
``(insert ....`` from above code snippet with

.. code:: src

    (insert (current-time-string))

