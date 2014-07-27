#!/bin/bash                                                                     
                                                                                
website_output="/var/www/gnu-linux.org/"                                        

while true;
    do
	if [ $(git pull | wc -l) -gt 1 ];
            then                                                                
                make publish                                                    
                cp -r output/* $website_output                                  
        fi                                                                  
    sleep 10
    done
# Just for manual copy paste #lazy-me
# make publish && cp -r output/* /var/www/gnu-linux.org/
