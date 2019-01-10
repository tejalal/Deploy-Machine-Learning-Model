import numpy as np
import pickle

model = pickle.load(open('model.pk', 'rb'))

x = np.array([5.4,3.2,5.4,2.8])
x=x.reshape(1,4)

p=model.predict(x)

print("Input Sample: ", x)
print("Predicted Class:", p)


