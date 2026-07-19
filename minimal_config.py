# minimal_config.py
# Хірургічний мінімум функцій OpenCV для роботи нашого круглокоду
#
# ВАЖЛИВО: imread/imwrite НЕ підтримуються в opencv.js (немає файлової
# системи в браузері). Для роботи з картинками у JS використовуються
# imencode/imdecode (робота з буфером у пам'яті), і вони задаються
# ОКРЕМИМ словником `imgcodecs`, а не всередині `white_list`.

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
    ]
}

imgcodecs = {
    '': ['imencode', 'imdecode']
}
