# web_scraping_py
This is a simple web scraping with python.

which contains two variants, one which uses the tor browser as a proxy server, in order to be as anonymous as possible.
And the other does not use tor, but has the advantage that it is faster.

Also, this project contains a script that Tor can use as a proxy (which you can use for other projects if you want). 
However, you have to do some basic settings in the Tor browser to use it.

you need:

-Activate the "ControlPort" so that TOR listens on port 9051, since this is the port on which TOR will listen to any communication from the applications that talk to the TOR controller.

-Create a new password hash that prevents random access to the port:

We create the hash of a new password as follows:
`tor --hash-password my_password`

-Implement cookie authentication:

Finally, in the TOR configuration file found in / etc / tor / torrc, we update the port, the password (hash) and enable the authentication of cookies. For this we open with vim (you can open it with other editors: vi, nano, gedit, etc.) the file for editing as follows:
`sudo vim /etc/tor/torrc`

In the file we have to uncomment and modify the following:

ControlPort 9051
hashed password below is obtained via `tor --hash-password my_password`
HashedControlPassword 16:9529EB03A306DE6F60171DE514EA2FCD49235BAF1E1E55897209679683(the hash generated has been this)
CookieAuthentication 1
