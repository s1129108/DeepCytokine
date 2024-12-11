from sklearn.utils import shuffle
import os
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import gc

datalabel="cytokine_receptor"

def data_label():
    return datalabel

def MCNN_data_load(DATA_TYPE,MAXSEQ):
    # Update your paths
    path_m_testing = "C:/jupyter/globe/deepcytokine/dataset/numpy/membrane/test.npy"
    path_m_training = "C:/jupyter/globe/deepcytokine/dataset/numpy/membrane/train.npy"

    path_v_testing = "C:/jupyter/globe/deepcytokine/dataset/numpy/cytokine/test.npy"
    path_v_training = "C:/jupyter/globe/deepcytokine/dataset/numpy/cytokine/train.npy"
   
    
    x_train,y_train=data_load(path_v_training,path_m_training)
    x_test,y_test=data_load(path_v_testing,path_m_testing)
    return(x_train,y_train,x_test,y_test)

def data_load(p_folder,n_folder):
    p=np.load(p_folder)
    n=np.load(n_folder)
    print(p.shape)
    print(n.shape)
    label_p = np.ones(p.shape[0])
    label_n = np.zeros(n.shape[0])
        
    print(label_p.shape)
    print(label_n.shape)
    
    x=np.concatenate([p, n], axis=0)
    y=np.concatenate([label_p, label_n], axis=0)
    y= tf.keras.utils.to_categorical(y,2)
    #y.dtype='float16'
    gc.collect()
    return x, y 
