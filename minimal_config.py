# minimal_config.py
# Хірургічний мінімум функцій OpenCV для роботи нашого круглокоду
#
# ВАЖЛИВО: справжній формат конфіга opencv.js — це окремі словники
# по модулях, де ключ '' означає "вільні функції модуля" (не методи
# класу). Їх потім об'єднує функція makeWhiteList(), яка вже є
# всередині генератора байндингів OpenCV - визначати її самим не треба.
#
# Класи Mat/Rect/Point/Size/Scalar та константи (COLOR_BGR2GRAY,
# THRESH_BINARY і т.д.) прописувати тут НЕ треба - вони підключаються
# автоматично разом із функціями, які їх використовують.
#
# imread/imwrite прибрані повністю: в браузері немає файлової системи,
# ці функції в opencv.js не існують. Замість них - imencode/imdecode
# (робота з картинкою через буфер у пам'яті).

core = {
    '': [
        'countNonZero', 'minMaxLoc', 'bitwise_xor', 'bitwise_and', 'bitwise_not'
    ]
}

imgproc = {
    '': [
        'cvtColor', 'threshold', 'adaptiveThreshold', 'GaussianBlur', 'medianBlur',
        'findContours', 'contourArea', 'arcLength', 'approxPolyDP',
        'warpAffine', 'getRotationMatrix2D', 'warpPerspective', 'getPerspectiveTransform'
    ]
}

imgcodecs = {
    '': ['imencode', 'imdecode']
}

white_list = makeWhiteList([core, imgproc, imgcodecs])
