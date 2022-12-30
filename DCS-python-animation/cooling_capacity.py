import pandas as pd
import plotly.express as px 
import plotly 

# Read Data From Excel and store in a variable df [dataframe]
df = pd.read_excel('excel_files/cooling_capacity.xlsx')

# Store each coloumn in a seperate variable
area = df['DCS Project Area']
capacity = df['Cooling Capacity in MW']
date = df['Date'].dt.strftime('%Y-%m-%d')

# Creating Bar Chart and store it as fig
fig = px.bar(
    df,
    x= area,
    y= capacity,
    color = area,
    animation_frame= date,
    animation_group= area,
    range_y= [0, 220]
    
            )   

# Save
plotly.offline.plot(fig, filename = 'area_cooling_capacity.html')