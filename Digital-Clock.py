from tkinter import *  # importing modules#
from tkinter.ttk import *
import datetime
import platform
try:
        import winsound #windows
except:
        import os #other

        # Making Tinker Window#
        window = Tk()
        window.title("Clock")
        window.geometry('500x250')

           #Adding  tkinker tab control#
        tabs_control = Notebook(window)
        clock_tab = Frame(tabs_control)
        alarm_tab = Frame(tabs_control)
        stopwatch_tab = Frame(tabs_control)
        timer_tab = Frame(tabs_control)
        tabs_control.add(clock_tab, text="Clock")
        tabs_control.add(alarm_tab, text="Alarm")
        tabs_control.add(stopwatch_tab, text="Stopwatch")
        tabs_control.add(timer_tab, text="Timer")
        tabs_control.pack(expand = 1, fill ="both")

        #Creating Clock#

        #Adding Clock Components#

        time_label = Label(clock_tab, font = 'calibri 40 bold', Foreground= 'black')
        time_label.pack (anchor='center')
        date_label = Label(clock_tab, font = 'calibri 40 bold', forground = 'black')
        date_label.pack(andchor='s')

        #Clock Function#

        def clock():
                date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
                date,time1 = date_time.split(
                time2, time3 = time.split('/')
                hour, minutes, seconds = time2.split(':')

                if int(hour) > and init(hour) < 24:
                        time = str(int(hours) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
                   else:
                           time = time2 + ' ' + time3
                        time_label.config(text=time)
                        date_label.config(text=date)        
                )

        # Creating Alarm#       

          get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15 bold')
          get_alarm_time_entry.pack(anchor='center')
          alarm_instructions_label = Label(alarm_tab, font = 'calibri 10 bold', text = "Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
          alarm_instructions_label.pack(anchor='s')
          set_alarm_button = Button(alarm_tab, text = "Set Alarm", command=alarm)
          set_alarm_button.pack(anchor='s')
          alarm_status_label = Label(alarm_tab, font = 'calibri 15 bold')
          alarm_status_label.pack(anchor='s') 

          # Alarm Function #

          def alarm(): #Takes the time from the datetime module and format it#
                  main_time = datetime.datetime.now(). strftime("%H:%M %p")
                  alarm_time = get_alarm_time_entry.get()
                  alarm_time1, alarm_time2 = alarm_time.split('')
                  alarm_hour, alarm_minutes = alarm_time1.split(' ')
                  main_time1, main_time2 = main_time1.split(':')
                   #This checks if the time eneterd is equal or not. If equal it will 'Beep' according to OS#
                  if int(main_hour1) > 12 and int(main_hour1) < 24:
                          main_hour = str(int(main_hour1) - 12)
                  else:
                          main_hour = main_hour1
                  if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:    
                       for i in range(3):
                               alarm_status_label.config(text = 'Time Is Up')
                               if platform.system() == 'Windows':
                                       winsound.beep(5000,1000)
                                elif platform.system() == 'Darwin':
                                        os.system('say Time Is Up')
                                elif platfor.system() == 'Linux':
                                        os.system('beep -f 5000')

                        get_alarm_time_entry.config(state = 'enabled')
                        set_alarm_button.cofig(state = 'enabled')
                        get_alarm_time_entry.delete(0, END)
                        alarm_status_label.cofig(text = '')

                        else: 
                                alarm_status_label.cofig(text ='Alarm Has Started')
                                get_alarm_time_entry.config(state = 'disabled')
                                set_alarm_button.config(state = 'disabled')
                                alarm_status_label.after(1000, alarm) 


                # Making Stopwatch Components #

                stopwatch_label = label(stopwatch_tab, font = 'calibr 40 bold', text = 'Stopwatch')
                stopwatch_label.pack(anchor = 'center')
                stopwatch_start = Button (stopwatch_tab, text = 'Stop', state = 'disabled', command = lambda:stopwatch('start'))
                stopwatch_start.pack(anchor = 'center')
                stopwatch_stop = Button(stopwatch_tab, text = 'Stop', state = 'disabled', command=lambda:stopwatch('stop'))
                stopwatch_stop.pack(anchor = 'center')
                stopwatch_reset = Button(stopwatch_tab, text = 'Reset', state = 'disabled', command=lambda:stopwatch('reset'))
                stopwatch_reset.pack(anchor = 'center')

                 # Stopwatch Counter Function #

                 stopwatch_counter_num = 66600
                 stopwatch_running = False

                 def stopwatch_counter(label)
                        def count():
                                if stopwatch_running:
                                        global stopwatch_counter_num
                                        if stopwatch_counter_num=66600:
                                                display = "Starting..."
                                         else:
                                                 tt= datetime.datetime.fromtimestamp(stopwatch_counter_num)
                                                 string= tt.strftime("%H:%M:%S")
                                                 display=string
                                            label.cofig(text=display)
                                            label.after(1000, count)
                                            stopwatch_counter_num += 1

                                        count()    

                   # Adding stopwatch function #

                     def stopwatch(work):
                        if work == 'start':
                                global stopwatch_running
                                stopwatch_running=True
                                stopwatch_start.config(state='disable')
                                stopwatch_stop.config(state='enabled')
                                stopwatch_reset.config(state='enabled')
                                stopwatch_counter(stopwatch_label)
                          elif work == 'stop':
                                  stopwatch_running=False
                                  stopwatch_start.config(state='disabled')
                                  stopwatch_stop.config(state='enabled')
                                  stopwatch_reset.config(state='enabled')
                          elif work = 'reset'
                                global stopwatch_counter_num
                                stopwatch_running=False
                                stopwatch_counter_num=66600
                                stopwatch_label.config(text='Stopwatch')
                                stopwatch_start.config(state='enabled')
                                stopwatch_stop.config(state='disabled')
                                stopwatch_reset.config(state='disabled')

                                #Making Timer#              

