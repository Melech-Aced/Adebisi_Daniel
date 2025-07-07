
fruit_list=["apple","banana","cherry","eggplant","dates","fig","guava","hawthorn","hazelnut","imbe","juggernut"]
#print(fruit_list.sort())
#print(fruit_list.sort(reverse=True,))
print(fruit_list.sort())


print("what are you looking for?")
search = input()
if search in fruit_list:
    print(f"Yes we have {search}")
    print(fruit_list.index("apple"))
else:
    print("This shrrrr ain't here man")
    fruit_list.append(search)
    print(fruit_list,"it should be added now")
