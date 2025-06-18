# src/config.py
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import (
    KFold, StratifiedKFold, TimeSeriesSplit, ShuffleSplit
)

SCALERS = {
    "standard": StandardScaler(),
    "minmax": MinMaxScaler(),
    "robust": RobustScaler()
}

MODELS = {
    "random_forest": RandomForestClassifier(),
    "decision_tree": DecisionTreeClassifier(),
    "svm": LinearSVC(),
    "knn": KNeighborsClassifier(n_neighbors=20)
}

CV_METHODS = {
    "kfold": KFold(n_splits=5),
    "stratified_kfold": StratifiedKFold(n_splits=5),
    "timeseries": TimeSeriesSplit(n_splits=5),
    "shuffle": ShuffleSplit(n_splits=5)
}