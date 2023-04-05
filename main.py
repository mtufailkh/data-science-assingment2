import pandas as pd
import graphs


def read_data_world(filename):
    df = pd.read_csv(filename, skiprows=4)
    
    # transpose
    df_year = df.set_index('Country Name').T
    # clean up column headers
    df_year.columns.name = ''
    # transpose
    df_country = df_year.T
    df_country.columns.name = 'Country Name'
    # clean up
    df_year.fillna('', inplace=True)
    df_country.fillna('', inplace=True)
    # return
    return df_country, df_year

df_country, df_year = read_data_world('development.csv')

# print data
print(df_country,df_year)


# Read data
df = pd.read_csv('development.csv', skiprows=4)
# clean data
df.fillna('', inplace=True)

# Countries of interest
countries_array = ['China','France','India','Nigeria','South Africa','Romania','United Kingdom','United States']


# Indicators of interest
indicators_array = ['Rural population (% of total population)', 'Forest area (% of land area)','Arable land (% of land area)','Rural population growth (annual %)', 'Agricultural nitrous oxide emissions (% of total)', 'Access to electricity, rural (% of rural population)']


# Subset the data
df_sub = df[(df['Country Name'].isin(countries_array)) & (df['Indicator Name'].isin(indicators_array))]

# Calculate statistics with describe
stats = df_sub.groupby(['Country Name', 'Indicator Name']).describe()

# Print the statistics
print(stats)

# get years
year = [col for col in df_sub.columns if col.isdigit()]

# graphs
graphs.bar_graph(df_sub, year, 'Rural population (% of total population)', 'Country Name', '')
graphs.bar_graph(df_sub, year, 'Agricultural nitrous oxide emissions (% of total)', 'Country Name', '')
graphs.heatmap(df_sub, 'China', indicators_array,'BrBG')
graphs.heatmap(df_sub, 'South Africa', indicators_array,'crest')
