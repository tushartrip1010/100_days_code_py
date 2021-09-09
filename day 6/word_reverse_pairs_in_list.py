def word(tl):
    c=0
    rev=[]
    for word in tl:
        if word[::-1] in tl:
            tl.remove(word[::-1])
            tl.remove(word)
            c+=1
    return c
Given_list = ["skeeg", "best", "tseb",
              "for", "skeeg", "skeeg", "best", "geeks", "tseb","abbbb","abbbb","abbbb","abbbb"]
print(word(Given_list))
