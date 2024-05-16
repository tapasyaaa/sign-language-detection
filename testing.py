from training_model import *
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
score = accuracy_score(y_predict, y_test)
print(classification_report(y_test, y_predict))
print('{}% of samples were classified correctly !'.format(score * 100))