How to add onboard in minimal lxde ?
####################################
:date: 2012-12-10 16:40
:author: srikant
:category: blogs
:tags: linux, lxde, onboard, python-gi-cairo
:slug: how-to-add-onboard-in-minimal-lxde

onboard is  popular new age virtual keyboard in ubuntu environment. It
sometimes won't work  properly in minimal lxde setup. The reason is
missing python dependency *python-gi-cairo.
*\ So install this package along with onboard :

    apt-get install python-gi-cairo onboard
