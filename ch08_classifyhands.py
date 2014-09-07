import glob
import os
import numpy

import knn
import sift

"""Run after ch08_preparedata.py has run."""

def read_gesture_feature_labels(path):
  featlist = glob.glob(os.path.join(path, '*.dsift'))
  features = [sift.read_features_from_file(f)[1].flatten() for f in featlist]
  labels = [os.path.basename(f)[0] for f in featlist]
  return numpy.array(features), numpy.array(labels)


features, labels = read_gesture_feature_labels('out_hands/train')
test_features, test_labels = read_gesture_feature_labels('out_hands/test')

classnames = numpy.unique(labels)

# Test kNN.
k = 1
knn_classifier = knn.KnnClassifier(labels, features)

res = numpy.array([knn_classifier.classify(feat, k) for feat in test_features])
acc = numpy.sum(1.0 * (res == test_labels)) / len(test_labels)
print 'Accuracy:', acc