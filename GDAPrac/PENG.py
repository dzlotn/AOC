import seaborn as sns
import pandas as pd
from statsmodels.formula.api import ols

# Load dataset
penguins = sns.load_dataset("penguins")
print("Hello")
# Examine first 5 rows of dataset
print(penguins.head())
# Keep Adelie and Gentoo penguins, drop missing values
penguins_sub = penguins[penguins["species"] != "Chinstrap"]
penguins_final = penguins_sub.dropna()
penguins_final.reset_index(inplace=True, drop=True)
# Create pairwise scatterplots of data set
sns.pairplot(penguins_final)
sns.show()
# Subset Data
ols_data = penguins_final[["bill_length_mm", "body_mass_g"]]
# Write out formula
ols_formula = "body_mass_g ~ bill_length_mm"
# Import ols function

# Build OLS, fit model to data
OLS = ols(formula = ols_formula, data = ols_data)
model = OLS.fit()

#checking homostedacicity
# Import matplotlib
import matplotlib.pyplot as plt
fig = sns.scatterplot(x=fitted_values, y=residuals)

# Add reference line at residuals = 0
fig.axhline(0)

# Set x-axis and y-axis labels
fig.set_xlabel("Fitted Values")
fig.set_ylabel("Residuals")

# Show the plot
plt.show()