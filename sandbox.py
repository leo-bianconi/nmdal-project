import pandas as pd
import numpy as np
import time
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials, STATUS_FAIL
import hyperopt
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import matplotlib.pyplot as plt
import random

# TPOT
from tpot import TPOTClassifier

import sdv

df = pd.read_csv('dataset_alarms_anonymized.csv')

def process_alarms_bi(df):
    alarm_columns = [col for col in df.columns if col.startswith('alarm')]
    for col in alarm_columns:
        df[col] = df[col].apply(lambda x: 1 if x > 0 else 0)
    return df

def process_alarms_cat(df):
    alarm_columns = [col for col in df.columns if col.startswith('alarm')]
    for col in alarm_columns:
        df[col] = df[col].apply(lambda x: 1 if 0 < x <= 45 else (2 if 45 < x <= 450 else (3 if x > 450 else 0)))
    return df

df_processed = process_alarms_bi(df)
df_processed_cat = process_alarms_cat(df)
df_unprocessed = pd.read_csv('dataset_alarms_anonymized.csv')


X_bin, y_bin = df_processed.drop('label', axis=1).to_numpy(), df_processed['label'].to_numpy()
X_cat, y_cat = df_processed_cat.drop('label', axis=1).to_numpy(), df_processed_cat['label'].to_numpy()
X_unproc, y_unproc = df_unprocessed.drop('label', axis=1).to_numpy(), df_unprocessed['label'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X_unproc, y_unproc, test_size=0.2)

# Print majority class baseline
print('Majority class baseline:', max(np.mean(y_test == 0), np.mean(y_test == 1), np.mean(y_test == 2), np.mean(y_test == 3)))
