import telebot
user_info={
    "fname":[],
    "sname":[],
    "phonenum":[]
}
check = None
bot=telebot.TeleBot("YOUR TOKEN")
@bot.message_handler(commands=["start"])
def greeting(message):
    bot.send_message(message.from_user.id,"Hello, welcome to the pizza delivery\nHow can we help you?")
    markup=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    orderpizza=telebot.types.KeyboardButton("Order a Pizza")
    markup.add(orderpizza)
    bot.send_message(message.from_user.id,"Choose Please :",reply_markup=markup)
@bot.message_handler(content_types=["text"])
def usr_info(message):
    global fn
    global sn
    global check
    global phone
    sn=None
    if message.text=="Order a Pizza":
        bot.reply_to(message,"Please enter your first name :") #Checking user info
    else:
        for i in range(len(user_info["fname"])):
            if(user_info["fname"][i]==message.text):
                fn=user_info["fname"][i]
                sn=user_info["sname"][i]
                phone=user_info["phonenum"][i]
                markup=telebot.types.InlineKeyboardMarkup()
                markup.row_width = 2
                edit_user_info=telebot.types.InlineKeyboardButton("Edit",callback_data="edit")
                order=telebot.types.InlineKeyboardButton("Order",callback_data="order")
                markup.add(edit_user_info)
                bot.send_message(message.from_user.id,f"First name : {user_info['fname'][i]}\nLast name : {user_info['sname'][i]}\nPhone Number : {user_info['phonenum'][i]}",reply_markup=markup)
                break
        else:
            if(message.text=="Yes"):
                user_info["fname"].append(fn)
                check="passed_yes"
                bot.send_message(message.from_user.id,"Please enter your surname : ")
            elif(message.text=="No"):
                bot.send_message(message.from_user.id,"Registration Terminated\nYou cannot order without an account!!!")
            else:
                if(check==None):
                    fn=message.text
                    markup=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
                    yes=telebot.types.KeyboardButton("Yes")
                    no=telebot.types.KeyboardButton("No")
                    markup.add(yes,no)
                    bot.reply_to(message,"Oops, looks like this user hasn't been registered\nDo you wannna get registerd?: ",reply_markup=markup)
                elif(message.text[0]=='+' and check=="passed_sn"):
                    if(message.text[1:4]=='998'):
                        user_info["phonenum"].append(message.text)
                        markup=telebot.types.InlineKeyboardMarkup()
                        markup.row_width = 2
                        edit_user_info=telebot.types.InlineKeyboardButton("Edit",callback_data="edit")
                        markup.add(edit_user_info)
                        bot.send_message(message.from_user.id,f"First name : {user_info['fname'][-1]}\nLast name : {user_info['sname'][-1]}\nPhone Number : {user_info['phonenum'][-1]}",reply_markup=markup)
                        check=None
                    else:
                        bot.reply_to(message,"Incorrect phone number")
                elif(check=="passed_yes"):
                    if(sn==None):
                        sn=message.text
                        user_info["sname"].append(sn)
                        bot.send_message(message.from_user.id,"Please enter your phone number : ")
                        check="passed_sn"
@bot.callback_query_handler(func=lambda call : True)
def edit_callback(call):
    global fn
    global sn
    global phone
    if call.data=="edit":
        markup=telebot.types.InlineKeyboardMarkup()
        markup.row_width=2
        markup=telebot.types.InlineKeyboardButton("Edit First name",callback_data="edit_fname")
        markup=telebot.types.InlineKeyboardButton("Edit Last name",callback_data="edit_sname")
        markup=telebot.types.InlineKeyboardButton("Edit Phone number",callback_data="edit_num")
        bot.send_message(call.message.from_user.id,f"First name : {fn}\nLast name : {sn}\nPhone Number : {0}",reply_markup=markup)
    elif call.data=="edit_fname":
       pass
bot.infinity_polling()
