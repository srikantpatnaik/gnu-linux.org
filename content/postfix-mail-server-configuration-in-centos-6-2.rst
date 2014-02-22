Postfix mail server configuration in Centos 6.2
###############################################
:date: 2013-07-05 12:32
:author: camitr
:category: blogs
:tags: centos postfix, dovecot, mail server, postfix, squirrel mail
:slug: postfix-mail-server-configuration-in-centos-6-2

In this post I configure Postfix mail server, Dovecot, and Squirrel
mail. Postfix is a mail server, Which is an alternate to send mail.
Postfix act as Mail Transfer Agent [MTA]. Dovecot is open source IMAP
POP3 server, It act as Mail Delivery Agent [MDA]. The Squirrel mail
provide the web based mail application.

I will explain some of the important term used in mail server
configuration.

1. MTA ----> Mail Transfer Agent, send and received email between the
MTA. Some MTA severs are: Postfix,Sendmail

2. MDA ----> Mail Delivery Agent, Received mail from MTA for delivery to
mailbox. Some MDA are: Dovecot,Procmail

3. MUA ----> Mail User Agent, email client, It can be user web browser
or Thunderbird, .

| Prerequisites-:
|  Your DNS should have MX record entry for your mail server.
|  Firewall and selinux should be disabled.
|  # service iptables stop
|  # vim /etc/selinux/config # line number 7 edit this file to disable
the selinux
|  SELINUX=disabled
|  Reboot your server
|  # init 6

| If your centos server already has sendmail server remove it
|  # yum remove sendmail

My test scenario to configure the mail server

| Hostname =mailon
|  IP address =172.16.1.3

| I have MX record entry for my mail server in my DNS server.
|  **
 Installation**

# yum install postfix -y

| **Configuration**
|  Open the main.cf file in any text editor, I prefer vim
|  # vim /etc/postfix/main.cf

**myhostname = servername.mail.com ## edit the hostname line# 75
 mydomain = mail.com ## edit the domain name line# 85
 myorigin = $myhostname ## comment out the line# 99
 inet\_interfaces = all ## change to all line# 119
 mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
## include $mydomain at the end line# 166
 mynetwork = 172.16.0.0/16, 127.0.0.0/8 ## include your network ip line#
268
 home\_mailbox = Maildir/ ## comment out line 424 to enable inbox
directory**

**Start the Postfix service**

| # service postfix start
|  # chkconfig postfix on ## to start the service on startup

**Testing Postfix**

| [root@servername ~]# **telnet localhost 25**
|  Trying ::1...
|  Connected to local host
|  Escape character is '^]'.
|  220 server.mail.com ESMTP Postfix

**ehlo localhost**

| 250-servername.mail.com
|  250-PIPELINING
|  250-SIZE 10240000
|  250-VRFY
|  250-ETRN
|  250-ENHANCEDSTATUSCODES
|  250-8BITMIME
|  250 DSN

| **mail from: mailuser**
|  mail from: mailuser
|  **rcpt to: mailuser**
|  250 2.1.5 Ok
|  **data**
|  354 End data with .
|  **hello amit this the gnu-linux
 .**
|  250 2.0.0 Ok: queued as 4C8F91E00F5
|  **quit**
|  221 2.0.0 Bye
|  Connection closed by foreign host.

**Check the mail in user Maildir**

| [root@mailon ~]# cd /home/mailuser/Maildir/new
|  [root@mailon new]# vim 1373093244.Vfd03I20023M85510.mailon
|  Return-Path:
|  X-Original-To: mailuser
|  Delivered-To: mailuser@servername.mail.com
|  Received: from localhost (localhost [IPv6:::1])
|  by servername.mail.com (Postfix) with ESMTP id 4C8F91E00F5
|  for ; Sat, 6 Jul 2013 12:15:24 +0530 (IST)
|  Message-Id:
|  Date: Sat, 6 Jul 2013 12:15:24 +0530 (IST)
|  From: mailuser@servername.mail.com
|  To: undisclosed-recipients:;
|  hello amit this the gnu-linux

If you got the mail it means postfix is working now.

Issues--> if you do not get the mail. Check the log detail in
/var/log/maillog, If you you find the permission denied error. Check the
the permission on Maildir in user home, make it writeable or if it is
not there create the directory.
