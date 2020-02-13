# This script is used to generate pickle file from Udacity car simulator.
# It will allow me to reuse dataset easier.

# Change LOG_PATH and IMG_PATH to generate new file
import pickle
from FLAGS import *
from DataSet import DataSet

LOG_PATH = '../bag/driving_log.csv'
IMG_PATH = '../bag/imgs/'
FILE_NAME = '../data.p'

data = DataSet(LOG_PATH, IMG_PATH, sequence=TIME_STEPS)

features, labels = data.build_train_data()
pickle.dump({'features': features, 'labels': labels}, open(FILE_NAME, 'wb'))
