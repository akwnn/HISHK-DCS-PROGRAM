from sjvisualizer import DataHandler, Canvas, BarRace

#load data into dataframe
japan_data = "excel_files/Japan_DCS.xlsx"
FPS = 60
DURATION = 0.5

#load data into dataframe
df= DataHandler.DataHandler(excel_file=japan_data, number_of_frames=FPS*DURATION*60).df

#creating the canvas
canvas = Canvas.canvas()

#adding the bar chart
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas, width= 400, height=300, x_pos= 500, y_pos=400)
canvas.add_sub_plot(bar_chart)

#customising
canvas.add_title("Japan's Growth in Building DCS")
canvas.add_sub_title("From 1972-2017")
canvas.add_time(df=df, time_indicator= 'year')
canvas.add_logo(logo='assets/japan.png')

canvas.play(fps=FPS)


