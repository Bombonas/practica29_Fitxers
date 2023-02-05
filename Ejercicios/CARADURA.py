def ord_dict(dic):
    list_clau = list(dic.keys())
    for pasada in range(len(list_clau) - 1):
        lista_ordenada = True
        for i in range(len(list_clau) - 1 - pasada):
            if dic[list_clau[i]]["company"] > dic[list_clau[i + 1]]["company"]:
                lista_ordenada = False
                aux = list_clau[i]
                list_clau[i] = list_clau[i + 1]
                list_clau[i + 1] = aux
        if lista_ordenada:
            break
    return list_clau

def save_in_dictionary(file, dic):
    f = open(file, "r")
    lines = f.readlines()
    for line in lines:
        values = line.split(" | ")
        dic_aux = {"company": values[1], "direction": values[2], "city": values[3][:-1]}
        dic.update({values[0]: dic_aux})



dict_total = {}
save_in_dictionary("Cara.txt", dict_total)
save_in_dictionary("Dura.txt", dict_total)
print(dict_total["BVBEV"])
print(ord_dict(dict_total))