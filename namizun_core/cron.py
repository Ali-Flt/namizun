from namizun_menu import display
from namizun_menu.main_menu import menu as main_menu
import numpy as np
from crontab import CronTab

def cron_setter():
    display.banner()
    print(f"\n{display.cornsilk_color}Enter the number of minutes you want namizun to run per hour (muss be <= 30).\n")
    selection = int(input("\nNumber of minutes per hour?"))
    
    if 0 < selection <= 30:
        cron = CronTab(user=True)
        start_mins = np.linspace(0, 58, selection, dtype=int)
        stop_mins = start_mins + 1
        for start, end in zip(start_mins, stop_mins):
            job = cron.new(command='systemctl start namizun.service')
            job.setall(f'{start} * * * *')
            job = cron.new(command='systemctl stop namizun.service')
            job.setall(f'{end} * * * *')
        cron.write()
        return main_menu()
    else:
    	return cron_setter()


def cron_remover():
    cron = CronTab(user=True)
    iter = cron.find_command('namizun')
    for job in iter:
        cron.remove(job)
    cron.write()