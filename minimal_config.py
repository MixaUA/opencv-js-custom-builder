# minimal_config.py
# Мінімальний набір OpenCV.js для розпізнавання круглокоду

core = {
    '': [
        'countNonZero',
        'minMaxLoc',

        'bitwise_xor',
        'bitwise_and',
        'bitwise_not',

        'transpose',
        'flip'
    ]
}

imgproc = {
    '': [
        # Перетворення та фільтрація
        'cvtColor',
        'threshold',
        'adaptiveThreshold',
        'GaussianBlur',
        'medianBlur',

        # Морфологія
        'getStructuringElement',
        'erode',
        'dilate',
        'morphologyEx',

        # Контури
        'findContours',
        'contourArea',
        'arcLength',
        'approxPolyDP',
        'convexHull',
        'isContourConvex',

        # Геометрія
        'moments',
        'boundingRect',
        'minAreaRect',
        'boxPoints',
        'minEnclosingCircle',
        'fitEllipse',

        # Перетворення
        'getRotationMatrix2D',
        'warpAffine',
        'getPerspectiveTransform',
        'warpPerspective'
    ]
}

imgcodecs = {
    '': [
        'imencode',
        'imdecode'
    ]
}

white_list = makeWhiteList([
    core,
    imgproc,
    imgcodecs
])
