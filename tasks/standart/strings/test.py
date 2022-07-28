try:
    try:
        10/0
    except ZeroDivisionError:
        print ('деление на ноль')
except Exception:
    print('ошибка')

