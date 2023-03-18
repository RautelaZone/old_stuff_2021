'''
Falsy words like False,0,None etc
Input:  [10,20,30,0,False,40,0]
Output:  [10,20,30,40]

Input: [False,None,1,2,3,"Geeks"]
Output: [1,2,3,"Geeks"]

Input: [[],(),"Concepts&LearningConcepts&Programs",26,27]
Output: ["Concepts&LearningConcepts&Programs",26,27]
'''

def Remove_Falsy(List):
    newList = []
    for item in List:
        if(bool(item)):
            newList.append(item)
    return newList

List = [10, 20, 30, 0, False, 40, 0]
print("List after Removing Flasy values:", Remove_Falsy(List))


#Using Filter
def Remove_Falsy(List):
    return list(filter(bool,List))

List = [ [], (), "Concepts ", 26, 27]
print("List after Removing Flasy values:", Remove_Falsy(List))

