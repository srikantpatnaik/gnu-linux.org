var tld_=new Array();tld_[0]="com";tld_[1]="org";tld_[2]="net";tld_[3]="ws";tld_[4]="info";tld_[10]="co.uk";tld_[11]="org.uk";tld_[12]="gov.uk";tld_[13]="ac.uk";var topDom_=13;var m_="mailto:";var a_="@";var d_=".";function mail(b,f,a,d){var c=e(b,f,a);document.write('<a href="'+m_+c+d+'">'+c+"</a>")}function mail2(b,f,a,d,c){document.write('<a href="'+m_+e(b,f,a)+d+'">'+c+"</a>")}function e(b,d,a){var c=b+a_;if(a!=-2){c+=d;if(a>=0){c+=d_+tld_[a]}}else{c+=swapper(d)}return c}function swapper(c){var b="";for(var a=0;a<c.length;a+=2){if(a+1==c.length){b+=c.charAt(a)}else{b+=c.charAt(a+1)+c.charAt(a)}}return b.replace(/\?/g,".")};