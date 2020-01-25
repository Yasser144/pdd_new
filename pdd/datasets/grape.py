"""MNIST handwritten digits dataset.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ..utils.data_utils import get_file
from ..utils.data_utils import datadir_train_test_split
import numpy as np
import sys


def load_data(path='tomato.zip', 
              split_on_train_test=False, 
              test_size=None, 
              random_state=0):
    """Loads the PDD grape dataset.
    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.pdd/datasets).
        split_on_train_test: flag, controls whether or not
            data should be splitted on train and test
        test_size: the size of test data fraction
    # Returns
        Path to the folder with data or tuple with train and test paths
    """
    path = get_file(path,
                    origin="/content/drive/My Drive/new_test/ttttt/tomato.zip",
                    file_hash='5a4043518ba0071832eb45be2c6a24fb887998fa774636b6e6c50947f1757731',
                                                                                                 
                    extract=True)

    try:
        if split_on_train_test:
            print("Splitting on train and test...")
            test_size = 0.15 if test_size is None else test_size
            train_path, test_path = datadir_train_test_split(
                path, test_size, random_state)
            return (train_path, test_path)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    
    return path


