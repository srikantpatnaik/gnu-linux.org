what is Git?
############
:date: 2012-08-24 18:05
:author: tas_devil
:category: what is
:tags: git, git add, git commit, github, version control
:slug: what-is-git

`Git`_ is a `version control`_ software used to manage documents and
source-code of a software program over time and between people. As we
know that the software changes with time with many updates and BUG
fixes. Sometimes it happens such that the latest changes implemented in
a source-code makes it completely unusable, and if the copy of the
previous working code is not kept safely, all the work is in vain.

**Git** does the job of maintaining the state of file pretty well and in
a neat and clean fashion. Developers and users don't have to keep
multiple copies of a file. They just have to tell git that *this* file
is to be managed by version control and all the changes to the file is
taken care by git. We don't have to keep a copy of same file with
different names like

*barCodeScanner\_2\_aug\_2012.c*

or

*barCodeScanner\_new\_feature\_10\_aug\_2012.c*

When a file is managed by git, there will be only one instance of a file
named *barCodeScanner.c* and the changes occurred to the file is
recorded in terms of `commits`_. ``commit`` stores the current state of
the file with a log message described by user. The commit log also
stores details like ``commit hash`` which is unique hash code for every
commit along with user details, date-time and changes between two
commits. So if the user made some changes in a file and now wants to go
back to previous working state of that file, he just have to `revert`_
to that commit and start again. This is easy and safe way to manage
software repositories with time and between people.

Git is also good at managing remote repositories, where many developers
can come together and can work on a same project simultaneously without
worrying of conflicts in a code. Git repositories can be hosted on sites
like `github.com`_ and `gitorious.org`_, or you can create your own
git-server.

If you are having a debian-based distro, you can install **git** by
typing

.. code:: src

    sudo apt-get install git

on red-hat based distro like fedora, mandriva etc., you can install it
by typing

.. code:: src

    yum install git

or else you can install it by compiling the latest source-code which can
be found on this `link`_.

If you are not comfortable with the command-line version of git, the GUI
client are **git-cola** and **SmartGit** for linux distros, more
information can be found `here`_. An excellent `documentation`_ and
`book`_ is available free. If you are too lazy in reading those, watch
these `videos`_.

.. _Git: http://git-scm.com/
.. _version control: http://en.wikipedia.org/wiki/Revision_control
.. _commits: http://www.kernel.org/pub/software/scm/git/docs/git-commit.html
.. _revert: http://www.kernel.org/pub/software/scm/git/docs/git-revert.html
.. _github.com: https://github.com/
.. _gitorious.org: http://gitorious.org/
.. _link: http://git-scm.com/downloads
.. _here: http://git-scm.com/downloads/guis
.. _documentation: http://git-scm.com/doc
.. _book: http://git-scm.com/book
.. _videos: http://git-scm.com/videos
