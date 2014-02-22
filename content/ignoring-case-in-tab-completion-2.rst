Ignoring Case in TAB-Completion
###############################
:date: 2011-10-26 10:21
:author: tas_devil
:category: blogs
:tags: ignoring case in GNU/linux terminal, linux terminal, shell, tab auto complete, tab completion, ubuntu shell
:slug: ignoring-case-in-tab-completion-2

By Default TAB-Completion is not useful if the name of file or directory
starts with an UpperCase. You can make your Shell totally ignore the
case(in-case sensitive) by adding following entry in /etc/inputrc
file(you need root access).

    set completion-ignore-case on

Save the file and restart your Shell. From now onwards TAB-completion
will completely ignore the case for file or directory.

for complete man page type:

    man readline
