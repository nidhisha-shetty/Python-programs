def  div(a,b):
    print(a/b)

def smart_div(func):
    def smart_div_args(x,y):
        
        if x<y:
            x,y = y,x
        return func(x,y)
    return smart_div_args
    
division=smart_div(div)
division(4,8)