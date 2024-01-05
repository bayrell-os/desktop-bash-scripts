# Scripts

Install script
```
cd /opt
sudo git clone https://github.com/bayrell-os/desktop_bash_scripts ./scripts
```

Add script to sudoers
```
echo "$USER ALL = NOPASSWD: /opt/scripts/brightness.sh" >> /etc/sudoers
```
