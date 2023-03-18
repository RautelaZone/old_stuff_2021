import pickle

try:
    with open('C:/python3.8/Practice/mydata.pickle', 'wb') as mysavedata:
        pickle.dump([1, 2, 'three'], mysavedata)

    with open('C:/python3.8/Practice/mydata.pickle', 'rb') as myrestoredata:
        a_list = pickle.load(myrestoredata)
        print(a_list)

except IOError as err:
    print("File error:",err)

except pickle.PickleError as perr:
    print("Pickling Error:",perr)