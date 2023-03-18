def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)

    return (mins + '.' +secs)

def get_coachData(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return ( { 'Names' : temp.pop(0),
                   'DOB' : temp.pop(0),
                   'Times' : str(sorted(set([sanitize(t) for t in temp]))[0:3])})
    except IOError as ioErr:
        print("File Error", ioErr)
        return(None)

james = get_coachData('C:/python3.8/Practice/james.txt')
julie = get_coachData("C:/python3.8/Practice/julie.txt")
mikey = get_coachData("C:/python3.8/Practice/mikey.txt")
sarah = get_coachData("C:/python3.8/Practice/sarah.txt")

print(james['Names'] + "'s fastest times are: " +james['Times'])
print(julie['Names'] + "'s fastest times are: " +julie['Times'])
print(mikey['Names'] + "'s fastest times are: " +mikey['Times'])
print(sarah['Names'] + "'s fastest times are: " +sarah['Times'])


