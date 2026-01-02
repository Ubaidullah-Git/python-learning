def filter_list(l):
    return list(filter(lambda x: isinstance(x,int), l))

result = ["abc", 1 , 34 ,'happy', 46]
print(filter_list(result))
