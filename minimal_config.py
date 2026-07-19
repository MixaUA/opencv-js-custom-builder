# minimal_config.py
# Визначаємо хірургічний мінімум функцій OpenCV для роботи нашого круглокоду

white_list = {
    'core': [
        'Mat', 'Rect', 'Point', 'Size', 'Scalar',
        'countNonZero', 'minMaxLoc', 'bitwise_xor', 'bitwise_and', 'bitwise_not'
    ],
    'imgproc': [
        'cvtColor', 'threshold', 'adaptiveThreshold', 'GaussianBlur', 'medianBlur',
        'findContours', 'contourArea', 'arcLength', 'approxPolyDP',
        'warpAffine', 'getRotationMatrix2D', 'warpPerspective', 'getPerspectiveTransform',
        'COLOR_BGR2GRAY', 'COLOR_RGBA2GRAY', 'THRESH_BINARY', 'THRESH_BINARY_INV', 
        'THRESH_OTSU', 'ADAPTIVE_THRESH_GAUSSIAN_C', 'RETR_EXTERNAL', 'CHAIN_APPROX_SIMPLE'
    ],
    'imgcodecs': [
        'imread', 'imwrite', 'imencode', 'imdecode'
    ]
}
