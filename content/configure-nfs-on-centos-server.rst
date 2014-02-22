Configure NFS on Centos Server 
###############################
:date: 2012-09-27 12:21
:author: camitr
:category: blogs
:slug: configure-nfs-on-centos-server

| NFS stands for Network File System, through NFS a client can access
(read & write) directory shared by the NFS server. Its a distributed
system protocol originally designed by SUN Microsystem. The shared
storage act as a local storage for the client.
|  The post will guide to configure NFS server & client on CENTOS 6.2.
 Here we consider a scenario of two linux machine.

| Machine 1-: NFS-server: IP address-> 10.10.10.1
|  Machine 2-: NFS-client: IP address-> 10.10.10.2

**Configuration For  NFS-server**

| **Step-1** Download the NFS package on server
|  # yum install nfs-utils nfs-utils-lib
|  # service nfs start

| **Step-2** Exporting the directory to share on server
|  I will make a directory /var/nfs  to be shared with the client
machine,for this we have to export the directory.
|  When a client access a NFS share, its normally happens as the user
nobody. So create a directory /var/nfs and change its permissions. Make
owner of directory to user **nobody** user id as **65534**

| #mkdir /var/nfs
|  #chown 65534:65534 /var/nfs
|  #chmod 777 /var/nfs

| edit in the /etc/exports directory to export our NFS share.
|  # vim /etc/exports
|  /var/nfs                              
 10.10.10.2(rw,sync,no\_subtree\_check)

save and quit the file.

| Whenever we modify /etc/exports. must run
|  # exportfs -a

This end the server side configuration for NFS.

| **Configuration For  NFS-Client **
|  \ **
Step 1.** Download the NFS package
|  # yum install nfs-utils nfs-utils-lib
|  Create the directory to Mount for NFS share
|  # mkdir -p /mnt/nfs
|  **Step 2.** Mounting the shared directories
|  # mount 10.10.10.1:/var/nfs   /mnt/nfs
|  mount take 2 parameters, first is NFS server IP and  directory which
is exported and second is the NFS client directory to mount.

| To check the mounted directory run command
|  # df -h
|  Filesystem      Size      Used     Avail     Use%    Mounted on
|  /dev/sda6        56G      6.5G     47G      13%        /
|  10.10.10.1:/var/nfs  30G 20G   10G     66.66%  /mnt/nfs

This create the temporary mount point for NFS shared. To make boot time
mount point make entries in /etc/fstab. Open the file using vim editor
and make the following entries at bottom of file with NFS specification.

| # vim /etc/fstab
|  10.10.10.1:/var/nfs     /mnt/nsf     nfs   rw,sync,hard,intr 0 0

It contains server name:path    /mountpoint     fstype  option,
option.....

| **Testing the configure NFS**
|  \ **
 Step 1.** Create empty file on NFS client share directory 
|  # touch /mnt/nfs/test.txt
|  **Step 2.** Check the files on the server
|  # cd /var/nfs
|  # ls
|  # test.txt

NFS configuration is completed.

 

 

 

 

 

 
