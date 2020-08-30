# Setup Instructions

setup of Apache2 on Ubuntu 18.04 and Enabling CGI (comman gateway interface) for handling execution of scripts on server and generate their responce using web app.

---

## Apache2 Setup

Open terminal and type

```bash
$ sudo apt-get update
```

1. Install Apache

```bash
$ sudo apt install apache2
```

2. verify apache installation

visit `http://localhost/` or `http://127.0.0.1/` or `http://<YOUR_SERVER_IP>` and you can see now a apache 2 page.

3. Config Firewall

```bash
$ sudo ufw show app list

$ sudo ufw allow 'Apache'

$ sudo ufw status
```

4. Useful apache2 commands

```bash
$ sudo systemctl start|stop|restart|reload apache2
```

5. Apache Configuration Files, Directories and Modules

- Root Dir - `/var/www/html`
- Config - `/etc/apache2/apache2.conf`
- Apache2 - `/etc/apache2/`

6. Enable modules

```bash
$ sudo a2enmod name_of_module
```

---

## Running CGI Scripts on Apache2 / Setup CGI for Apache2

just need to make changes on two configuration files, them being

1. `/etc/apache2/apache2.conf`
2. `/etc/apache2/conf-available/serve-cgi-bin.conf`

- On the terminal

```bash
# create cgi-bin dir under /var/www
$ mkdir /var/www/cgi-bin

# Edit /etc/apache2/apache2.conf
$ sudo vim /etc/apache2/apache2.conf
```

And add the following at the end

```apache
###################################################################
#########     Adding capaility to run CGI-scripts #################
ServerName localhost
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
Options +ExecCGI
AddHandler cgi-script .cgi .pl .py
```

This converts the cgi-bin address to the specified address and the AddHandler tells the server to treat all files with `.cgi`, `.pl` and `.py` extensions as cgi scripts.

- Now for the second conf file

```bash
$ sudo vim /etc/apache2/conf-available/serve-cgi-bin.conf
```

The final file should look something like this

```apache
<IfModule mod_alias.c>
	<IfModule mod_cgi.c>
		Define ENABLE_USR_LIB_CGI_BIN
	</IfModule>

	<IfModule mod_cgid.c>
		Define ENABLE_USR_LIB_CGI_BIN
	</IfModule>

	<IfDefine ENABLE_USR_LIB_CGI_BIN>
		#ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
		#<Directory "/usr/lib/cgi-bin">
		#	AllowOverride None
		#	Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
		#	Require all granted
		#</Directory>

		## cgi-bin config
		ScriptAlias /cgi-bin/ /var/www/cgi-bin/
	    <Directory "/var/www/cgi-bin/">
	        AllowOverride None
	        Options +ExecCGI
	    </Directory>

	</IfDefine>
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

- Enable `cgi` module

```bash
$ sudo a2enmod cgi
```

- Now restart the `apache2`

```bash
$ sudo systemctl restart apache2
```

### Creating a simple CGI script

```bash
$ cd /var/www/cgi-bin
$ touch hello.py
$ nano hello.py
```

Add the following to `hello.py`

```python
#!/usr/bin/python

print("Content-Type: text/html;charset=utf-8\n")

print("Hello World")
```

make it executable for you and others

```bash
$ chmod o+x hello.py
```

### Run the Script:

Open your browser and enter the following link

`http://localhost/cgi-bin/hello.py`

And the script should run just fine.
