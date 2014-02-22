'ls' command doesn't show colors in konsole !
#############################################
:date: 2011-12-14 10:57
:author: srikant
:category: blogs
:tags: alias, bash.bashrc, konsole color, kubuntu konsole color, ls color
:slug: ls-command-doesnt-show-colors-in-konsole

Gnome-terminal shows default coloring for files and directories but
konsole doesn't. Those who love Kubuntu always see this difference.Here
is the simple trick to add the file highlighting in konsole.

    alias ls='ls --color=auto'

This will highlight the different colors for  *ls*\ output.To save this
permanently for your konsole just add this line to bash.bashrc file.

    sudo vi /etc/bash.bashrc 

Add \ *ls='ls --color=auto'*\ at the end of bash.bashrc file.And you are
done.
