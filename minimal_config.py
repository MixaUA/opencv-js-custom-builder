# minimal_config.py
# Хірургічний мінімум функцій OpenCV для роботи нашого круглокоду
#
# Формат конфіга opencv.js: окремі словники по модулях, ключ ''
# означає "вільні функції модуля" (не методи класу). makeWhiteList()
# вже є всередині генератора байндингів OpenCV - визначати самим не треба.
#
# Класи Mat/Rect/Point/Size/Scalar/RotatedRect та константи
# (COLOR_BGR2GRAY, THRESH_BINARY, RETR_TREE, CHAIN_APPROX_SIMPLE...)
# підключаються автоматично разом із функціями, які їх використовують.
#
# imread/imwrite прибрані: в браузері немає файлової системи.
# Замість них - imencode/imdecode (буфер у памʼяті).

core = {
    '': [
        'countNonZero', 'minMaxLoc', 'bitwise_xor', 'bitwise_and', 'bitwise_not',
        'transpose', 'flip'
    ]
}

imgproc = {
    '': [
        'cvtColor', 'threshold', 'adaptiveThreshold', 'GaussianBlur', 'medianBlur',
        'findContours', 'contourArea', 'arcLength', 'approxPolyDP',
        'moments', 'minEnclosingCircle', 'fitEllipse', 'boundingRect',
        'warpAffine', 'getRotationMatrix2D', 'warpPerspective', 'getPerspectiveTransform'
    ]
}

imgcodecs = {
    '': ['imencode', 'imdecode']
}

white_list = makeWhiteList([core, imgproc, imgcodecs])
