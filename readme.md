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

## New Features:

1. Added the ability to select the network interface.
2. Added the ability to set cron rules for namizun for it to run a specific number of minutes per hour throughtout the day.
