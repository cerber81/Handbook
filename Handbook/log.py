import datetime
def log_cash(mode):
    with open ('log.txt', 'a', encoding= 'utf-8') as file:
        file.write (f'{mode} дата и время: {str(datetime.datetime.now())} \n')
