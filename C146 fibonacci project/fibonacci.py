from tkinter import*
rt=Tk()

rt.title("Fibonacci Project")
rt.geometry("500x500")

rt.mainloop()

label_series= Label(rt, text="Fibonacci Series")
label_sum= Label(rt)


def fibonacci():
    first_num = 0
    second_num = 1
    new_num = 0
    total_num = 10
    i = 1

    while i <= total_num : 
        label_series["text"] += str(new_num) + " "
        i = i+1
        first_num = second_num
        second_num = new_num
        new_num = first_num + second_num
    

label_sum["text"] = "Fibonacci Sum : " + str(second_num) + str(second_num)



label_series.pack()
label_sum.pack()