import numpy as np
import h5py
    
    
def load_dataset():
    train_dataset = h5py.File('https://drive.google.com/file/d/1rA_FRXc_MwS1uGBaBJ-mqMXPvirhr3PP/view?usp=sharing')
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('https://drive.google.com/file/d/1Y5ixdMYl2bMia6eQ6zoNG8m2hW5Nhhcb/view?usp=sharing')
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
