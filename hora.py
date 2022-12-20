from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%d-%m-%Y'))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.day)
    print(data_atual.year)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    #data_string = '01/01/2019 12:20:2022'
    #data_convertida = datetime.strptime(data_string, '%d/ %m/ %Y %H:%m:%S')
    #print(data_convertida)
    #nova_data = data_atual -timedelta(days=365, hours=2)
    #print(nova_data)


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()