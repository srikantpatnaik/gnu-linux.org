Enable Kernel virtualization on Intel/AMD arch
##############################################
:date: 2012-08-23 11:51
:author: tas_devil
:category: blogs
:tags: /proc/cpuinfo, egrep, kernel, modrpobe., svm, virtualization, vmx
:slug: enable-kernel-virtualization-on-intel-arch

To check if the hardware supports Virtualizaton Technology(VT), open a
terminal and type

.. code:: src

    egrep '(vmx|svm)' /proc/cpuinfo

if you can see some output, then your hardware supports VT.

Next to enable kernel modules, type

.. code:: src

    sudo modprobe kvm_intel
    sudo modprobe kvm

.. raw:: html

   <div id="outline-container-1" class="outline-3">

Note
~~~~

.. raw:: html

   <div id="text-1" class="outline-text-3">

-  **vmx** - is for Intel
-  **svm** - is for AMD

.. raw:: html

   </div>

.. raw:: html

   </div>

