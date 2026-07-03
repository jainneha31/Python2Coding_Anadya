import tkinter as tk


def calculate():
  start = start_station.get()
  stop = stop_station.get()

  if start in stn_L1:
    start_line = stn_L1
  elif start in stn_L2:
    start_line = stn_L2
  else:
    start_line = stn_L3

  if stop in stn_L1:
    stop_line = stn_L1
  elif stop in stn_L2:
    stop_line = stn_L2
  else:
    stop_line = stn_L3

  if start_line is stop_line:
    n_stops = abs(start_line.index(start) - start_line.index(stop))

  elif (start_line is stn_L1 and stop_line is stn_L2) or (start_line is stn_L2 and stop_line is stn_L1):
    if start_line is stn_L1:
      n_stops = abs(stn_L1.index(start) - stn_L1.index('London'))
      n_stops = n_stops + abs(stn_L2.index('Number 12, Grimmauld Place') - stn_L2.index(stop))
    else:
      n_stops = abs(stn_L2.index(start) - stn_L2.index('Number 12, Grimmauld Place'))
      n_stops = n_stops + abs(stn_L1.index('London') - stn_L1.index(stop))

  elif (start_line is stn_L2 and stop_line is stn_L3) or (start_line is stn_L3 and stop_line is stn_L2):
    if start_line is stn_L2:
      n_stops = abs(stn_L2.index(start) - stn_L2.index("Godric's Hollow"))
      n_stops = n_stops + abs(stn_L3.index('Hogsmeade') - stn_L3.index(stop))
    else:
      n_stops = abs(stn_L3.index(start) - stn_L3.index('Hogsmeade'))
      n_stops = n_stops + abs(stn_L2.index("Godric's Hollow") - stn_L2.index(stop))

  else:
    if start_line is stn_L1:
      n_stops = abs(stn_L1.index(start) - stn_L1.index('London'))
      n_stops = n_stops + abs(stn_L2.index('Number 12, Grimmauld Place') - stn_L2.index("Godric's Hollow"))
      n_stops = n_stops + abs(stn_L3.index('Hogsmeade') - stn_L3.index(stop))
    else:
      n_stops = abs(stn_L3.index(start) - stn_L3.index('Hogsmeade'))
      n_stops = n_stops + abs(stn_L2.index("Godric's Hollow") - stn_L2.index('Number 12, Grimmauld Place'))
      n_stops = n_stops + abs(stn_L1.index('London') - stn_L1.index(stop))

  fare = n_stops * 50
  farelabel.configure(text = 'FARE = K₧ ' + str(fare))

print ('Currency System in Wizarding World of Harry Potter:')
print('Includes Galleons, Sickles, and Knuts but metros only accept Knuts')
print('Knuts or K₧ = 0.02 USD or 0.10 INR')


window = tk.Tk()
window.title("Wizarding Metro Map")
window.configure(bg='DarkGreen')
window.geometry("700x620+10+0")

c = tk.Canvas(window, width=680, height=500)
c.pack()

# Line 1 - horizontal (orange)
stn_L1 = ['Little Whinging', 'Surrey', 'Number 4, Privet Drive', 'London',
           'Cokeworth', 'Wiltshire', 'Malfoy Manor']

x_s = 40
y_s = 170
d_stn = 90
r_stn = 6

for stn in stn_L1:
  if stn != stn_L1[-1]:
    c.create_line(x_s, y_s, x_s + d_stn, y_s, fill='DarkOrange')
  c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='DarkOrange')
  c.create_text(x_s, y_s + 20, text=stn, fill='DarkOrange', font=('Helvetica 6 bold'))
  x_s = x_s + d_stn

# Line 2 - vertical (blue)
stn_L2 = ['Diagon Alley', 'Knockturn Alley', 'Number 12, Grimmauld Place',
           "Godric's Hollow", 'Ottery St Catchpole', 'The Burrow', 'Devon']

x_s = 310
y_s = 40
d_stn = 65
r_stn = 6

for stn in stn_L2:
  if stn != stn_L2[-1]:
    c.create_line(x_s, y_s, x_s, y_s + d_stn, fill='blue')
  c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='blue')
  c.create_text(x_s - 10, y_s, text=stn, fill='blue', font=('Helvetica 6 bold'), anchor='e')
  y_s = y_s + d_stn

# Line 3 - horizontal (green)
stn_L3 = ['Little Hangleton', 'Cornwall', 'Beauxbatons', 'Hogsmeade',
           'Durmstrang', 'Ilvermorny', 'MACUSA Headquarters']

x_s = 40
y_s = 235
d_stn = 90
r_stn = 6

for stn in stn_L3:
  if stn != stn_L3[-1]:
    c.create_line(x_s, y_s, x_s + d_stn, y_s, fill='green')
  c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='green')
  c.create_text(x_s, y_s - 20, text=stn, fill='green', font=('Helvetica 6 bold'))
  x_s = x_s + d_stn

all_stations = stn_L1 + stn_L2 + stn_L3

c.create_text(60, 390, text='Start', fill='white')
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x=30, y=410)

c.create_text(270, 390, text='Stop', fill='white')
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x=240, y=410)

button = tk.Button(text="Calculate Fare", command=calculate)
button.pack()

farelabel = tk.Label(window, text='FARE = ', font=('Helvetica 12 bold'))
farelabel.pack()

tk.mainloop()