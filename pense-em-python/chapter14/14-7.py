import pickle

t1 = [1,2,3]

print(pickle.dumps(t1))
s = pickle.dumps(t1)
t2 = pickle.loads(s)

print(s)
print(t2)
