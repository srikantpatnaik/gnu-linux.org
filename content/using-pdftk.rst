using pdftk
###########
:date: 2012-08-26 18:15
:author: tas_devil
:category: blogs
:tags: commandline, join, linux, merge, pdftk, secure, split, terminal
:slug: using-pdftk

.. raw:: html

   <div id="outline-container-1" class="outline-3">

merging
~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-1">

suppose I have some pdf pages like

.. code-block:: identifier

    front.pdf, toc.pdf, auth_colo.pdf, part1.pdf, chap01.pdf,
    chap02.pdf, part2.pdf, chap03.pdf, chap04.pdf, chap05.pdf,
    part3.pdf, app_A.pdf, app_B.pdf, and, index.pdf

I want to merge all the pdf's into a single book, then my command will
be

.. code-block:: identifier

    pdftk front.pdf toc.pdf auth_colo.pdf part1.pdf chap01.pdf ... index.pdf cat output my_full_book.pdf

this will create a pdf file in the same order in which I have specified.
*\*.pdf* may also work if I don't care about page ordering. Remember
that ``my_full_book.pdf`` is my output file name and ``cat output`` are
output flags.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-2" class="outline-3">

removing a page
~~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-2">

suppose I want to remove 'pages 3' then my command will be

.. code-block:: identifier

    pdftk my_full_book.pdf cat 1-2 4-end output full_book_with_page2-removed.pdf

in the above example, I have skipped page number which I want to remove,
page ``3`` in this case. The above command means, I want pages to be
included from 1 to 2, I don't want page number 3, so **skip it**, then
start from page 4 till the **end**.

the syntax goes like this

.. code-block:: identifier

    pdftk PDF_FILE cat FROM-TO FROM-end output NEW_PDF_FILE_NAME

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-3" class="outline-3">

rotating pages
~~~~~~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-3">

If I want to rotate the first page at 90 degrees right, then

.. code-block:: identifier

    pdftk my_full_book.pdf cat 1R 2-end output page1_turned_right.pdf

in the same way if I want to rotate all odd pages from range 1 to 25 to
180 degrees, then

.. code-block:: identifier

    pdftk my_full_book.pdf cat 1-25oddD 26-end output odd_pages_book.pdf

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="outline-container-4" class="outline-3">

Reference
~~~~~~~~~

.. raw:: html

   <div class="outline-text-3" id="text-4">

For more info on ``pdftk``, visit its manual pages by typing

.. code-block:: identifier

    man pdftk

.. raw:: html

   </div>

.. raw:: html

   </div>

