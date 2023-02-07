def ord_dict(dic):
    list_clau = list(dic.keys())
    for pasada in range(len(list_clau) - 1):
        lista_ordenada = True
        for i in range(len(list_clau) - 1 - pasada):
            if dic[list_clau[i]]["company"].lower() > dic[list_clau[i + 1]]["company"].lower():
                lista_ordenada = False
                aux = list_clau[i]
                list_clau[i] = list_clau[i + 1]
                list_clau[i + 1] = aux
        if lista_ordenada:
            break
    return list_clau

def save_data(file, dic, list):
    f = open(file, "w")
    for id in list:
        txt = id + dic[id]["company"]+ dic[id]["direction"] + dic[id]["city"] + "\n"
        f.write(txt)
    f.close()
def load_data(file, dic):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        dic_aux = {"company": line[6:37], "direction": line[37:68], "city": line[68:-1]}
        dic.update({line[:6]: dic_aux})

dict_total = {}
load_data("Cara.txt", dict_total)
load_data("Dura.txt", dict_total)
list_ord = ord_dict(dict_total)
save_data("clients.txt", dict_total, list_ord)

