import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# TODO: Modify this list to include the numerical columns
NUMERICAL_VARS = ['pclass', 'age', 'sibsp', 'parch', 'fare']

# Crear custom transformer



class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        return self

    def transform(self, X):
        # TODO: Put your code here
        X = X.copy()
        for var in self.variables:
            X[var + '_nan'] = pd.isnull(X[var]).astype(int)
        return X




# Leer el csv sin aplicar transformaciones
df = pd.read_csv('C:\Users\Edgar F\Desktop\itesm_mlops_S6\activity/raw-data.csv')



# Imprimir los primeros datos
print(df.head(10))

mi = MissingIndicator(variables=NUMERICAL_VARS)
# Aplicar las transformaciones
df_mi = mi.transform(df)

# Imprimir resultados despues de las transformaciones
print(df_mi.head(20))
