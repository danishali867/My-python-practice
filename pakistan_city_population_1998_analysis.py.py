# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Set the theme
# sns.set_theme(style="darkgrid", color_codes=True)

# # Load the data
# data = pd.read_csv("Major.csv")
# print(data.columns)
# # Alternative plot showing population trends
# plt.figure(figsize=(12, 8))
# sns.lineplot(
#     data=data.melt(id_vars=[ 'ProvinceRank'], 
#                   value_vars=['City','Population 1998 Census', 'Change'],
#                   var_name='ProvinceRank',
#                   value_name='City'),
#     x='City',
#     y='Population 1998 census',
#     hue='area',
#     style='Change'
# )
# plt.title('Population Trends by Country and Area')
# plt.ylabel('Population 1998 census')
# plt.xticks(rotation=45)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.show()



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
data = pd.read_csv("Major.csv")

# Set theme
sns.set_theme(style="darkgrid", color_codes=True)

# Melt the data
melted_data = data.melt(
    id_vars=['Province'],  # Use actual column
    value_vars=['Population 1998 Census', 'Change'],
    var_name='Data_Type',
    value_name='Value'
)

# Plotting
plt.figure(figsize=(14, 8))
sns.barplot(
    data=melted_data,
    x='Province',
    y='Value',
    hue='Data_Type'
)
plt.title('City Population and Change (1998) by Province')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
