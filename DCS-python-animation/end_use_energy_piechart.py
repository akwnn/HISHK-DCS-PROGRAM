from sjvisualizer import PieRace
from sjvisualizer import DataHandler
from sjvisualizer import Canvas

#define name of excel file
energy_data = "excel_files/energy_consumption_hk.xlsx"

df = DataHandler.DataHandler(excel_file=energy_data, number_of_frames=400).df

#canvas is the area we store the graph in
canvas = Canvas.canvas()

pie_race = PieRace.pie_plot(canvas=canvas.canvas, df=df)
canvas.add_sub_plot(pie_race)
canvas.add_title("Total Energy Consumption by End-use 最終用途")
canvas.add_time(df=df, time_indicator="year")

canvas.play()
