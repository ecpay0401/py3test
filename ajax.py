def ajax(url, /, **user_settings):
    settings = {
        'method' : user_settings.get('method', 'GET'),
        'contents' : user_settings.get('contents', ''),
        'datatype' : user_settings.get('datatype', 'text/plain'),
        # 其他設定 ...
    }
    print('請求 {}'.format(url))
    print('設定 {}'.format(settings))
#ajax(url = 'https://openhome.cc', method = 'POST')
ajax('https://openhome.cc', method = 'POST')