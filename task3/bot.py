# import csv
# import json
# import os.path
# import model


# cd_file_name = ''
# cd = []
# global_id = 0  # id для добавления пользователей


# def init_data_base(file_name='company_directory.csv'):
#     global global_id
#     global cd
#     global cd_file_name
#     cd_file_name = file_name
#     cd.clear()
#     if os.path.exists(cd_file_name):
#         with open(cd_file_name, 'r', encoding='utf-8', newline='') as csv_file:
#             reader = csv.reader(csv_file)
#             for row in reader:
#                 if(row[0] != 'ID'):
#                     cd.append(row)
#                     if(int(row[0]) > global_id):
#                         global_id = int(row[0])
#     else:
#         open(cd_file_name, 'w', newline='').close()


# def create(id='', name='', surname='', job='', phone_number='', salary=''):    
#     global global_id
#     global cd
#     global cd_file_name
#     if(id == ''):
#         print("ALARM NO ID SPECIFIED!!!!!1111")
#         return
#     if(name == ''):
#         print("ALARM NO NAME SPECIFIED!!!!!1111")
#         return
#     if(surname == ''):
#         print("ALARM NO SURNAME SPECIFIED!!!!!1111")
#         return
#     if(job == ''):
#         print("ALARM NO JOB SPECIFIED!!!!!1111")
#         return
#     if(phone_number == ''):
#         print("ALARM NO TELEPHONE NUMBER SPECIFIED!!!!!1111")
#         return
#     if(salary == ''):
#         print("ALARM NO SALARY SPECIFIED!!!!!1111")
#         return

#     for row in cd:
#         if(row[0] == id and row[2] == name.title() and row[1] == surname.title() and row[3] == job.title() and row[4] == phone_number and row[4] == salary):
#             print("already exist")
#             return

#     global_id += 1
#     new_row = [str(global_id), name.title(),
#                surname.title(), job.title(), phone_number, salary]
#     cd.append(new_row)
#     with open(cd_file_name, 'a', encoding='utf-8', newline='') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',',
#                             quotechar='\'', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(new_row)


# # поиск (если нужно выгрузить все: result = retrive())
# def retrive(id='', name='', surname='', job='', phone_number='', salary=''):
#     global global_id
#     global cd
#     global cd_file_name
#     result = []
#     for row in cd:
#         if (id != '' and row[0] != id):
#             continue
#         if(surname != '' and row[1] != surname.title()):
#             continue
#         if(name != '' and row[2] != name.title()):
#             continue
#         if(job != '' and row[3] != job.title()):
#             continue
#         if(phone_number != '' and row[4] != phone_number):
#             continue
#         if(salary != '' and row[5] != salary):
#             continue
#         result.append(row)
#     if len(result) == 0:
#         return f'Контакты не найдены'
#     else:
#         # выход список списков (переделать в строку с разделителем)
#         return result


# def update(id='', new_name='', new_surname='', new_job='', new_phone_number='', new_salary=''):
#     global global_id
#     global cd
#     global cd_file_name
#     if(id == ''):
#         print('specify id for update')
#         return
#     with open(cd_file_name, 'w', encoding='utf-8', newline='') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',',
#                             quotechar='\'', quoting=csv.QUOTE_MINIMAL)
#         for row in cd:
#             if(row[0] == id):
#                 if(new_name != ''):
#                     row[1] = new_name.title()

#                 if(new_surname != ''):
#                     row[2] = new_surname.title()

#                 if(new_job != ''):
#                     row[3] = new_job.title()

#                 if(new_phone_number != ''):
#                     row[4] = new_phone_number

#                 if(new_salary != ''):
#                     row[5] = new_salary()

#             writer.writerow(row)


# def delete(id=''):
#     global global_id
#     global cd
#     global cd_file_name
#     if(id == ''):
#         print('specify id for delete')
#         return

#     for row in cd:
#         if (row[0] == id):
#             cd.remove(row)
#             break

#     with open(cd_file_name, 'w', encoding='utf-8', newline='') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',',
#                             quotechar='\'', quoting=csv.QUOTE_MINIMAL)
#         for row in cd:
#             writer.writerow(row)


# def get_token():
#     file = open('token.csv', 'r')
#     for i in file:
#         token = i
#     file.close()
#     return token


# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Updater, ConversationHandler
# # from _applicationbuilder import *
# from telegram_bot_commands import *
# # from User_Interface import user_choice
# from process import data_processor
# from import_data import input_people as write
# from export_data import read_file as exphum
# from export_data import read_file as expjob
# from export_data import read_file as expsal
# from change_data import change_elem as chel
# from delete_data import delete_people as delhum

# if __name__ == '__main__':
#         bot_token="5580146319:AAGSW35Ujibr_P-PDZNZXlxILQEVRN4RvGA" #Вносим свой токен
#         # # Создаем Updater и передаем ему токен вашего бота.
#         updater = Updater(bot_token, update_queue=True)
#         # # получаем диспетчера для регистрации обработчиков
#         dispatcher = updater.dispatcher
#         # точка входа в разговор
#         entry_points=[CommandHandler('start', start)],
#         app = ApplicationBuilder().token("5157594801:AAFHHasq8CBNBoT5y6V55vvkMYuawHJk4_8").build()
        
#         app.add_handler(CommandHandler("f1", help_command))             # Показать список команд
#         # app.add_handler(CommandHandler("1", id_command))              # 1 - вывод ID
#         app.add_handler(CommandHandler("1", input_command))             # 1 - вывод добавить сотрудника
#         app.add_handler(CommandHandler("2", exphum_command))            # 2 - вывод поиск сотрудника
#         app.add_handler(CommandHandler("3", expjob_command))            # 3 - вывод поиск сотрудника по должности
#         app.add_handler(CommandHandler("4", expsal_command))            # 4 - вывод поиск сотрудника по зарплате
#         app.add_handler(CommandHandler("5", chel_command))              # 5 - вывод изменить данные сотрудника
#         app.add_handler(CommandHandler("6", delhum_command))            # 6 - вывод удалить сотрудника
#         app.add_handler(CommandHandler("7", exit_command))              # 7 - выход


#         fallbacks=[CommandHandler('cancel', cancel)],

#         # Добавляем обработчик разговоров `conv_handler`
#         dispatcher.add_handler(conversation_handler)

# # Запуск бота
# updater.start_polling()
# updater.idle()



# # print('server start')


 
#         # # этапы разговора, каждый со своим списком обработчиков сообщений
#         # states={
#         #     CHOICE: [MessageHandler(Filters.text, choice)],
#         #     RATIONAL_ONE: [MessageHandler(Filters.text, rational_one)],
#         #     RATIONAL_TWO: [MessageHandler(Filters.text, rational_two)],
#         #     OPERATIONS_RATIONAL: [MessageHandler(Filters.text, operatons_rational)],
#         #     OPERATIONS_COMPLEX: [MessageHandler(Filters.text, operatons_complex)],
#         #     COMPLEX_ONE: [MessageHandler(Filters.text, complex_one)],
#         #     COMPLEX_TWO: [MessageHandler(Filters.text, complex_two)],
#         # },
#         # точка выхода из разговора


# #     app.run_polling()
# # stop_signals=None


import logging
import csv

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from config import TOKEN
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, WRITE_CVS, SEARCH, FIO, TEL = range(5)


# функция обратного вызова точки входа в разговор


def start(update, context):
    context.bot.send_sticker(update.effective_chat.id,'5580146319:AAGSW35Ujibr_P-PDZNZXlxILQEVRN4RvGA')
    update.message.reply_text(
        'Добро пожаловать в телефонную книгу.\n Выберите нужное действие:')
    update.message.reply_text(
        '1 - добавление записи в телефонную книгу \n'
        '2 - поиск записи в телефонной книге \n'
        '3 - просмотр телефонной книги \n'
        '4 - выход')
    return CHOICE


def choice(update, context):
    user_choice = update.message.text
    if user_choice == '1':
        update.message.reply_text(
            'Фамилия Имя:')
        return FIO
    if user_choice == '2':
        context.bot.send_message(
            update.effective_chat.id, 'Введите значение для поиска: ')
        return SEARCH
    if user_choice == '3':
        text = read_csv()
        context.bot.send_message(
            update.effective_chat.id, text)
        return start(update, context)
    if user_choice == '4':
        return cancel(update, context)

def fio(update, context):
    lst = []
   
    
    text =update.message.text
    lst.append(text)
    update.message.reply_text(
            'Номер телефона: ')
    with open ('company_directory.csv', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator=',')
        file_writer.writerow(lst)
     
    return TEL
   

def tel(update, context):
    lst = []
    while True:
      try:
       text =int (update.message.text)
       lst.append(text)
       update.message.reply_text(
             'Комментарий: ')
       with open ('company_directory.csv', mode = 'a', encoding='utf-8') as w_file:
         file_writer = csv.writer(w_file, delimiter=',', lineterminator=',')
         file_writer.writerow(lst)
       return WRITE_CVS
      except ValueError:
       context.bot.send_sticker(update.effective_chat.id,'5580146319:AAGSW35Ujibr_P-PDZNZXlxILQEVRN4RvGA')
       update.message.reply_text(
            'Неверный ввод номера , повторите ввод \n Номер телефона')
       break     


def write_cvs(update, context):
    '''
    Запись в csv фаил
    '''
    lst = []
    text = update.message.text
    lst.append(text)
    # update.message.reply_text(
    #         'Номер телефона: ')
    # text_1 = update.message.text
    # lst.append(text_1)
    # update.message.reply_text(
    #         'Комментарий: ')
    # text_2 = update.message.text
    # lst.append(text_2)
    with open ('company_directory', mode = 'a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
        file_writer.writerow(lst)
    return start(update, context)

def search(update, context):
    '''
    Поиск в телефонной книге
    '''
    text = update.message.text
    lst_input = read_csv()
    line_output = ''
    for line in lst_input:
        if text in line:
            line_output += line + '\n'
    update.message.reply_text(line_output)
    return start(update, context)

def read_csv():
    '''
    Чтение из файла csv
    '''
    with open('company_directory.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        contact =''
        for line in reader:
            contact += ' '.join(line)+'\n'
            #contact_list.append(line)
    return contact


    # with open('phone_book_bot.csv', encoding='utf-8') as r_file:
    #     file_reader_1 = csv.reader(r_file, delimiter=' ')
    #     file_reader = []
    #     for line in file_reader_1:
    #         line = ' '.join(line)
    #         file_reader.append(line)
    #     return file_reader

def cancel(update, context):
    context.bot.send_sticker(update.effective_chat.id,'5580146319:AAGSW35Ujibr_P-PDZNZXlxILQEVRN4RvGA')
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - заходи.',
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN, update_queue=True)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO
    conversation_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            WRITE_CVS: [MessageHandler(Filters.text, write_cvs)],
            SEARCH: [MessageHandler(Filters.text, search)],
            FIO: [MessageHandler(Filters.text, fio)],
            TEL: [MessageHandler(Filters.text, tel)],
            # COMPLEX_ONE: [MessageHandler(Filters.text, complex_one)],
            # COMPLEX_TWO: [MessageHandler(Filters.text, complex_two)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()