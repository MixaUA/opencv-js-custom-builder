# minimal_config.py
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
