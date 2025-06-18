# src/config.py
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import (
    KFold, StratifiedKFold, ShuffleSplit
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
    "shuffle": ShuffleSplit(n_splits=5)
}

HYPERPARAMETERS = {
    "random_forest": {
        "model__n_estimators": [50, 100, 200],
        "model__max_depth": [None, 10, 20],
        "model__min_samples_split": [2, 5, 10]
    },
    "decision_tree": {
        "model__max_depth": [None, 10, 20],
        "model__min_samples_split": [2, 5, 10]
    },
    "svm": {
        "model__C": [0.1, 1, 10],
        "model__penalty": ["l2"],
        "model__loss": ["hinge", "squared_hinge"]
    },
    "knn": {
        "model__n_neighbors": [5, 10, 20],
        "model__weights": ["uniform", "distance"]
    }
}