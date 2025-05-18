def get_first_element(tpl):
    if tpl:
        return tpl[0]
    else:
        return None  

print(get_first_element((10, 20, 30)))  
print(get_first_element(()))             #
