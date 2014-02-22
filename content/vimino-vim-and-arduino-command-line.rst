vimino: Vim and arduino command line
####################################
:date: 2013-10-10 14:39
:author: srikant
:category: blogs
:tags: arduino, command line arduino, inotool, vim, vim key mapping
:slug: vimino-vim-and-arduino-command-line

If you're an arduino folk who has no regards for the Java IDE, then
upgrade your life now.

**Benifits with vimino (Vim + ino):**

1) Using Vim to write arduino code, ofcourse with syntax highlight

2) Using Vim keymap to compile and upload the hex file to Arduino board
(using inotool)

**Steps to perform:**

1) Download the vim syntax file from `here`_

2) Move the downloaded ***arduino.vim***\ file to
***~/.vim/syntax/arduino.vim***

3) Create a file\ ***~/.vim/ftdetect/arduino.vim***\ and add the
following line

***autocmd BufNewFile,BufReadPost \*.ino,\*.pde set filetype=arduino***

4) Install the ***arduino*** IDE distribution(for libraries & tools, we
are not going to use IDE for sure) and ***picocom***

5) Install\ ***ino***\ by either ***pip install
ino ** *\ or\ ***easy\_install ino***. This package is required
to compile and upload your sketches.

6) Open your **~/.vimrc** file and add the following line at the end:

***map <buffer> <F3> :<Esc>:w<CR>:!clear<CR>:!ino build<CR>:!ino
upload<CR>: <Ins> <CR>***

save and exit.

This will map your<F3> key to build and upload from inside Vim
environment.

7) Now follow the steps given at inotool.org/quickstart to test your
first blinky code.

NOTE:  To use\ **<F3> keymap**, open the source file from project's root
directory. For example,

**vim src/sketch.ino**

Now connect your arduino uno hardware and press <F3> to enjoy.

You will be thrilled to notice that how much time and effort it saves to
test your sketches.

Tested on **Ubuntu 12.10**

 

.. _here: http://www.vim.org/scripts/download_script.php?src_id=17108
