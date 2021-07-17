import matplotlib.colors as colors

def check_color(r, g, b):
    rgb_list = []
    for i in (r, g, b):
        if i < 0:
            rgb_list.append(0)
        elif i > 255:
            rgb_list.append(255)
        else:
            rgb_list.append(i)
    return tuple(rgb_list)

def rgb(r, g, b):
    rgb_tuple = check_color(r, g, b)  
    return (colors.rgb2hex([1.0*x/255 for x in rgb_tuple]).upper())[1:]



print(rgb(0,0,0),"000000", "testing zero values")
print(rgb(1,2,3),"010203", "testing near zero values")
print(rgb(255,255,255), "FFFFFF", "testing max values")
print(rgb(254,253,252), "FEFDFC", "testing near max values")
print(rgb(-20,275,125), "00FF7D", "testing out of range values")