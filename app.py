import eel

eel.init('web')

@eel.expose
def calculate(expression, base):
    try:
        result = eval(expression)
        if base == 'binary':
            return bin(result)
        elif base == 'octal':
            return oct(result)
        elif base == 'decimal':
            return str(result)
        elif base == 'hexadecimal':
            return hex(result)
        else:
            return str(result)
    except Exception as e:
        return str(e)

eel.start('initial.html', size=(800,600))