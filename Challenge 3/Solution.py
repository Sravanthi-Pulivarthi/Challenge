def extract(objects, keys):
    l = keys.split('/')
    print(l)
    temp = objects
    for a in l :
        temp = temp[temp.find(a)+len(a)+2:-1]
    out = temp[1:-1]
    print(out)


def main():
    objects = input("enter objects: ")
    keys = input("enter keys: ")
    extract(objects,keys)


if __name__=="__main__":
    main()
