import pandas as pd
import ast
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
import matplotlib.gridspec as gridspec

pd.set_option('display.width', 1000)  
pd.set_option('display.max_colwidth', 200) 
IMAGES_PATH_TO_SAVE = '../images/'

TITLE_SIZE=20
XTICKS_SIZE=14

def evaluate_score(list_to_fill, model_name, model, y_pred, y_test, X_test, best_params:dict, plots: bool = True, filename:str=''):    
    list_to_fill.append({
        model_name: {
            "accuracy": metrics.accuracy_score(y_test, y_pred),
            "precision": metrics.precision_score(y_test, y_pred),
            "recall": metrics.recall_score(y_test, y_pred),
            "f1": metrics.f1_score(y_test, y_pred),
            "auc_roc": metrics.roc_auc_score(y_test, y_pred),
            "log_loss": metrics.log_loss(y_test, y_pred),
            "best_params": best_params
        }
    })

    if plots:
        show_plots(y_test, y_pred, X_test, model, filename)
    

def show_plots(y_test, y_pred, X_test, model, filename=''):
    confusion_matrix = metrics.confusion_matrix(y_test, y_pred, labels=[1, 0])
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=['attack', 'normal'])
    
    try:
        predicted_probs = model.predict_proba(X_test)[:, 1]
    except AttributeError: 
        predicted_probs = y_pred
    
    precision, recall, thresholds = metrics.precision_recall_curve(y_test, predicted_probs)
    ap = metrics.average_precision_score(y_test, predicted_probs)
    
    fig = plt.figure(figsize=(16, 8))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])
    
    ax_cm = plt.subplot(gs[0])
    ax_cm.grid(False)
    cm_display.plot(ax=ax_cm, cmap='Blues')
    ax_cm.set_title("Confusion Matrix", fontsize=TITLE_SIZE)
    ax_cm.set_xlabel("True label" , fontsize=XTICKS_SIZE)
    ax_cm.set_ylabel("Predicted label", fontsize=XTICKS_SIZE)
    ax_cm.tick_params(axis='both', which='major', labelsize=XTICKS_SIZE)

    for text in ax_cm.texts:  
        text.set_fontsize(XTICKS_SIZE) 
    
    ax_pr = plt.subplot(gs[1])
    ax_pr.plot(recall, precision, label=f'AP = {ap:.2f}')
    ax_pr.set_title("Precision-Recall Curve", fontsize=TITLE_SIZE)
    ax_pr.set_xlabel("Recall" , fontsize=XTICKS_SIZE)
    ax_pr.set_ylabel("Precision", fontsize=XTICKS_SIZE)
    ax_pr.legend()
    plt.tight_layout()

    if filename != '':
        plt.savefig(IMAGES_PATH_TO_SAVE + filename, bbox_inches="tight")
    plt.show()

def display_all_trees_metrics(trees_metrics_df, all_trees, filename):
    fig, ax = plt.subplots(figsize=(10, 12))
    
    num_models = len(trees_metrics_df.index)
    num_metrics = len(trees_metrics_df.columns)  
    bar_height = 0.15
    spacing = 0.5 

    y = np.arange(num_models) * (num_metrics * bar_height + spacing) 

    min_value = 0.75  
    max_value = 1
    ax.set_xlim(min_value, max_value)
    
    ax.barh(y - 2 * bar_height, trees_metrics_df["accuracy"], color='g', height=bar_height, label="Accuracy")
    ax.barh(y - bar_height, trees_metrics_df["f1"], color='b', height=bar_height, label="F1")
    ax.barh(y, trees_metrics_df["auc_roc"], color='r', height=bar_height, label="AUC-ROC")
    ax.barh(y + bar_height, trees_metrics_df["precision"], color='y', height=bar_height, label="Precision")
    ax.barh(y + 2 * bar_height, trees_metrics_df["recall"], color='olive', height=bar_height, label="Recall")

    classifiers = [all_trees.iloc[i] for i in trees_metrics_df.index]
    classifiers_str = []
    for classifier in classifiers:
        params = ast.literal_eval(classifier['best_params'])
        classifiers_str.append(f"cv: {classifier['cv']} \nscaler: {classifier['scaler']} \nmax_depth: {params['model__max_depth']} \nmin_samples_split: {params['model__min_samples_split']}")
    
    ax.legend()
    ax.set_yticks(y)
    ax.set_yticklabels(classifiers_str, fontsize=10)
    plt.xlabel("Metric value", fontsize=12)
    plt.title("Model Performance Metrics", fontsize=14)
    
    if filename:
        plt.savefig(IMAGES_PATH_TO_SAVE + filename, bbox_inches="tight")
    
    plt.show()
