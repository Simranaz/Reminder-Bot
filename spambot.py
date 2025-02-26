import pyautogui, time, datetime
  
time.sleep(2) 
  
while True: 
    # to display the time at which the message is sent  
    print(datetime.datetime.now()) 
    pyautogui.typewrite("Reminder: Drink water!")  
    pyautogui.press("enter") 
    time.sleep(1) 
  
    print(datetime.datetime.now()) 
  
    pyautogui.typewrite("Reminder: Reminder: Take medicine!")
    pyautogui.press("enter") 
    time.sleep(2) 
  
    print(datetime.datetime.now()) 
  
    pyautogui.typewrite("Reminder: Take the dog for a walk!") 
    pyautogui.press("enter") 
    time.sleep(3) 
  
    print(datetime.datetime.now()) 
  
    pyautogui.typewrite("Reminder: Drink water!") 
    pyautogui.press("enter") 
    time.sleep(4) 
  
    print(datetime.datetime.now()) 
  
    pyautogui.typewrite("Reminder: Drink water!") 
    pyautogui.press("enter") 
    time.sleep(5) 
    