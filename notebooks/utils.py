import numpy as np

lime = {
    'rgb': np.array([0,255,0]),
    'hex': '#00ff00',
    'low_hsv': np.array([50, 230,230]),
    'high_hsv': np.array([70, 260,260]),
    'category': '01_books'
}

orange = {
    'rgb': np.array([255,165,0]),
    'hex': '#ffa500',
    'low_hsv': np.array([15,210, 230]),
    'high_hsv': np.array([20,300,300]),
    'category': '02_wall_hangings'
}

blue = {
    'rgb': np.array([0,0,255]),
    'hex': '#0000ff',
    'low_hsv': np.array([110, 240,190]),
    'high_hsv': np.array([140, 260,250]),
    'category': '03_objects'
}

pink = {
    'rgb': np.array([255,20,147]),
    'hex': '#ff1493',
    'low_hsv': np.array([160,200, 220]),
    'high_hsv': np.array([170,260,260]),
    'category': '04_teacher'
}


categories = [lime,orange,blue,pink]
