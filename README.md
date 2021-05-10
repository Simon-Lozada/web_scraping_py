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

Finally, in the TOR configuration file found in / etc / tor / torrc, we update the port, the password (hash) and enable the authentication of cookies. For this we open with vim (you can open it with other editors: vi, nano, gedit, etc.).

the file for editing as follows:`sudo vim /etc/tor/torrc`

In the file we have to uncomment and modify the following:

ControlPort 9051

#hashed password below is obtained via `tor --hash-password my_password`

HashedControlPassword 16:9529EB03A306DE6F60171DE514EA2FCD49235BAF1E1E55897209679683 (the hash generated by the password has been this)

CookieAuthentication 1

We do a TOR restart to apply the changes as follows:`sudo /etc/init.d/tor restart`

It may be the case that there are problems or conflicts when enabling ControlPort. In that case, it should be enabled as follows, putting the '&' at the end to make it run in the background:`tor --controlport 9051 &`

That would be all the Tor browser settings.

TOR by itself is not an http proxy, so to gain access to the TOR network, you must use Privoxy as an http proxy through socks5. We install Privoxy as follows:`sudo apt-get install privoxy`

We have to tell Privoxy to use TOR to carry all traffic through the SOCKS server on local port 9050. To do this, we open the configuration file with vim as follows:
`sudo vim /etc/privoxy/config`

We activate forward-socks5 uncommenting the following line:
`forward-socks5 / 127.0.0.1:9050`

Hacemos un Restart de Privoxy para aplicar los cambios de la siguiente manera:
`sudo /etc/init.d/privoxy restart`

ok that's all, I must especially thank jarroba for creating a tutorial in Spanish on this same topic, the tutorial link is:
https://jarroba.com/scraping-anonimo-la-red-tor/
