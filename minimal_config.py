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
white_list = makeWhiteList([
    core,
    imgproc
])
