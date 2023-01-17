#!/usr/bin/env python

from dotenv import load_dotenv
load_dotenv()

import logging 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
# __________________________________________________

hwNums = [1, 2, 3, 4, 5]

id = 0
acceptedChars = list("[] .-1234567890;")
acceptedChars.append("\n")


# ____________________

hwList = """

Алгебраические структуры - 1
Однородные СЛАУ - 2
Линейная оболочка - 3
Неоднородные СЛАУ - 4
Сумма и пересечение подпространств - 5

"""
# ____________________

# ____________________

beforeExampleText = """

Если вам нужны только некоторые задания, скопируйте пример ввода и измените в нем только части с нужными вам заданиями

Пример ввода:

"""
# ____________________


# Remove temporary files on start
rootFolder = os.getcwd()
for item in os.listdir(rootFolder):
    if item.endswith(".txt"):
        os.remove(os.path.join(rootFolder, item))

# Get examples and count conditions for a card
hwExamples = {}
hwConditionCount = {}
for fileName in os.listdir("examples"):
    with open(os.path.join("examples", fileName), encoding="utf-8") as file:
        card = int(fileName.replace(".txt", ""))
        fullText = file.read()
        hwExamples[card] = fullText
        hwConditionCount[card] = len(list(filter(None, fullText.split("\n"))))

# Get descriptions
hwDescriptions = {}
for fileName in os.listdir("descriptions"):
    with open(os.path.join("descriptions", fileName), encoding="utf-8") as file:
        card = int(fileName.replace(".txt", ""))
        hwDescriptions[card] = file.read()


async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(f"Здарова {user.mention_html()}!")
    await update.message.reply_text(f"Присылай мне номер дз: {hwList}", disable_notification=True)
    await update.message.reply_text("""
Условия присылать в порядке чтения, то есть например матрица 2x5 будет выглядеть так 
`\[1 2 3 4 5; 6 7 8 9 10\]`
Вертикальные матрицы вида 3x1 транспонируем так
`\[1 2 3\]`\.

Если в условии несколько матриц, пишем новую матрицу на новой строке\. 

Если система, то считать её за матрицу `\[1 2 3; 4 5 6\]`, если есть пропущенная переменая \(e1 e2 e4 \- нет e3\), на ее место ставим 0, это важно\!
""", parse_mode='MarkdownV2', disable_notification=True)


async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
f"""Напиши просто номер домашки, и там будет пример ввода к ней. В нем задания разделены пустой строкой для понимания""")


async def matlabText(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    # Check for illegal characters
    for character in message:
        if character not in acceptedChars:
            await update.message.reply_text("В вашем запросе есть запрещенные символы, например \"" + character + "\"\n Исправьте свой запрос и пришлите его заново.")
            return

    conditions = message.split("\n")
    conditions = list(filter(None, conditions))
    hw = conditions[0] # Number of the homework

    # Check if hw number is really a number
    if hw not in '1234567890':
        await update.message.reply_text("На первой строке должен быть только номер домашки!")
        return

    hw = int(hw)

    # Check if this homework is registered
    if hw not in hwNums:
        await update.message.reply_text("Не знаю, что это за домашка такая")
        return

    # Only homework oneline
    if len(conditions) == 1:
        await update.message.reply_text(hwDescriptions[hw])
        await update.message.reply_text(beforeExampleText, disable_notification=True)
        await update.message.reply_text(f"```\n{hwExamples[hw]}\n```", parse_mode='MarkdownV2', disable_notification=True)
        return
        
    # Check if amount of conditions is same as needed
    if len(conditions) != hwConditionCount[hw]:
        await update.message.reply_text("Неправильное количество введенных условий: " + str(len(conditions)-1) + ", так как для ДЗ №" + str(hw) + " нужно " + str(hwConditionCount[hw]) + " условий!") 
        return

    global id
    id += 1

    # logging
    print("Начинаю выполнение заказа " + str(id) + ", дз " + str(hw) + " для " + str(update.message.from_user['username']))
    print(conditions)

    pendingMessage = await update.message.reply_text(f"""
    
Условия верны! Начинаю работу..

⚠️ Если в течении 10 секунд ответ не поступит, значит что бот завис/выключился и нужно написать @ruddnev

    """) 

    fileName = "id" + str(id) + ".txt"
    inputArgs = str(id) + ", " + ', '.join(conditions[1:hwConditionCount[hw]+1])

    os.system("matlab -nosplash -nodesktop -minimize -r \"try, dz" + str(hw) + "(" + inputArgs + "), catch, exit, end, exit\"")
    
    while not os.path.exists(fileName):
        await asyncio.sleep(1)
    await asyncio.sleep(2)

    with open(fileName, encoding="utf-8") as file:
        line = "ДЗ №" + str(hw) + "\n" + file.readline().rstrip().replace(">", "\n")
        if hw != 4:
            line = line.replace("[", "`[").replace("]", "]`")

    await context.bot.deleteMessage(message_id = pendingMessage.message_id, chat_id = update.message.chat_id)
    await update.message.reply_text(line, parse_mode='MarkdownV2')    
    
    print("Завершаю выполнение заказа " + str(id) + ", дз " + str(hw) + " для " + str(update.message.from_user['username']))







def main() -> None:
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    application.add_handler(CommandHandler("start", startCommand))
    application.add_handler(CommandHandler("help", helpCommand))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, matlabText))
    # application.add_handler(MessageHandler(filters.ATTACHMENT, matlabFile))

    application.run_polling()


if __name__ == "__main__":
    main()