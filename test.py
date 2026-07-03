import tkinter as tk

# --- Station lists with shared intersections ---
stn_sL = ['Hogwarts', 'Camp Half-Blood', 'Ilya', 'Camp Jupiter', 'Miyagi Do', 'Wonderland', 'Heartless']
stn_pL = ['Azkaban', 'Hogsmeade', 'Elites', 'Miyagi Do', 'Earth', 'The Valley', 'Cobra Kai']
stn_dL = ['Wildcat island', 'The Bowl', 'Loot', '', 'BG5142', 'Venus', 'Pensieve']

coords_sL = {}
coords_pL = {}
coords_dL = {}

win = tk.Tk()
win.title("Simple Metro Map")
win.configure(bg='DarkGreen')
win.geometry("600x600")

canvas = tk.Canvas(win, width=550, height=500, bg='white')
canvas.pack()

# --- Draw Line (horizontal) ---
x, y = 50, 200
for stn in stn_sL:
    coords_sL[stn] = (x, y)
    if stn != stn_sL[-1]:
        canvas.create_line(x, y, x + 70, y, fill='orange', width=2)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='orange')
    if stn != 'Ilya' and stn != 'Miyagi Do':
        canvas.create_text(x, y + 20, text=stn, fill='orange', font=('Helvetica', 8))
    x += 70

# --- Draw Line (vertical) ---
x, y = 330, 40
for stn in stn_pL:
    coords_pL[stn] = (x, y)
    if stn != stn_pL[-1]:
        canvas.create_line(x, y, x, y + 70, fill='blue', width=2)
    if stn != 'Miyagi Do':
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')
        if stn == 'Elites':
            canvas.create_text(x + 40, y - 10, text=stn, fill='blue', font=('Helvetica', 8))
        else:
            canvas.create_text(x + 40, y, text=stn, fill='blue', font=('Helvetica', 8))
    y += 70

# --- Draw Line (vertical intersecting 'Ilya') ---
ix, iy = coords_sL['Ilya']
x, y = ix, iy - (len(stn_dL) // 2) * 60
for stn in stn_dL:
    coords_dL[stn] = (x, y)
    if stn != stn_dL[-1]:
        canvas.create_line(x, y, x, y + 60, fill='green', width=2)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='green')
    if stn == 'Loot':
        canvas.create_text(x - 40, y - 10, text=stn, fill='green', font=('Helvetica', 8))
    elif stn != 'Ilya':
        canvas.create_text(x - 40, y, text=stn, fill='green', font=('Helvetica', 8))
    y += 60

# --- Draw shared 'Ilya' and 'Miyagi Do' in red only once ---
ix, iy = coords_sL['Ilya']
canvas.create_oval(ix - 6, iy - 6, ix + 6, iy + 6, fill='red')
canvas.create_text(ix, iy + 20, text='Ilya', fill='red', font=('Helvetica', 9, 'bold'))

mx, my = coords_sL['Miyagi Do']
canvas.create_oval(mx - 6, my - 6, mx + 6, my + 6, fill='red')
canvas.create_text(mx + 35, my - 10, text='Miyagi Do', fill='red', font=('Helvetica', 9, 'bold'))

# --- Dropdowns ---
all_stations = list(set(stn_sL + stn_pL + stn_dL))
tk.Label(win, text='Start').place(x=50, y=300)
tk.Label(win, text='Stop').place(x=250, y=300)

start_var = tk.StringVar()
stop_var = tk.StringVar()
tk.OptionMenu(win, start_var, *all_stations).place(x=50, y=320)
tk.OptionMenu(win, stop_var, *all_stations).place(x=250, y=320)

fare_label = tk.Label(win, text='FARE =', font=('Helvetica', 12, 'bold'), bg='DarkGreen', fg='white')
fare_label.pack(pady=10)

# --- Draw route line ---
def draw_route():
    canvas.delete('route')
    start = start_var.get()
    stop = stop_var.get()
    if not start or not stop or start == stop:
        fare_label.config(text='Invalid selection')
        return

    # Get coordinates
    if start in coords_sL:
        x1, y1 = coords_sL[start]
        line_start = stn_sL
    elif start in coords_pL:
        x1, y1 = coords_pL[start]
        line_start = stn_pL
    else:
        x1, y1 = coords_dL[start]
        line_start = stn_dL

    if stop in coords_sL:
        x2, y2 = coords_sL[stop]
        line_stop = stn_sL
    elif stop in coords_pL:
        x2, y2 = coords_pL[stop]
        line_stop = stn_pL
    else:
        x2, y2 = coords_dL[stop]
        line_stop = stn_dL

    # Same line
    if line_start == line_stop:
        canvas.create_line(x1, y1, x2, y2, fill='red', width=3, tags='route')
        stops = abs(line_start.index(start) - line_start.index(stop))

    # Different lines - check for intersections
    elif ('Miyagi Do' in line_start and 'Miyagi Do' in line_stop):
        xm, ym = coords_sL['Miyagi Do']
        canvas.create_line(x1, y1, xm, ym, fill='red', width=3, tags='route')
        canvas.create_line(xm, ym, x2, y2, fill='red', width=3, tags='route')
        stops = abs(line_start.index(start) - line_start.index('Miyagi Do')) + abs(line_stop.index(stop) - line_stop.index('Miyagi Do'))

    elif ('Ilya' in line_start and 'Ilya' in line_stop):
        xi, yi = coords_sL['Ilya']
        canvas.create_line(x1, y1, xi, yi, fill='red', width=3, tags='route')
        canvas.create_line(xi, yi, x2, y2, fill='red', width=3, tags='route')
        stops = abs(line_start.index(start) - line_start.index('Ilya')) + abs(line_stop.index(stop) - line_stop.index('Ilya'))

    else:
        # Complex 3-line route via both intersections: Ilya → Miyagi Do
        xi, yi = coords_sL['Ilya']
        xm, ym = coords_sL['Miyagi Do']
        canvas.create_line(x1, y1, xi, yi, fill='red', width=3, tags='route')
        canvas.create_line(xi, yi, xm, ym, fill='red', width=3, tags='route')
        canvas.create_line(xm, ym, x2, y2, fill='red', width=3, tags='route')

        stops1 = abs(line_start.index(start) - line_start.index('Ilya'))
        stops2 = abs(line_stop.index(stop) - line_stop.index('Miyagi Do'))
        stops = stops1 + 1 + stops2  # +1 for transfer between Ilya and Miyagi Do

    fare_label.config(text=f"FARE = INR {stops * 75}")

tk.Button(win, text='Calculate Fare', command=draw_route).pack()

win.mainloop()