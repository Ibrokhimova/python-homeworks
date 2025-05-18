def get_last_element(tpl):
    if tpl:
        return tpl[-1]
    else:
        return None  
print(get_last_element((10, 20, 30)))  
print(get_last_element(()))             
