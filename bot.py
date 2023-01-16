#!/usr/bin/env python

import logging 
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()


id = 0

dzList = """

---
Алгебраические структуры - 1
Однородные СЛАУ - 2
Линейная оболочка - 3
Неоднородные СЛАУ - 4
Сумма и пересечение подпространств - 5
---
"""

path = "C:\\users\\rud\\desktop\\geotg"
files = os.listdir(path)

for item in files:
    if item.endswith(".txt"):
        os.remove(os.path.join(path, item))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
f"""Здарова {user.first_name}! Присылай мне номер дз: {dzList}
Условия присылать в порядке чтения, то есть например матрица 2x5 будет выглядеть так [1 2 3 4 5; 6 7 8 9 10], вертикальные матрицы вида МНОГОx1 транспонируем в [1 2 3]
Если в условии больше двух матриц, пишем новую матрицу на новой строке

""")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Напиши просто номер домашки, и там будет пример ввода к ней. В нем задания разделены пустой строкой для понимания")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mainFunc))
    # application.add_handler(MessageHandler(filters.ATTACHMENT, backward))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

dzTaskCount = [0, 9, 14, 25, 15, 20]
async def mainFunc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global id
    id += 1
    fileName = "id" + str(id) + ".txt"
    # tasks = []
    # lines = update.message.text.split("\n")
    theMessage = update.message.text
    tasks = theMessage.split("\n")
    tasksGood = True
    dickt = list("[] .-1234567890;")
    dickt.append("\n")
    
    for i in theMessage:
        if i not in dickt:
            tasksGood = False
            break
    tasks = list(filter(None, tasks))
    
    # for line in lines:
        
    

    # print(tasks)
    dz = tasks[0]
    numbers = "12345"
    if tasksGood:
        if dz in numbers:
            dz = int(dz)
            if len(tasks) == 1:
                match dz:
                    case 1:
                        await update.message.reply_text("""ДЗ 1\. Алгебраические структуры, в нём я умею решать задания 5 и 6

Если вам нужны только некоторые задания, скопируйте пример ввода и измените в нем только части с нужными вам заданиями

Пример ввода:

```
1

[1 1 1]
[2 2 2]

[1 1 1]
[2 2 2]
[3 3 3]
[4 4 4]
[5 5 5]
[6 6 6]
[7 7 7]
```        
                        """, parse_mode='MarkdownV2')
                    case 2:
                        await update.message.reply_text("""ДЗ 2\. Однородные СЛАУ, в нём я умею решать все 6 заданий

Если вам нужны только некоторые задания, скопируйте пример ввода и измените в нем только части с нужными вам заданиями

Пример ввода:

```
2

[1 1 1 1 1; 2 2 2 2 2; 3 3 3 3 3; 4 4 4 4 4; 5 5 5 5 5]

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]

[1 1 1 1 1; 2 2 2 2 2; 3 3 3 3 3; 4 4 4 4 4; 5 5 5 5 5]

[1 1 1 1 1; 2 2 2 2 2; 3 3 3 3 3; 4 4 4 4 4; 5 5 5 5 5]

[1 1 1]
[2 2 2]
[3 3 3]

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]
```                    
                        """, parse_mode='MarkdownV2')
                    case 3:
                        await update.message.reply_text("""ДЗ 3\. Линейная оболочка, в нём я умею решать все 5 заданий

Если вам нужны только некоторые задания, скопируйте пример ввода и измените в нем только части с нужными вам заданиями

Пример ввода:

```
3

[1 1 1 1 1]
[2 2 2 2 2]
[3 3 3 3 3]
[4 4 4 4 4]
[5 5 5 5 5]

[1 1 1]
[2 2 2]
[3 3 3]
[4 4 4]
[5 5 5]
[6 6 6]

[1 1 1 1 1]
[2 2 2 2 2]
[3 3 3 3 3]
[4 4 4 4 4]
[5 5 5 5 5]

[1 1 1 1 1]
[2 2 2 2 2]
[3 3 3 3 3]
[4 4 4 4 4]
[5 5 5 5 5]

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]
```                 
                        """, parse_mode='MarkdownV2')
                    case 4:
                        await update.message.reply_text("""ДЗ 4\. Неоднородные СЛАУ, в нём я умею решать все 6 заданий

Если вам нужны только некоторые задания, скопируйте пример ввода и измените в нем только части с нужными вам заданиями

Пример ввода:

```
4

[1 1 1 1 1 1; 2 2 2 2 2 2; 3 3 3 3 3 3; 4 4 4 4 4 4; 5 5 5 5 5 5; 6 6 6 6 6 6]

[1 1 1 1 1]
[2 2 2 2 2]
[3 3 3 3 3]
[4 4 4 4 4]

[1 1 1 1 1; 2 2 2 2 2; 3 3 3 3 3; 4 4 4 4 4; 5 5 5 5 5]

[1 1 1 1 1 1; 2 2 2 2 2 2; 3 3 3 3 3 3; 4 4 4 4 4 4; 5 5 5 5 5 5; 6 6 6 6 6 6]

[1 1 1]
[2 2 2]
[3 3 3]
[4 4 4]

[1 1 1]
[2 2 2]
[3 3 3]
[4 4 4]
```
                        
                        """, parse_mode='MarkdownV2')
                        # await update.message.reply_text("Над четвертым еще работа кипит, пока что не работает")
                    case 5:
                        await update.message.reply_text("""ДЗ 5\. Сумма и пересечение подпространств, в нём я умею решать все 4 задания

Если вам нужны только некоторые задания, скопируйте пример ввода и измените в нем только части с нужными вам заданиями

Пример ввода:

```
5

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]
[5 5 5 5]

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]
[5 5 5 5]

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]
[5 5 5 5]

[1 1 1 1]
[2 2 2 2] 
[3 3 3 3]
[4 4 4 4]
[5 5 5 5]
```
                        """, parse_mode='MarkdownV2')
                    case _: await update.message.reply_text("Не знаю, что это за домашка такая")
            elif (len(tasks)-1) != dzTaskCount[dz]:
                await update.message.reply_text("Неправильное количество введенных условий: " + str(len(tasks)-1) + ", так как для ДЗ №" + str(dz) + " нужно " + str(dzTaskCount[dz]) + " условий!") 
            else:
                if dz in [1, 2, 3, 4, 5]:
                    inputArgs = str(id) + ", " + ', '.join(tasks[1:dzTaskCount[dz]+1])
                    print("Начинаю выполнение заказа " + str(id) + ", дз " + str(dz) + " для " + str(update.message.from_user['username']))
                    print(tasks)
                    os.system("matlab -nosplash -nodesktop -minimize -r \"try, dz" + str(dz) + "(" + inputArgs + "), catch, exit, end, exit\"")
                    while not os.path.exists(fileName):
                        await asyncio.sleep(1)
                    await asyncio.sleep(2)
                    with open(fileName, encoding="utf-8") as file:
                        line = "ДЗ №" + str(dz) + "\n" + file.readline().rstrip().replace(">", "\n")
                        if dz not in [4]:
                            # if line.count("[") == line.count("]"):
                            line = line.replace("[", "`[").replace("]", "]`")
                        # else:
                        #     line += "`"
                        # print(line)
                    await update.message.reply_text(line, parse_mode='MarkdownV2')    
                else:
                    await update.message.reply_text("Не знаю, что это за домашка такая")
                print("Завершаю выполнение заказа " + str(id) + ", дз " + str(dz) + " для " + str(update.message.from_user['username']))
        else:
            await update.message.reply_text("На первой строке должен быть только номер домашки!")
    else:
        await update.message.reply_text("В вашем запросе есть запрещенные символы, например \"" + i + "\"\n Исправьте свой запрос и пришлите его заново.")


    # if update.message.from_user.id == 444620736:
    #     await update.message.copy(chat_id='5333890704')
    # elif update.message.from_user.id == 364962073:
    #     await update.message.copy(chat_id='5333890704')


# async def backward(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if update.message.from_user.id == 5333890704:
#         await update.message.copy(chat_id='444620736')
#         await update.message.copy(chat_id='364962073')


if __name__ == "__main__":
    main()