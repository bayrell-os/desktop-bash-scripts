# Scripts

Install script
```
cd /opt
sudo git clone https://github.com/bayrell-os/desktop_bash_scripts ./scripts
apt-get install python3-pynput libnotify-bin kde-spectacle scrot
```

Add script to sudoers
```
echo "$USER ALL = NOPASSWD: /opt/scripts/brightness.sh" >> /etc/sudoers
```
