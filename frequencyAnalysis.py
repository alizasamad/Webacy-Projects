#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load & display dataset
df = pd.read_excel('/Users/alizasamad/downloads/Externships/Webacy/compiled_risk_data.xlsx', sheet_name="Data")
pd.set_option('display.max_columns', 5)
print(df.head())

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





# risk tag frequency (TRUE)
freq = df[risk_columns].apply(lambda x: x.value_counts()).loc[True]
freq = freq.fillna(0)
print("Frequency of Risk Tags with True Value")
print(freq)
print('\n')

# risk tag frequency (FALSE)
print("Frequency of Risk Tags with False Value")
freqF = df[risk_columns].apply(lambda x:x.value_counts()).loc[False]
freqF = freqF.fillna(0)
print(freqF)
print('\n')

# initialize subplot function
fig, axes = plt.subplots(1,2,figsize=(12,8))

# create visualization of frequencies (TRUE)
sns.set_style('whitegrid')
sns.barplot(x=freq.index, y=freq.values, hue = freq.index, legend = False, palette = 'flare', ax=axes[0])
axes[0].set_title('Frequency of True Values for Each Risk Tag')
axes[0].set_xlabel('Risk Tags')
axes[0].set_ylabel('Frequency of True')
axes[0].tick_params(axis = 'x', rotation=90)

# create visualization of frequencies (FALSE)
sns.set_style('whitegrid')
sns.barplot(x=freqF.index, y=freqF.values, hue = freqF.index, legend = False, palette = 'mako', ax=axes[1])
axes[1].set_title('Frequency of False Values for Each Risk Tag')
axes[1].set_xlabel('Risk Tags')
axes[1].set_ylabel('Frequency of False')
axes[1].tick_params(axis = 'x', rotation=90)





# Ethereum
eth_df = df[df["Chain"] == "Ethereum"]
freqE = eth_df[risk_columns].apply(lambda x:x.value_counts()).loc[True]
print("Frequency of Risk Tags with True Value in Ethereum")
print(freqE)
print('\n')

# Arbitrum
arb_df = df[df["Chain"] == "Arbitrum"]
freqA = arb_df[risk_columns].apply(lambda x:x.value_counts()).loc[True]
print("Frequency of Risk Tags with True Value in Arbitrum")
print(freqA)
print('\n')

# Optimism
opt_df = df[df["Chain"] == "Optimism"]
freqO = opt_df[risk_columns].apply(lambda x:x.value_counts()).loc[True]
print("Frequency of Risk Tags with True Value in Optimism")
print(freqO)
print('\n')

# Polygon
pol_df = df[df["Chain"] == "Polygon"]
freqP = pol_df[risk_columns].apply(lambda x:x.value_counts()).loc[1]
print("Frequency of Risk Tags with True Value in Polygon")
print(freqP)
print('\n')

# initalize subplot function
figs, ax = plt.subplots(2,2, figsize=(12,8))

# create Ether visualization
sns.set_style('whitegrid')
sns.barplot(x=freqE.index, y=freqE.values, hue=freqE.index, legend = False, palette = "viridis", ax=ax[0,0])
ax[0,0].set_title('Risk Tag Frequency in Ethereum')
ax[0,0].set_xlabel(None)
ax[0,0].set_ylabel('Frequency')
ax[0,0].tick_params(axis = 'x', rotation=90, labelsize=8)

# create Arb visualization
sns.set_style('whitegrid')
sns.barplot(x=freqA.index, y=freqA.values, hue=freqA.index, legend = False, palette = "viridis", ax=ax[0,1])
ax[0,1].set_title('Risk Tag Frequency in Arbitrum')
ax[0,1].set_xlabel(None)
ax[0,1].set_ylabel('Frequency')
ax[0,1].tick_params(axis = 'x', rotation=90, labelsize=8)

# create Opt visualization
sns.set_style('whitegrid')
sns.barplot(x=freqO.index, y=freqO.values, hue=freqO.index, legend = False, palette = "viridis", ax=ax[1,0])
ax[1,0].set_title('Risk Tag Frequency in Optimism')
ax[1,0].set_xlabel(None)
ax[1,0].set_ylabel('Frequency')
ax[1,0].tick_params(axis = 'x', rotation=90, labelsize=8)

# create Poly visualization
sns.set_style('whitegrid')
sns.barplot(x=freqP.index, y=freqP.values, hue=freqP.index, legend = False, palette = "viridis", ax=ax[1,1])
ax[1,1].set_title('Risk Tag Frequency in Polygon')
ax[1,1].set_xlabel(None)
ax[1,1].set_ylabel('Frequency')
ax[1,1].tick_params(axis = 'x', rotation=90, labelsize=8)




# display figures
plt.tight_layout()
plt.show()
