import os
os.system('pip3 install -r  ~/Desktop/Face_ID/requirements.txt')
import tkinter as tk
from tkmacosx import Button

root = tk.Tk()
root.title('Face ID Mac')
label = tk.Label(padx=50,pady=50)


def setting_sleep_watcher():
    try:
        os.system('sudo rm -rf /Library/StartupItems/SleepWatcher')
        os.system('sudo cp ~/Desktop/Face_ID/sleepwatcher_2.2.1/sleepwatcher /usr/local/sbin')
        os.system('sudo cp ~/Desktop/Face_ID/sleepwatcher_2.2.1/sleepwatcher.8 /usr/local/share/man/man8')
        os.system('sudo cp ~/Desktop/Face_ID/sleepwatcher_2.2.1/config/de.bernhard-baehr.sleepwatcher-20compatibility.plist /Library/LaunchDaemons/de.bernhard-baehr.sleepwatcher.plist')
        os.system('sudo cp ~/Desktop/Face_ID/sleepwatcher_2.2.1/config/rc.* /etc')
        os.system('sudo launchctl load /Library/LaunchDaemons/de.bernhard-baehr.sleepwatcher.plist')
    except Exception as e:
        label.insert(0, 'ERROR')

def click():
    #os.system('pip3 install -r requirements.txt')
    setting_sleep_watcher()
    try:
        os.system('python3 ~/Desktop/Face_ID/collecting_images.py')
        os.system('python3 ~/Desktop/Face_ID/creating_files.py')
    except Exception as e:
        label.insert(0, 'ERROR')
    
    os.system('/usr/local/sbin/sleepwatcher --verbose --wakeup ~/Desktop/Face_ID/hello.sh')


button = Button(root,command=click,text='RUN FACE ID',padx=50,pady=50,fg='red',bg='blue').pack()


root.mainloop()
quit()
