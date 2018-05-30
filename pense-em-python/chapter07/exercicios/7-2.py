

def eval_loop():
    while True:
        result = input('>>>')
        if result == 'done':
            print(result_eval)
            break
        else:
            result_eval = eval(result)
            print(result_eval)

eval_loop()