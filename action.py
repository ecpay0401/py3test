dt = {'x': 10, 'y': 20}

match dt:
    case {'x': 0, 'y': 0}:
        print('原點')
    case {'x': x, 'y': y} if x * y > 0:
        print('一、三象限', (x, y))
    case {'x': x, 'y': y} if x * y < 0:
        print('二、四象限', (x, y))