Authentication for Nginx server
###############################
:date: 2012-10-03 15:35
:author: camitr
:category: blogs
:slug: authentication-for-nginx-server

| Nginx is open source web and reverse proxy server.In this blog we will
learn how to create authentication on Nginx server to access the web
site running on nginx server.
|  I have create a scenario to apply the authentication. lets the domain
name of website is www.gnu-org, and its running by Nginx web server.
Document root for the site is in /var/www/html/gnu-linux and the
configuration of the nginx for the gnu-linux is in /etc/nginx/nginx.conf

| **Document root** is the directory where you keep the website file for
the domain,
|  Now to make authentication to access the site, we will follow these
steps.

| **Step 1.** Create the password file
|  Use apache's htpasswd to create the password file.If it is not found
install it.
|  # yum install httpd-tools
|  # htpasswd -c /var/www/html/gnu-linux/.htpasswd user1

| It will ask to create a password, type your password.
|  htpasswd takes two parameter first the location of htpasswd file in
documented root and second parameter is the user name.

| **Step 2.** Configure Nginx file
|  # vim /etc/nginx/nginx.conf

Now in this edit these two lines to the location where you want the
authentication.

**auth\_basic "Restricted";
 auth\_basic\_user\_file /var/www/gnu-linux/.htpasswd ;**

**server {
 listen 80;
 server\_name www.gnu-linux.org ;**

| access\_log /var/log/nginx/gnu-linux.org.access.log;
|  [......]
|  gnu-landing page
|  /location {
|  root /var/www/html/gnu-linux;

| auth\_basic "Restricted";
|  auth\_basic\_user\_file /var/www/html/gnu-linux/.htpasswd ;
|  index index.html index.htm;
|  expires 1m;
|  }

save the file and restart your nginx server.

# service nginx restart

Step 3. Open the web browser and type your url.

You will find a authentication window.

So its just very simple to create a Authentication for the Nginx
