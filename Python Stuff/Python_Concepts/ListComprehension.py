# List Comprehension is a technique to write your line of codes in single code

# mins = [1, 2, 3]
# sec = [m*60 for m in mins]
# print(sec)

# lower = ["anil", "rautela"]
# upp = [u.upper() for u in lower]
# print(upp)

old_l=["anil","rautela"]
new_l = []
#
# for t in old_l:
#     new_l.append(len(t))

new_l = [len(t) for t in old_l]
print(new_l)