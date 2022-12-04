def extract(objects, keys):
    l = keys.split('/')
    temp = objects
    for a in l :
        temp = temp[temp.find(a)+3:]
    out = temp[1]
    print(out)


def main():
    objects = input("enter objects: ")
    keys = input("enter keys: ")
    extract(objects,keys)


if __name__=="__main__":
    main()
