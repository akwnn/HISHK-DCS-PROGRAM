import pandas as pd
import plotly.express as px 
import plotly 

# Read Data From Excel and store in a variable df [dataframe]
df = pd.read_excel('excel_files/district_temp.xlsx')

# Store each coloumn in a seperate variable
district = df['District']
temperature = df['Temperature (°C)']
date = df['Date'].dt.strftime('%Y-%m-%d')

# Creating Bar Chart and store it as fig
fig = px.bar(
    df,
    x= district,
    y= temperature,
    color = district,
    animation_frame= date,
    animation_group= district,
    range_y= [0, 40]
    
            )   

# Save
plotly.offline.plot(fig, filename = 'district_temp.html')
