try:
    f=open("text.txt","w")
    print("find")
except FileExistsError:
    print("file is missing")
finally:
    print("done")
