from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr_r=time.strftime('%I')
    mi=time.strftime('%M')
    sec_c=time.strftime('%S')
    am_pm=time.strftime('%p')

    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    hr.config(text=hr_r)
    min1.config(text=mi)
    sec.config(text=sec_c)
    am.config(text=am_pm)

    date_txt.config(text=date)
    month_txt.config(text=month)
    year_txt.config(text=year)
    day_txt.config(text=day)
    hr.after(200,date_time)

clock=Tk()
clock.title('   ## DIGITAL CLOCK ##')
clock.geometry("700x500")
clock.config(bg='#8B475D')

hr=Label(clock,text="00",font=('Arial Black',45,"bold"), bg='#808080', fg='white')
hr.place(x=40, y=40, height=110, width=100)
hr_txt=Label(clock,text="Hour",font=('Arial Black',15, "bold"), bg='#808080', fg='white')
hr_txt.place(x=40, y=170, height=40, width=100)

min1=Label(clock,text="00",font=('Arial Black',45,"bold"), bg='#808080', fg='white')
min1.place(x=210, y=40, height=110, width=100)
min_txt=Label(clock,text="Minute",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
min_txt.place(x=210, y=170, height=40, width=100)

sec=Label(clock,text="00",font=('Arial Black',45,"bold"), bg='#808080', fg='white')
sec.place(x=380, y=40, height=110, width=100)
sec_txt=Label(clock,text="Second",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
sec_txt.place(x=380, y=170, height=40, width=100)

am=Label(clock,text="00",font=('Arial Black',40,"bold"), bg='#808080', fg='white')
am.place(x=550, y=40, height=110, width=100)
am_txt=Label(clock,text="AM/PM",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
am_txt.place(x=550, y=170, height=40, width=100)

# date
date_txt=Label(clock,text="00",font=('Arial Black',45,"bold"), bg='#808080', fg='white')
date_txt.place(x=40, y=250, height=110, width=100)
date_txt_txt=Label(clock,text="Date",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
date_txt_txt.place(x=40, y=380, height=40, width=100)

month_txt=Label(clock,text="00",font=('Arial Black',45,"bold"), bg='#808080', fg='white')
month_txt.place(x=210, y=250, height=110, width=100)
month_txt_txt=Label(clock,text="Month",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
month_txt_txt.place(x=210, y=380, height=40, width=100)

year_txt=Label(clock,text="00",font=('Arial Black',45,"bold"), bg='#808080', fg='white')
year_txt.place(x=380, y=250, height=110, width=100)
year_txt_txt=Label(clock,text="Year",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
year_txt_txt.place(x=380, y=380, height=40, width=100)

day_txt=Label(clock,text="00",font=('Arial Black',25,"bold"), bg='#808080', fg='white')
day_txt.place(x=550, y=250, height=110, width=100)
day_txt_txt=Label(clock,text="Day",font=('Arial Black',15,"bold"), bg='#808080', fg='white')
day_txt_txt.place(x=550, y=380, height=40, width=100)

date_time()
clock.mainloop()