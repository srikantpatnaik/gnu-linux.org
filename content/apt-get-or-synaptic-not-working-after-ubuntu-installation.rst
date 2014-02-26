apt-get or synaptic not working after ubuntu installation !
###########################################################
:date: 2011-12-17 23:12
:author: srikant
:category: blogs
:tags: apt-get, Could not get lock /var/lib/dpkg/lock, jockey, Resource temporarily unavailable, synaptic, ubuntu
:slug: apt-get-or-synaptic-not-working-after-ubuntu-installation

Many times you might have faced this problem.With Ubuntu live CD or
fresh installation there is  additional drives installer which runs in background.

You get the error as `Could not get lock /var/lib/dpkg/lock` .The simple solution 
to this is to kill that background process.The process responsible for locking is jockey('additional drivers')::


    killall jockey-gtk      (for ubuntu)

    killall jockey-backend && killall jockey-kde    (for kubuntu)

Thats all.Now open your synaptic/software-manager to install packages.
