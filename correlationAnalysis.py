# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats

# Load & display dataset
df = pd.read_excel('/Users/alizasamad/downloads/Externships/Webacy/compiled_risk_data.xlsx', sheet_name="Data")
pd.set_option('display.max_columns', 5)
print(df.head())

# Define Phi Coefficient calculator for two binary variables
def phi_coefficient(x,y):
    contingency_table = pd.crosstab(x,y)
    chi2 = scipy.stats.chi2_contingency(contingency_table, correction = False)[0]
    n = np.sum(np.sum(contingency_table, axis=0))
    phi = np.sqrt(chi2 / n)
    return phi

# Test Coefficient
phi = phi_coefficient(df['Is_honeypot'], df['anti_whale_modifiable'])
print(f'Phi Coefficient between "Is_honeypot" and "anti_whale_modifiable": {phi}')

# Calculate phi coefficient for all columns
risk_columns = ['Is_closed_source', 'hidden_owner', 'anti_whale_modifiable',
       'Is_anti_whale', 'Is_honeypot', 'buy_tax', 'sell_tax',
       'slippage_modifiable', 'Is_blacklisted', 'can_take_back_ownership',
       'owner_change_balance', 'is_airdrop_scam', 'selfdestruct', 'trust_list',
       'is_whitelisted', 'is_fake_token', 'illegal_unicode', 'exploitation',
       'bad_contract', 'reusing_state_variable', 'encode_packed_collision',
       'encode_packed_parameters', 'centralized_risk_medium',
       'centralized_risk_high', 'centralized_risk_low', 'event_setter',
       'external_dependencies', 'immutable_states',
       'reentrancy_without_eth_transfer', 'incorrect_inheritance_order',
       'shadowing_local', 'events_maths']

risk_df = df[risk_columns]
phi_matrix = pd.DataFrame(index=risk_df.columns, columns=risk_df.columns)  # create DF to store Phi coefficients

# calculate Phi coeffiecent for each pair of binary variables
for var1 in risk_df.columns:  
    for var2 in risk_df.columns:
        phi_matrix.loc[var1,var2] = phi_coefficient(risk_df[var1], risk_df[var2])

print("Phi Coefficients calculated for all pairs of variables")

# Store Data Frame as a CSV
file_name = "correlationAnalysis.csv"
phi_matrix.to_csv(file_name, encoding='utf-8', index=True, header=True)
print('CSV stored successfully!')

# Creating heatmap visualization
plt.figure(figsize=(12,10))
sns.heatmap(phi_matrix.astype(float), annot=False, fmt = ' .2f', cmap = 'BuPu', vmin=0, vmax = 1)
plt.title('Heatmap of Phi Coefficients Between Risk Tags')
plt.show()
