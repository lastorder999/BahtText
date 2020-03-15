def number2String(number):
    return str("{:.2f}".format(number))

def spellNagativeValue(number, text):
    text = "ลบ" + text if number < 0 else text
    return text
    
def changeDecimalPoint(number):
    return round(abs(number), 2)

def spellCurrency(front: str, rear: str) -> str:
    if front == "ศูนย์" and rear != '':
        textRear = rear + "สตางค์" 
        return textRear
    else:
        textFront = front + "บาท"
        textRear = "ถ้วน" if rear is '' else rear + "สตางค์"
        return textFront + textRear

def splitDot(strNumber: str) -> str:
    temp = strNumber.split('.')
    if len(temp) != 1:
        front = temp[0]
        rear = temp[1]
    else:
        front = temp[0]
        rear = ''
    return front, rear

def spellNumber(strNumber: str) -> str:
    text = ""
    if strNumber is '0':
        text = getDigit('0') 
    elif strNumber is '1' or strNumber == "01":
        text = getDigit('1')
    else:
        for index, value in enumerate(strNumber[::-1]):
            if index is 0 and value is '1':
                text = 'เอ็ด'
            elif index % 6 is 0 and index is not 0:
                text = getDigit(value) + getPlaces(6) + text
            elif value is not '0':
                text = getDigit(value) + getPlaces(index % 6) + text
        for search, replaces in getException():
            text = text.replace(search, replaces)
    return text

def getDigit(digit: str) -> str:
    digits = {
        '0':"ศูนย์", '1':"หนึ่ง", '2':"สอง", '3':"สาม", '4':"สี่", '5':"ห้า", '6':"หก", '7':"เจ็ด", '8':"แปด", '9':"เก้า"
    }
    return digits.get(digit)

def getPlaces(index: int):
    places = [
        "", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"
    ]
    return places[index]

def getException():
    exceptions = {
        'ศูนย์':'',
        'หนึ่งสิบ':'สิบ',
        'สองสิบ':'ยี่สิบ',
        'สิบหนึ่ง':'สิบเอ็ด'
    }
    return exceptions.items()

def bahtText(number):
    
    baht, satang = splitDot(number2String(changeDecimalPoint(number)))
    text = spellNagativeValue(number, spellCurrency(spellNumber(baht), spellNumber(satang)))
    return text
