import telebot
from telebot import types

#Ссылка на бота
#http://dip-psi.ru/psikhologicheskiye-testy/post/metodika-ocenki-karernyh-orientacij-e-shejna-yakorya-karery-adaptaciya-v-a-chiker-i-v-e-vinourova

#Имя клиента
name = ''

#Список ответов клиента на тест1
answers_test1 = [0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,
                 0]
#Список результатов клиента на тест1
results_test1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

#Link
#http://t.me/hr_prof_bot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Добро пожаловать! *** - сервис карьерного консультирования.\n"
                         "Введите /test для прохождения тестирования.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Привет!')
    elif message.text == "/test":
        bot.send_message(message.from_user.id, "Давайте познакомимся! Как Вас зовут?")
        bot.register_next_step_handler(message, reg_name)
    else:
        bot.reply_to(message, "Я не понял Вашу команду")

def reg_name(message):
    global name
    name = message.text
    keyboard =types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, name + ", желаете пройти тестирование оценки карьерных ориентаций "
                                                  "Э.Шейна «Якоря карьеры»?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Отлично! Тест содержит 41 вопрос. "
                                               "В каждом вопросе оцените, насколько важным является для вас каждое из "
                                               "следующих утверждений, поставив оценку от 1 до 10. "
                                               "\nГде 1 - совершенно неважно(совершенно не согласен), "
                                               "\n10 - исключительно важно(полностью согласен)\n")
        bot.send_message(call.message.chat.id,"Вопрос №1: насколько важным является для вас cтроить свою карьеру в"
                                              "пределах конкретной научной или технической сферы?")
        bot.register_next_step_handler(call.message, question1)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Можете посетить наш сайт: ***")

def question1(message):
    global answers_test1
    try:
        answers_test1[0] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №2: насколько важным является для вас осуществлять "
                                                         "наблюдение и контроль над людьми, влиять на них на всех уровнях?")
        bot.register_next_step_handler(message, question2)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №1: насколько важным является для вас cтроить свою карьеру в"
                                              "пределах конкретной научной или технической сферы?")
        bot.register_next_step_handler(message, question1)


def question2(message):
    global answers_test1
    try:
        answers_test1[1] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №3: насколько важным является для вас "
                                                         "иметь возможность делать все по-своему и не быть "
                                                         "стесненным правилами какой-либо организации?")
        bot.register_next_step_handler(message, question3)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №2: насколько важным является для вас осуществлять "
                                                         "наблюдение и контроль над людьми, влиять на них на всех уровнях?")
        bot.register_next_step_handler(message, question2)

def question3(message):
    global answers_test1
    try:
        answers_test1[2] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №4: насколько важным является для вас иметь постоянное "
                                           "место работы с гарантированным окладом и социальной защищенностью?")
        bot.register_next_step_handler(message, question4)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №3: насколько важным является для вас иметь возможность делать "
                                               "все по-своему и не быть стесненным правилами какой-либо организации?")
        bot.register_next_step_handler(message, question3)

def question4(message):
    global answers_test1
    try:
        answers_test1[3] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №5: насколько важным является для вас употреблять свое "
                                           "умение общаться на пользу людям, помогать другим?")
        bot.register_next_step_handler(message, question5)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №4: насколько важным является для вас иметь постоянное "
                                           "место работы с гарантированным окладом и социальной защищенностью?")
        bot.register_next_step_handler(message, question4)

def question5(message):
    global answers_test1
    try:
        answers_test1[4] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №6: насколько важным является для вас "
                                                "работать с проблемами, которые представляются почти неразрешимыми?")
        bot.register_next_step_handler(message, question6)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №5: насколько важным является для вас употреблять свое "
                                           "умение общаться на пользу людям, помогать другим?")
        bot.register_next_step_handler(message, question5)

def question6(message):
    global answers_test1
    try:
        answers_test1[5] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №7: насколько важным является для вас "
                                                         "вести такой образ жизни, чтобы интересы семьи и карьеры "
                                           "были уравновешены?")
        bot.register_next_step_handler(message, question7)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №6: насколько важным является для вас "
                                                "работать с проблемами, которые представляются почти неразрешимыми?")
        bot.register_next_step_handler(message, question6)

def question7(message):
    global answers_test1
    try:
        answers_test1[6] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №8: насколько важным является для вас создать и построить нечто, "
                                               "что будет всецело моим произведением или идеей?")
        bot.register_next_step_handler(message, question8)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №7: насколько важным является для вас "
                                        "вести такой образ жизни, чтобы интересы семьи и карьеры были уравновешены?")
        bot.register_next_step_handler(message, question7)

def question8(message):
    global answers_test1
    try:
        answers_test1[7] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №9: насколько важным является для вас продолжать работу по своей "
                            "специальности, чем получить более высокую должность, не связанную с моей специальностью?")
        bot.register_next_step_handler(message, question9)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №8: насколько важным является для вас создать и построить нечто, "
                                               "что будет всецело моим произведением или идеей?")
        bot.register_next_step_handler(message, question8)

def question9(message):
    global answers_test1
    try:
        answers_test1[8] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №10: насколько важным является для вас "
                                                         "быть первым руководителем в организации?")
        bot.register_next_step_handler(message, question10)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №9: насколько важным является для вас продолжать работу по своей "
                            "специальности, чем получить более высокую должность, не связанную с моей специальностью?")
        bot.register_next_step_handler(message, question9)

def question10(message):
    global answers_test1
    try:
        answers_test1[9] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №11: насколько важным является для вас иметь работу, не "
                                               "связанную с режимом или  другими организационными ограничениями?")
        bot.register_next_step_handler(message, question11)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №10: насколько важным является для вас "
                                                         "быть первым руководителем в организации?")
        bot.register_next_step_handler(message, question10)

def question11(message):
    global answers_test1
    try:
        answers_test1[10] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №12: насколько важным является для вас работать в организации, "
                                               "которая обеспечит мне стабильность на длительный период времени?")
        bot.register_next_step_handler(message, question12)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №11: насколько важным является для вас иметь работу, не "
                                               "связанную с режимом или  другими организационными ограничениями?")
        bot.register_next_step_handler(message, question11)

def question12(message):
    global answers_test1
    try:
        answers_test1[11] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №13: насколько важным является для вас "
                                                "употребить свои умения и способности на то, чтобы сделать мир лучше?")
        bot.register_next_step_handler(message, question13)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №12: насколько важным является для вас работать в организации, "
                                               "которая обеспечит мне стабильность на длительный период времени?")
        bot.register_next_step_handler(message, question12)

def question13(message):
    global answers_test1
    try:
        answers_test1[12] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №14: насколько важным является для вас "
                                                         "соревноваться с другими и побеждать?")
        bot.register_next_step_handler(message, question14)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №13: насколько важным является для вас "
                                                "употребить свои умения и способности на то, чтобы сделать мир лучше?")
        bot.register_next_step_handler(message, question13)

def question14(message):
    global answers_test1
    try:
        answers_test1[13] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №15: насколько важным является для вас строить карьеру, которая "
                                               "позволит мне не изменять своему образу жизни?")
        bot.register_next_step_handler(message, question15)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №14: насколько важным является для вас "
                                                         "соревноваться с другими и побеждать?")
        bot.register_next_step_handler(message, question14)

def question15(message):
    global answers_test1
    try:
        answers_test1[14] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №16: насколько важным является для вас "
                                                         "создать новое коммерческое предприятие?")
        bot.register_next_step_handler(message, question16)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №15: насколько важным является для вас строить карьеру, которая "
                                               "позволит мне не изменять своему образу жизни?")
        bot.register_next_step_handler(message, question15)

def question16(message):
    global answers_test1
    try:
        answers_test1[15] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №17: насколько важным является для вас "
                                                         "посвятить свою жизнь избранной профессии?")
        bot.register_next_step_handler(message, question17)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №16: насколько важным является для вас "
                                                         "создать новое коммерческое предприятие?")
        bot.register_next_step_handler(message, question16)

def question17(message):
    global answers_test1
    try:
        answers_test1[16] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №18: насколько важным является для вас "
                                                         "занять высокую руководящую должность?")
        bot.register_next_step_handler(message, question18)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №17: насколько важным является для вас "
                                                         "посвятить свою жизнь избранной профессии?")
        bot.register_next_step_handler(message, question17)

def question18(message):
    global answers_test1
    try:
        answers_test1[17] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №19: насколько важным является для вас иметь работу, которая "
                    "предоставляет максимум свободы и автономии в выборе характера занятий, времени выполнения и т.д.?")
        bot.register_next_step_handler(message, question19)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №18: насколько важным является для вас "
                                                         "занять высокую руководящую должность?")
        bot.register_next_step_handler(message, question18)

def question19(message):
    global answers_test1
    try:
        answers_test1[18] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №20: насколько важным является для вас "
                                            "оставаться на одном месте жительства, чем переехать в связи с повышением?")
        bot.register_next_step_handler(message, question20)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №19: насколько важным является для вас иметь работу, которая "
                    "предоставляет максимум свободы и автономии в выборе характера занятий, времени выполнения и т.д.?")
        bot.register_next_step_handler(message, question19)

def question20(message):
    global answers_test1
    try:
        answers_test1[19] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №21: насколько важным является для вас иметь возможность "
                                               "использовать свои умения и талант для служения важной цели?")
        bot.register_next_step_handler(message, question21)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №20: насколько важным является для вас "
                                            "оставаться на одном месте жительства, чем переехать в связи с повышением?")
        bot.register_next_step_handler(message, question20)

def question21(message):
    global answers_test1
    try:
        answers_test1[20] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №22: насколько вы согласны с утверждением, что единственная "
        "действительная цель моей карьеры — находить и решать трудные проблемы, независимо от того, в какой области "
                                               "они возникли?")
        bot.register_next_step_handler(message, question22)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №21: насколько важным является для вас иметь возможность "
                                               "использовать свои умения и талант для служения важной цели?")
        bot.register_next_step_handler(message, question21)

def question22(message):
    global answers_test1
    try:
        answers_test1[21] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №23: насколько вы согласны с утверждением, что я всегда стремлюсь"
                                               " уделять одинаковое внимание моей семье и моей карьере?")
        bot.register_next_step_handler(message, question23)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №22: насколько вы согласны с утверждением, что единственная "
        "действительная цель моей карьеры — находить и решать трудные проблемы, независимо от того, в какой области "
                                               "они возникли?")
        bot.register_next_step_handler(message, question22)

def question23(message):
    global answers_test1
    try:
        answers_test1[22] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №24: насколько вы согласны с утверждением, что я всегда нахожусь"
                                " в поиске идей, которые дадут мне возможность начать и построить собственное дело?")
        bot.register_next_step_handler(message, question24)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №23: насколько вы согласны с утверждением, что я всегда стремлюсь"
                                               " уделять одинаковое внимание моей семье и моей карьере?")
        bot.register_next_step_handler(message, question23)

def question24(message):
    global answers_test1
    try:
        answers_test1[23] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №25: насколько вы согласны с утверждением, что я соглашусь на"
            " руководящую должность только в том случае, если она находится в сфере моей профессиональной компетенции?")
        bot.register_next_step_handler(message, question25)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №24: насколько вы согласны с утверждением, что я всегда нахожусь"
                                " в поиске идей, которые дадут мне возможность начать и построить собственное дело?")
        bot.register_next_step_handler(message, question24)

def question25(message):
    global answers_test1
    try:
        answers_test1[24] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №26: насколько вы согласны с утверждением, что я хотел бы достичь"
        " такого положения в организации, которое давало бы возможность наблюдать за работой других и интегрировать их "
                                           "деятельность?")
        bot.register_next_step_handler(message, question26)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №25: насколько вы согласны с утверждением, что я соглашусь на"
            " руководящую должность только в том случае, если она находится в сфере моей профессиональной компетенции?")
        bot.register_next_step_handler(message, question25)

def question26(message):
    global answers_test1
    try:
        answers_test1[25] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №27: насколько вы согласны с утверждением, что в моей "
                                    "профессиональной деятельности я более всего забочусь о своей свободе и автономии?")
        bot.register_next_step_handler(message, question27)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №26: насколько вы согласны с утверждением, что я хотел бы достичь"
        " такого положения в организации, которое давало бы возможность наблюдать за работой других и интегрировать их "
                                           "деятельность?")
        bot.register_next_step_handler(message, question26)

def question27(message):
    global answers_test1
    try:
        answers_test1[26] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №28: насколько вы согласны с утверждением, что для меня важнее "
                "остаться на нынешнем месте жительства, чем получить повышение или новую работу в другой местности?")
        bot.register_next_step_handler(message, question28)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №27: насколько вы согласны с утверждением, что в моей "
                                    "профессиональной деятельности я более всего забочусь о своей свободе и автономии?")
        bot.register_next_step_handler(message, question27)

def question28(message):
    global answers_test1
    try:
        answers_test1[27] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №29: насколько вы согласны с утверждением, что я всегда искал "
                                               "работу, на которой мог бы приносить пользу другим?")
        bot.register_next_step_handler(message, question29)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №28: насколько вы согласны с утверждением, что для меня важнее "
                "остаться на нынешнем месте жительства, чем получить повышение или новую работу в другой местности?")
        bot.register_next_step_handler(message, question28)

def question29(message):
    global answers_test1
    try:
        answers_test1[28] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №30: насколько вы согласны с утверждением, что соревнование и "
                                               "выигрыш — это наиболее важные и волнующие стороны моей карьеры?")
        bot.register_next_step_handler(message, question30)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №29: насколько вы согласны с утверждением, что я всегда искал "
                                               "работу, на которой мог бы приносить пользу другим?")
        bot.register_next_step_handler(message, question29)

def question30(message):
    global answers_test1
    try:
        answers_test1[29] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №31: насколько вы согласны с утверждением, что карьера имеет "
                                    "смысл только в том случае, если она позволяет вести жизнь, которая мне нравится?")
        bot.register_next_step_handler(message, question31)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №30: насколько вы согласны с утверждением, что соревнование и "
                                               "выигрыш — это наиболее важные и волнующие стороны моей карьеры?")
        bot.register_next_step_handler(message, question30)

def question31(message):
    global answers_test1
    try:
        answers_test1[30] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №32: насколько вы согласны с утверждением, что "
                                        "предпринимательская деятельность составляет центральную часть моей карьеры?")
        bot.register_next_step_handler(message, question32)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №31: насколько вы согласны с утверждением, что карьера имеет "
                                    "смысл только в том случае, если она позволяет вести жизнь, которая мне нравится?")
        bot.register_next_step_handler(message, question31)

def question32(message):
    global answers_test1
    try:
        answers_test1[31] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №33: насколько вы согласны с утверждением, что я бы скорее ушел "
                                        "из организации, чем стал заниматься работой, не связанной с моей профессией?")
        bot.register_next_step_handler(message, question33)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №32: насколько вы согласны с утверждением, что "
                                        "предпринимательская деятельность составляет центральную часть моей карьеры?")
        bot.register_next_step_handler(message, question32)

def question33(message):
    global answers_test1
    try:
        answers_test1[32] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №34: насколько вы согласны с утверждением, что я буду считать, "
        "что достиг успеха в карьере только тогда, когда стану руководителем высокого уровня в солидной организации?")
        bot.register_next_step_handler(message, question34)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №33: насколько вы согласны с утверждением, что я бы скорее ушел "
                                        "из организации, чем стал заниматься работой, не связанной с моей профессией?")
        bot.register_next_step_handler(message, question33)

def question34(message):
    global answers_test1
    try:
        answers_test1[33] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №35: насколько вы согласны с утверждением, что я не хочу, чтобы "
                                               "меня стесняла какая-нибудь организация или мир бизнеса?")
        bot.register_next_step_handler(message, question35)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №34: насколько вы согласны с утверждением, что я буду считать, "
        "что достиг успеха в карьере только тогда, когда стану руководителем высокого уровня в солидной организации?")
        bot.register_next_step_handler(message, question34)

def question35(message):
    global answers_test1
    try:
        answers_test1[34] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №36: насколько вы согласны с утверждением, что я предпочел бы "
                                               "работать в организации, которая обеспечивает длительный контракт?")
        bot.register_next_step_handler(message, question36)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №35: насколько вы согласны с утверждением, что я не хочу, чтобы "
                                               "меня стесняла какая-нибудь организация или мир бизнеса?")
        bot.register_next_step_handler(message, question35)

def question36(message):
    global answers_test1
    try:
        answers_test1[35] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №37: насколько вы согласны с утверждением, что я бы хотел "
                                               "посвятить свою карьеру достижению важной и полезной цели?")
        bot.register_next_step_handler(message, question37)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №36: насколько вы согласны с утверждением, что я предпочел бы "
                                               "работать в организации, которая обеспечивает длительный контракт?")
        bot.register_next_step_handler(message, question36)

def question37(message):
    global answers_test1
    try:
        answers_test1[36] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №38: насколько вы согласны с утверждением, что я чувствую себя "
        "преуспевающим только тогда, когда я постоянно вовлечен в решение трудных проблем или в ситуации соревнования?")
        bot.register_next_step_handler(message, question38)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №37: насколько вы согласны с утверждением, что я бы хотел "
                                               "посвятить свою карьеру достижению важной и полезной цели?")
        bot.register_next_step_handler(message, question37)

def question38(message):
    global answers_test1
    try:
        answers_test1[37] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №39: насколько вы согласны с утверждением, что выбрать и "
                                    "поддерживать определенный образ жизни важнее, чем добиваться успеха в карьере?")
        bot.register_next_step_handler(message, question39)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №38: насколько вы согласны с утверждением, что я чувствую себя "
        "преуспевающим только тогда, когда я постоянно вовлечен в решение трудных проблем или в ситуации соревнования?")
        bot.register_next_step_handler(message, question38)

def question39(message):
    global answers_test1
    try:
        answers_test1[38] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №40: насколько вы согласны с утверждением, что "
                                                         "я всегда хотел основать и построить свой собственный бизнес?")
        bot.register_next_step_handler(message, question40)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №39: насколько вы согласны с утверждением, что выбрать и "
                                    "поддерживать определенный образ жизни важнее, чем добиваться успеха в карьере?")
        bot.register_next_step_handler(message, question39)

def question40(message):
    global answers_test1
    try:
        answers_test1[39] = int(message.text)
        bot.send_message(message.from_user.id, "Вопрос №41: насколько вы согласны с утверждением, что "
                                                         "я предпочитаю работу, которая не связана с командировками?")
        bot.register_next_step_handler(message, question41)
    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №40: насколько вы согласны с утверждением, что "
                                                         "я всегда хотел основать и построить свой собственный бизнес?")
        bot.register_next_step_handler(message, question40)

def question41(message):
    global answers_test1
    global results_test1

    try:
        answers_test1[40] = int(message.text)
        bot.send_message(message.from_user.id, name + ", " + "тест завершен. Ответы записаны.")

        # Обработка результатов теста
        results_test1[0] = (answers_test1[0] + answers_test1[8] + answers_test1[16] + answers_test1[24] + answers_test1[32]) / 5
        results_test1[1] = (answers_test1[1] + answers_test1[9] + answers_test1[17] + answers_test1[25] + answers_test1[33]) / 5
        results_test1[2] = (answers_test1[2] + answers_test1[10] + answers_test1[18] + answers_test1[26] + answers_test1[34]) / 5
        results_test1[3] = (answers_test1[3] + answers_test1[11] + answers_test1[35]) / 3
        results_test1[4] = (answers_test1[19] + answers_test1[27] + answers_test1[40]) / 3
        results_test1[5] = (answers_test1[4] + answers_test1[12] + answers_test1[20] + answers_test1[28] + answers_test1[36]) / 5
        results_test1[6] = (answers_test1[5] + answers_test1[13] + answers_test1[21] + answers_test1[29] + answers_test1[37]) / 5
        results_test1[7] = (answers_test1[6] + answers_test1[14] + answers_test1[22] + answers_test1[30] + answers_test1[38]) / 5
        results_test1[8] = (answers_test1[7] + answers_test1[15] + answers_test1[23] + answers_test1[31] + answers_test1[39]) / 5

        bot.send_message(message.from_user.id, "Карьерная ориентация считается ярко выраженной, если показатель "
                                           "превышает 6 баллов.\n"
                                           "\nВаши результаты: "
                                           "\nПроф. компетентность: " + str(round(results_test1[0], 1)) +
                                           "\nМенеджмент: " + str(round(results_test1[1], 1)) +
                                           "\nАвтономия (независимость): " + str(round(results_test1[2], 1)) +
                                           "\nСтабильность работы: " + str(round(results_test1[3], 1)) +
                                           "\nСтабильность места жительства: " + str(round(results_test1[4], 1)) +
                                           "\nСлужение: " + str(round(results_test1[5], 1)) +
                                           "\nВызов: " + str(round(results_test1[6], 1)) +
                                           "\nИнтеграция стилей жизни: " + str(round(results_test1[7], 1)) +
                                           "\nПредпринимательство: " + str(round(results_test1[8], 1)) + "\n"
                                           "\nВы можете записаться на карьерную консультацию по ссылке: *ссылка*")

    except Exception:
        bot.send_message(message.from_user.id, "Для ответа введите число от 1 до 10 включительно!")
        bot.send_message(message.from_user.id, "Вопрос №41: насколько вы согласны с утверждением, что "
                                                         "я предпочитаю работу, которая не связана с командировками?")
        bot.register_next_step_handler(message, question41)

bot.polling()
