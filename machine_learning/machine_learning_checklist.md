 Checklist:
- [ ] Shuffle rows with pandas sample (frac=1). train_test_split(X,y, shuffle=True) may also work but check.
- [ ] Remove wrong columns (ID, outcome variable) that are not features. 
- [ ] Check column variable types with df.info(verbose=1). 
- [ ] Make sure all metric variables are float or int (whatever they should be). 
- [ ] Dummy code categorical features. Remove redundant columns (male, if female is just the inverse). Columns with little variance (if value "other" existed in 4% of the cases, patterns associated to this value might not be learnable by most machine learning models, doesn't hurt to leave it in though). 
- [ ] Feature extraction 
If you're final results is k-fold then you have to use nested k-fold for hyperparameter tuning
Use a proper scoring argument for hyperparameter tuning depending on if it is a classification or regression task and what exactly you're trying to optimize: https://scikit-learn.org/stable/modules/model_evaluation.html
Longitudinal data or other repeated measures → group shuffle split 
Don't preprocess on the entire dataset if it the method uses all rows:
normalizing (standard scaler, min max)
Feature extraction (e.g., mean, SD, PCA)
Feature selection
Selecting subjects that perform high or low on some dependent variable. 
It's okay to remove some corrupted samples, replace values in a row (dummy coding) and things that don't use all rows to inform the values 
Use the same random_state for cross-validation or bootstrapping across different models so they all use the same test-sets.
Add tests to your code:
assert y_df.name == dependent_var_name  # should be True
Good to add as many of those tests as you can (e.g., a function or operation should return a certain value given a certain input)
Consider saving the model for perfect reproducibility: 
import pickle
with open('model_name.pkl', 'wb') as file:
    pickle.dump(trained_model, file)
with open('model_name.pkl', 'rb') as file:
    trained_model = pickle.load(file)
