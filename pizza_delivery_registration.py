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
    if message.text=="Order a Pizza":
        bot.reply_to(message,"Please enter your first name :")
    else:
        for i in range(len(user_info["fname"])):
            if(user_info["fname"][i]==message.text and check!="edit_fname_pressed" and check !="edit_sname_pressed" and check !="edit_num_pressed"):
                fn=user_info["fname"][i]
                sn=user_info["sname"][i]
                phone=user_info["phonenum"][i]
                markup=telebot.types.InlineKeyboardMarkup()
                markup.row_width = 2
                edit_user_info=telebot.types.InlineKeyboardButton("Edit",callback_data="edit")
                order=telebot.types.InlineKeyboardButton("Order",callback_data="order")
                markup.add(edit_user_info,order)
                bot.send_message(message.from_user.id,f"First name : {user_info['fname'][i]}\nLast name : {user_info['sname'][i]}\nPhone Number : {user_info['phonenum'][i]}",reply_markup=markup)
                break
        else:
            if(message.text=="Yes"):
                user_info["fname"].append(fn)
                check="passed_yes"
                bot.send_message(message.from_user.id,"Please enter your surname : ")
                sn=None
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
                        order=telebot.types.InlineKeyboardButton("Order",callback_data="order")
                        markup.add(edit_user_info,order)
                        bot.send_message(message.from_user.id,f"First name : {user_info['fname'][-1]}\nLast name : {user_info['sname'][-1]}\nPhone Number : {user_info['phonenum'][-1]}",reply_markup=markup)
                        phone=message.text
                        check=None
                    else:
                        bot.reply_to(message,"Incorrect phone number")
                elif(check=="passed_yes"):
                    if(sn==None):
                        sn=message.text
                        user_info["sname"].append(sn)
                        bot.send_message(message.from_user.id,"Please enter your phone number : ")
                        check="passed_sn"
                elif(check=="edit_fname_pressed"):
                    for i in range(len(user_info["fname"])):
                        if(fn==user_info["fname"][i]):
                            user_info["fname"][i]=message.text
                            fn=user_info["fname"][i]
                            markup=telebot.types.InlineKeyboardMarkup()
                            markup.row_width = 2
                            edit_user_info=telebot.types.InlineKeyboardButton("Edit",callback_data="edit")
                            order=telebot.types.InlineKeyboardButton("Order",callback_data="order")
                            markup.add(edit_user_info,order)
                            bot.send_message(message.from_user.id,f"First name : {user_info['fname'][i]}\nLast name : {user_info['sname'][i]}\nPhone Number : {user_info['phonenum'][i]}",reply_markup=markup)
                            check=None
                            break
                elif(check=="edit_sname_pressed"):
                    for i in range(len(user_info["sname"])):
                        if(sn==user_info["sname"][i]):
                            user_info["sname"][i]=message.text
                            sn=user_info["sname"][i]
                            markup=telebot.types.InlineKeyboardMarkup()
                            markup.row_width = 2
                            edit_user_info=telebot.types.InlineKeyboardButton("Edit",callback_data="edit")
                            order=telebot.types.InlineKeyboardButton("Order",callback_data="order")
                            markup.add(edit_user_info,order)
                            bot.send_message(message.from_user.id,f"First name : {user_info['fname'][i]}\nLast name : {user_info['sname'][i]}\nPhone Number : {user_info['phonenum'][i]}",reply_markup=markup)
                            check=None
                            break
                elif(check=="edit_num_pressed"):
                    for i in range(len(user_info["phonenum"])):
                        if(phone==user_info["phonenum"][i]):
                            if(message.text[0:5]=="+998"):
                                user_info["phonenum"][i]=message.text
                                phone=user_info["phonenum"][i]
                                markup=telebot.types.InlineKeyboardMarkup()
                                markup.row_width = 2
                                edit_user_info=telebot.types.InlineKeyboardButton("Edit",callback_data="edit")
                                order=telebot.types.InlineKeyboardButton("Order",callback_data="order")
                                markup.add(edit_user_info,order)
                                bot.send_message(message.from_user.id,f"First name : {user_info['fname'][i]}\nLast name : {user_info['sname'][i]}\nPhone Number : {user_info['phonenum'][i]}",reply_markup=markup)
                                check=None
                                break
                elif(message.text[0:5]!='+998'):
                    bot.send_message(message.from_user.id,"You have entered something wrong. Please check everything and retry. Have you entered the phone number correctly? Did you type it with +")
@bot.callback_query_handler(func=lambda call : True)
def edit_callback(call):
    global fn
    global sn
    global phone
    global check
    global pizza_type
    global pizza_type_portion
    if call.data=="edit":
        markup=telebot.types.InlineKeyboardMarkup()
        markup.row_width=2
        edit_fname=telebot.types.InlineKeyboardButton("Edit First Name",callback_data="edit_fname")
        edit_sname=telebot.types.InlineKeyboardButton("Edit Last Name",callback_data="edit_sname")
        edit_num=telebot.types.InlineKeyboardButton("Edit Phone Number",callback_data="edit_num")
        delete=telebot.types.InlineKeyboardButton("Delete Account",callback_data="delete")
        markup.add(edit_fname,edit_sname,edit_num,delete)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"First name : {fn}\nLast name : {sn}\nPhone Number : {phone}",reply_markup=markup)
    elif call.data=="order":
       markup=telebot.types.InlineKeyboardMarkup()
       first_t=telebot.types.InlineKeyboardButton("1",callback_data="first")
       second_t=telebot.types.InlineKeyboardButton("2",callback_data="second")
       markup.add(first_t,second_t)
       bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Choose pizza type:",reply_markup=markup)
    elif call.data=="edit_fname":
        for i in range(len(user_info["fname"])):
            if(user_info["fname"][i]==fn):
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please enter your first name")
                check="edit_fname_pressed"
    elif call.data=="edit_sname":
        for i in range(len(user_info["fname"])):
            if(user_info["sname"][i]==sn):
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please enter your last name")
                check="edit_sname_pressed"
    elif call.data=="edit_num":
        for i in range(len(user_info["phonenum"])):
            if(user_info["phonenum"][i]==phone):
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please enter your phone number")
                check="edit_num_pressed"
    elif call.data=="first":
        markup=telebot.types.InlineKeyboardMarkup()
        small=telebot.types.InlineKeyboardButton("Small",callback_data="small")
        medium=telebot.types.InlineKeyboardButton("Medium",callback_data="medium")
        large=telebot.types.InlineKeyboardButton("Large",callback_data="large")
        markup.add(small,medium,large)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please choose the portion",reply_markup=markup)
        print(fn,sn,phone,"first",end="")
    elif call.data=="second":
        markup=telebot.types.InlineKeyboardMarkup()
        small=telebot.types.InlineKeyboardButton("Small",callback_data="small")
        medium=telebot.types.InlineKeyboardButton("Medium",callback_data="medium")
        large=telebot.types.InlineKeyboardButton("Large",callback_data="large")
        markup.add(small,medium,large)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please choose the portion",reply_markup=markup)
        print(fn,sn,phone,"second",end="")
    elif call.data=="large":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please send your location")
        print(" Large")
    elif call.data=="medium":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please send your location")
        print(" Medium")
    elif call.data=="small":
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Please send your location")
        print(" Small")
    elif call.data=="delete":
        for i in range(len(user_info["fname"])):
            if(fn==user_info["fname"][i]):
                user_info["fname"].pop(i)
                user_info["sname"].pop(i)
                user_info["phonenum"].pop(i)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Your account has been deleted successfully")
bot.infinity_polling()
