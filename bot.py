#!/usr/bin/env python

from dotenv import load_dotenv
load_dotenv()

import logging 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

import re # for parsing file input
import os # for removing files
import magic # for guessing file type
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

hwNums = [1, 2, 3, 4, 5]
prohibitedUserIDs = [848733048, 430123872]
prohibitedUsernames = []

id = 0
dlId = 0
acceptedChars = list("[] .-1234567890;")
acceptedChars.append("\n")



hwList = """

Алгебраические структуры - 1
Однородные СЛАУ - 2
Линейная оболочка - 3
Неоднородные СЛАУ - 4
Сумма и пересечение подпространств - 5

"""

beforeExampleText = """

💹 *Эту домашку можно автоматически загрузить в бота\! Для этого нужно зайти на страницу домашки на геолине, нажать Ctrl\+S, куда\-нибудь сохранить и отправить этот файл боту\.*
*⚠️ Работает только на компьютере*

Но если вы хотите вручную, то вот пример ввода:

"""

async def slaewrite1(str):
    coefficients = []
    result = '['
    str = str.replace(" ", "")
    equations = re.split(r'\\\\', str)
    for i in equations:
        coefficients.append(re.findall(r'(?:[-\^]?\d+)|(?:[-]+)', i))
    for i in coefficients:
        lastindex = 0
        for j in range(len(i)):
            if i[j] == '-':
                i[j] = '-1'
            if i[j][0] == '^':
                while int(i[j][1]) - lastindex > 1:
                    result += '0 '
                    lastindex += 1
                if j != 0:
                    if i[j - 1][0] != '^':
                        result += i[j - 1] + ' '
                    else:
                        result += '1 '
                elif j == 0:
                    result += '1 '
                lastindex += 1
            elif j == len(i) - 1:
                while lastindex < 5:
                    result += '0 '
                    lastindex += 1
                result += i[j] + '; '
    result = result[:-2] + ']'
    return result

async def slaewrite2(str):
    coefficients = []
    result = '['
    str = str.replace(" ", "")
    equations = re.split(r'\\\\', str)
    for i in equations:
        coefficients.append(re.findall(r'(?:[-\^]?\d+)|(?:[-]+)', i))
    for i in coefficients:
        lastindex = 0
        for j in range(len(i) - 1):
            if i[j] == '-':
                i[j] = '-1'
            if i[j][0] == '^':
                while int(i[j][1]) - lastindex > 1:
                    result += '0 '
                    lastindex += 1
                if j != 0:
                    if i[j - 1][0] != '^':
                        result += i[j - 1] + ' '
                    else:
                        result += '1 '
                elif j == 0:
                    result += '1 '
                lastindex += 1
                if j == len(i) - 2:
                    while lastindex < 5:
                        result += '0 '
                        lastindex += 1
                    result += '; '
    result = result[:-2] + ']'
    return result


# Remove temporary files on start
rootFolder = os.getcwd()
for item in os.listdir(rootFolder):
    if item.endswith(".txt"):
        os.remove(os.path.join(rootFolder, item))

# Get examples and count conditions for a card, then count row length
hwExamples = {}
hwConditionCount = {}
hwRowsLengths = {}
for fileName in os.listdir("examples"):
    with open(os.path.join("examples", fileName), encoding="utf-8") as file:
        card = int(fileName.replace(".txt", ""))
        fullText = file.read()
        hwExamples[card] = fullText
        conditions = list(filter(None, fullText.split("\n")))
        hwConditionCount[card] = len(conditions)
        hwRowsLengths[card] = [len(list(filter(None, condition[1:-1].split(";")[0].split()))) for condition in conditions]

# Get descriptions
hwDescriptions = {}
for fileName in os.listdir("descriptions"):
    with open(os.path.join("descriptions", fileName), encoding="utf-8") as file:
        card = int(fileName.replace(".txt", ""))
        hwDescriptions[card] = file.read()


async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE, fromHelp = False) -> None:
    await beforeRunning(update, context)
    user = update.effective_user
    if not fromHelp:
        await update.message.reply_html(f"Здарова {user.mention_html()}!")
    await update.message.reply_text(f"Присылай мне номер дз, чтобы увидеть пример ввода: {hwList}", disable_notification=True)
    await update.message.reply_text("""
💹 *Любую домашку можно автоматически загрузить в бот\. Для этого нужно зайти на страницу домашки на геолине, нажать Ctrl\+S, куда\-нибудь сохранить и отправить этот файл боту\.*
*⚠️ Работает только на компьютере, у БИТ не получится так загрузить ДЗ 2, так как там другое 6 задание*

Но если вы хотите писать условия вручную, то это нужно делать так:

Условия присылать в порядке чтения, то есть например матрица 2x5 будет выглядеть так 
`\[1 2 3 4 5; 6 7 8 9 10\]`
Вертикальные матрицы вида 3x1 транспонируем так
`\[1 2 3\]`\.

Если в условии несколько матриц, пишем новую матрицу на новой строке\. 

Если система, то считать её за матрицу `\[1 2 3; 4 5 6\]`, если есть пропущенная переменая \(e1 e2 e4 \- нет e3\), на ее место ставим 0, это важно\!
""", parse_mode='MarkdownV2', disable_notification=True)


async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await beforeRunning(update, context)
    await startCommand(update, context, fromHelp=True)


async def matlabText(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await beforeRunning(update, context): return

    message = update.message.text

    if message.count("<") > 10:
        await update.message.reply_text("😠 HTML-код страницы нельзя присылать напрямую! Сохраните его в файл и пришлите этот файл боту.")
        return 

    # Check for illegal characters
    for character in message:
        if character not in acceptedChars:
            await update.message.reply_text("В вашем запросе есть запрещенные символы, например \"" + character + "\"\n\nИсправьте свой запрос и пришлите его заново.")
            return
    conditions = message.split("\n")
    await matlab(update, context, conditions=conditions)


async def matlabFile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await beforeRunning(update, context): return

    global dlId
    dlId += 1
    dlFileName = "dlId" + str(dlId) + ".txt"
    dl = await context.bot.get_file(update.message.document)
    if dl.file_size > 1_000_000:
        await update.message.reply_text("Размер вашего файла слишком большой!")
        os.remove(dlFileName)
        return

    await dl.download_to_drive(dlFileName)

    if not magic.from_file(dlFileName).count("HTML document"):
        await update.message.reply_text("Файл не является HTML-кодом. Правильный файл можно получить так: переходите на страницу домашки, дожидаетесь ее полной загрузки, нажимаете Ctrl+S, куда-нибудь сохраняете этот файл, и присылаете его боту.")
        return

    with open(dlFileName, encoding="utf8") as file:
        fullText = file.read()
    os.remove(dlFileName)


    if fullText.count('Алгебраические структуры'): # HW 1
        found = re.findall(r'(?:begin\{pmatrix\}.*?end\{pmatrix\})|(?:\\left.*?\\right)', fullText)
        conditions = ['1']
        delete = [0, 1, 2, 12]
        for element in found:
            if found.index(element) not in delete: 
                conditions.append(str(re.findall(r'[-]?\d+', element)))
        conditions = [element.replace("\'", "").replace(",","") for element in conditions]

    elif fullText.count('Однородные СЛАУ'): # HW 2
        f = fullText.replace("\n", "")
        task5 = re.findall(r'= \(.*?\)', f)
        task2 = re.findall(r'begin\{array\}.*?end\{array\}', f)
        task1 = re.findall(r'begin\{cases\}.*?end\{cases\}', f)
        task4 = [task1.pop()]
        task3 = [task1.pop()]
        task6 = [task2.pop()]
        task2 = re.split(r'\\\\', task2[0])
        task2.pop()
        task6 = re.split(r'\\\\', task6[0])
        task6.pop()
        result = ['2']
        result.append(await slaewrite2(task1[0]))
        for i in task2:
            result.append(str(re.findall(r'[-]?\d+', i)))
        result.append(await slaewrite2(task3[0]))
        result.append(await slaewrite2(task4[0]))
        for i in task5:
            result.append(str(re.findall(r'[-]?\d+', i)))
        for i in task6:
            result.append(str(re.findall(r'[-]?\d+', i)))
        conditions = [element.replace("\'", "").replace(",","").replace(" ;", ";") for element in result]

    elif fullText.count('Линейная оболочка'): # HW 3
        f = fullText.replace("\n", "")
        f = re.findall(r'begin\{array\}.*?end\{array\}',f)
        result = ['3']
        for i in f:
            task5 = re.findall(r'[-]?\d+', i)
            result.append(str(task5))
        result.pop()
        for i in range(4):
            result.append("[" + ' '.join(task5[i*4:(i+1)*4]) + "]")
        conditions = [element.replace("\'", "").replace(",","") for element in result]

    elif fullText.count('Неоднородные СЛАУ'): # HW 4
        f = fullText.replace("\n", "")
        slae = re.findall(r'begin\{cases\}.*?end\{cases\}', f)
        result = ['4']
        result.append(await slaewrite1(slae[0]))
        for i in range(1, 5):
            numbers = re.findall(r'[-]?\d+', slae[i])
            for j in reversed(range(len(numbers))):
                if j % 2 == 0: numbers.pop(j)
            result.append(str(numbers))
        result.append(await slaewrite2(slae[5]))
        result.append(await slaewrite1(slae[6]))
        vectors = re.findall(r'= \(.*?\)', f)
        for i in vectors:
            result.append(str(re.findall(r'[-]?\d+', i)))
        conditions = [element.replace("\'", "").replace(",","") for element in result]

    elif fullText.count('Сумма и пересечение подпространств'): # HW 5
        f = fullText.replace("\n", "")
        tasks = re.findall('(?:суммы)|(?:пересечения)',f)
        if tasks[3] == 'суммы': 
            Task4Flag = 1
        else: 
            Task4Flag = 0
        f = re.findall(r'begin\{array\}.*?end\{array\}',f)
        result = ['5']
        delete = []
        for i in f:
            if f.index(i) not in delete: 
                result.append(str(re.findall(r'[-]?\d+',i)))
        result = result[:21:]
        conditions = [element.replace("\'", "").replace(",","") for element in result]

    else:
        await update.message.reply_text("⚠️ Не смог прочитать ваш файл. Ещё раз: переходите на страницу домашки, дожидаетесь ее полной загрузки, нажимаете Ctrl+S, куда-нибудь сохраняете этот файл, и присылаете его боту.")
        return


    # Check for illegal characters
    for element in conditions:
        for character in element:
            if character not in acceptedChars:
                await update.message.reply_text("В вашем тексте есть запрещенные символы, например \"" + character + "\"\n\nИсправьте свой запрос и пришлите его заново.")
                return

    await matlab(update, context, conditions=conditions)


async def matlab(update: Update, context: ContextTypes.DEFAULT_TYPE, conditions) -> None:
    conditions = list(filter(None, conditions))
    hw = conditions[0].strip() # Number of the homework

    # Check if hw number is really a number
    for character in hw:
        if character not in '1234567890':
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
        await update.message.reply_text(beforeExampleText, parse_mode='MarkdownV2', disable_notification=True)
        await update.message.reply_text(f"```\n{hwExamples[hw]}\n```", parse_mode='MarkdownV2', disable_notification=True)
        return
        
    # Check if amount of conditions is same as needed
    if len(conditions) != hwConditionCount[hw]:
        await update.message.reply_text("Неправильное количество введенных условий: " + str(len(conditions)-1) + ", так как для ДЗ №" + str(hw) + " нужно " + str(hwConditionCount[hw]) + " условий!") 
        return


    # Check for matrix length and for matrix rows to be the same length 
    for i in range(len(conditions)):
        condition = conditions[i]
        rowsLengths = [len(list(filter(None, row.split()))) for row in condition[1:-1].split(";")]
        if len(set(rowsLengths)) != 1:
            await update.message.reply_text("⚠️ Вы пропустили элемент матрицы в строке:\n`" + condition.replace('-', '\\-') + "`\n\nЕсли в системе есть пропущенная переменая \(e1 e2 e4 \- нет e3\), на ее место ставим 0, это важно\!", parse_mode='MarkdownV2')    
            return
        elif i != 0 and rowsLengths[0] != hwRowsLengths[hw][i]:
            await update.message.reply_text("⚠️ В условии `" + condition.replace('-', '\\-') + "`неверная длина строки матрицы\! Чисел должно быть " + str(hwRowsLengths[hw][i+1]) + ", а у вас " + str(rowsLengths[0]) + "\!", parse_mode='MarkdownV2')    
            return

    global id
    id += 1

    # logging
    print("___")
    print("Начинаю выполнение заказа " + str(id) + ", дз " + str(hw) + " для " + str(update.message.from_user['username']))
    print(conditions)

    pendingMessage = await update.message.reply_text("Начинаю работу..\n\n⚠️ Если в течении 10 секунд ответ не поступит, значит что бот завис/выключился") 

    fileName = "id" + str(id) + ".txt"
    inputArgs = str(id) + ", " + ', '.join(conditions[1:hwConditionCount[hw]+1])


    os.system("matlab -nosplash -nodesktop -minimize -r \"try, dz" + str(hw) + "(" + inputArgs + "), catch, exit, end, exit\"")
    
    waitedTime = 0
    while not os.path.exists(fileName):
        if waitedTime > 5:
            await update.message.reply_text("⚠️ Не смог высчитать ответ. Проверьте, скорее всего в условии есть ошибка.")
            return
        await asyncio.sleep(1)
        waitedTime += 1
    await asyncio.sleep(1)

    with open(fileName, encoding="utf-8") as file:
        line = "*ДЗ №" + str(hw) + "*\n" + file.readline().rstrip().replace(">", "\n")
        if hw != 4:
            line = line.replace("[", "`[").replace("]", "]`")

    await context.bot.deleteMessage(message_id = pendingMessage.message_id, chat_id = update.message.chat_id)
    await update.message.reply_text(line, parse_mode='MarkdownV2')    
    
    print("Завершаю выполнение заказа " + str(id) + ", дз " + str(hw) + " для " + str(update.message.from_user['username']))


async def beforeRunning(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if str(update.message.chat_id) != os.getenv("LOG"):
        await context.bot.forward_message(chat_id = os.getenv("LOG"), from_chat_id = update.message.chat_id, message_id = update.message.id)

    if update.message.from_user.id in prohibitedUserIDs or update.message.from_user.username in prohibitedUsernames:
        await context.bot.forward_message(chat_id = os.getenv("DEV"), from_chat_id = update.message.chat_id, message_id = update.message.id)
        return False

    return True
    


def main() -> None:
    
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    application.add_handler(CommandHandler("start", startCommand))
    application.add_handler(CommandHandler("help", helpCommand))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, matlabText))
    application.add_handler(MessageHandler(filters.ATTACHMENT, matlabFile))

    application.run_polling()


if __name__ == "__main__":
    main()