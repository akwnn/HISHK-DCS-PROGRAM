from sjvisualizer import DataHandler, Canvas, BarRace

#load data into dataframe

co2_data = "excel_files/carbon_emissions.xlsx"
FPS = 60
DURATION = 0.5

#load data into dataframe
df= DataHandler.DataHandler(excel_file=co2_data, number_of_frames=FPS*DURATION*60).df

#creating the canvas
canvas = Canvas.canvas()

#adding the bar chart
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas, width= 400, height=300, x_pos= 500, y_pos=400)
canvas.add_sub_plot(bar_chart)

#customising
canvas.add_title("Carbon Emissions")
canvas.add_sub_title("From 1990-2020")
canvas.add_time(df=df, time_indicator= 'year')
canvas.add_logo(logo='assets/hk.png')

canvas.play(fps=FPS)