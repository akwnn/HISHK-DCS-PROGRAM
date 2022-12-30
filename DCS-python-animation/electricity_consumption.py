import pandas as pd
import plotly.express as px 
import plotly 

# Read Data From Excel and store in a variable df [dataframe]
df = pd.read_excel('excel_files/electricity_consum.xlsx')

# Store each coloumn in a seperate variable
power = df['Electricity Consumption (MJ)']
type = df['Type']
date = df['Date'].dt.strftime('%Y-%m-%d')

# Creating Bar Chart and store it as fig
fig = px.bar(
    df,
    x= type,
    y= power,
    color = type,
    animation_frame= date,
    animation_group= type,
    range_y= [0, 200]
    
            )   

# Save
plotly.offline.plot(fig, filename = 'electricity_consum.html')
