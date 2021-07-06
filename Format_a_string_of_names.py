def namelist(names):
    res = [i['name'] for i in names]
    if len(res) == 2:
        return f'{res[0]} & {res[1]}'
    elif len(res) >= 2:
        return f'{", ".join(res[:len(res) - 2])}, {res[-2]} & {res[-1]}'
    else:
        return "".join(res)









print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge')
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))