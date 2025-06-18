import pandas as pd

def get_path(purpose: str, target: str = 'train', raw: bool = False):
    if purpose not in ['eda', 'modelling']:
        raise ValueError(f'Invalid purpose: {purpose}')
    
    if target not in ['train', 'test']:
        raise ValueError(f'Invalid target: {target}')

    file_name = 'KDD' + target.capitalize() + ('+' if raw else '') +  '.csv'

    if raw:
        return f"../data/raw/{target}/{file_name}"

    return f"../data/processed/{purpose}/{file_name}" 


def load_test_dataset(purpose: str = 'eda', raw: bool = False, split: bool = False):
    return load_dataset(purpose=purpose, raw=raw, split=split, target='test')

def load_train_dataset(purpose: str = 'eda', raw: bool = False, split: bool = False):
    return load_dataset(purpose=purpose, raw=raw, split=split, target='train')

def load_dataset(purpose: str = 'eda', split: bool = False, raw=False, target: str = 'train'):
    path = get_path(purpose=purpose, target=target, raw=raw)
    df = pd.read_csv(path)
    if split:
        X, y = df.drop(columns=["class"]), df["class"]
        return X, y
    
    return df
    

def store_dataset(df: pd.DataFrame, target: str, purpose: str = 'modelling'):
    path = get_path(purpose=purpose, raw=False, target=target)
    df.to_csv(path, index=False)