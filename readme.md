# NAMIZUN

This is a fork of [namizun](https://github.com/malkemit/namizun) with a couple of features added.

## One line installation command:

```bash
sudo curl https://raw.githubusercontent.com/Ali-Flt/namizun/master/else/setup.sh | sudo bash
```

## Command to uninstall:
```bash
sudo systemctl stop namizun.service
rm -r /var/www/namizun/
rm /etc/systemd/system/namizun.service
rm /usr/local/bin/namizun
sudo systemctl daemon-reload
```