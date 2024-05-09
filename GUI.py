import tkinter as tk
from PIL import Image, ImageTk

from fuzzy import handleHealth, calBMI
import textwrap


def handleStart(root):
     
    
    root.destroy()
    newRoot = tk.Tk()
    
    
    # sets the geometry of toplevel
    newRoot.geometry("450x570")
    newRoot.title('Info')
    
 
    # A Label widget to show in toplevel
    tk.Label(newRoot, 
          text ="Your information", font=("Inconsolata", 20)).pack(pady=(20,0))
    sex_var=tk.StringVar()
    age_var=tk.IntVar()
    height_var = tk.IntVar()
    weight_var = tk.IntVar()
    health_var  = tk.IntVar()
    sleep_var = tk.IntVar()

    tk.Label(newRoot, text="Giới tính", width=10, 
          height=2, borderwidth=2, relief="solid").place(x=40,y=100)
    tk.Entry(newRoot,textvariable = sex_var, font=('Arial', 15,'normal')).place(x= 200, y = 105)

    tk.Label(newRoot, text="Độ tuổi", width=10, 
          height=2, borderwidth=2, relief="solid").place(x=40,y=170)
    tk.Entry(newRoot,textvariable = age_var, font=('Arial', 15,'normal')).place(x= 200, y = 175)
    
    tk.Label(newRoot, text="Chiều cao(cm)", width=12, 
          height=2, borderwidth=2, relief="solid").place(x=40,y=240)
    tk.Entry(newRoot,textvariable = height_var, font=('Arial', 15,'normal')).place(x= 200, y = 245)
    
    tk.Label(newRoot, text="Cân nặng", width=10, 
          height=2, borderwidth=2, relief="solid").place(x=40,y=310)
    tk.Entry(newRoot,textvariable = weight_var, font=('Arial', 15,'normal')).place(x= 200, y = 315)
    
    tk.Label(newRoot, text="Tập thể dục(số lần/tuần)", width=20, 
          height=2, borderwidth=2, relief="solid").place(x=40,y=390)
    tk.Entry(newRoot,textvariable = health_var, font=('Arial', 15,'normal')).place(x= 200, y = 395)

    tk.Label(newRoot, text="Giấc ngủ(giờ/1 đêm)", width=16, 
          height=2, borderwidth=2, relief="solid").place(x=40,y=460)
    tk.Entry(newRoot,textvariable = sleep_var, font=('Arial', 15,'normal')).place(x= 200, y = 465)

    tk.Button(newRoot, text='Xác nhận', padx=20, command=lambda: submitResult(newRoot, sex_var.get(), height_var.get(), weight_var.get(), health_var.get(), sleep_var.get(), age_var.get())).place(x= 180,y = 510)
    
    newRoot.mainloop()

def submitResult(root, sex, height, weight, exercise,sleep, age ):
    
    top = tk.Toplevel(root)
     
    top.title("Result")
    
    top.geometry("480x570")

    BMI = calBMI(height= float(height/100), weight=weight)
    
    
    
    result = handleHealth(bmi=BMI, sleep= sleep, gym= exercise)

    tk.Label(top, 
          text ="Your physical condition", font=("Arial", 20)).pack(pady=(20,80))
    if result <3:
        tk.Label(top, 
          text ="Weak", font=("Arial", 40)).pack(pady=(20,0))
    if result >=3 and result <= 4:
        tk.Label(top, 
          text ="Healthy", font=("Arial", 40)).pack(pady=(20,0))
        
    if result>4 and result <=5:
        tk.Label(top, 
          text ="Good", font=("Arial", 40)).pack(pady=(20,0))
        

    tk.Button(top, text='Advices', padx=20, command=lambda: showAdvice(top,sex,height,weight,exercise,sleep,age,BMI)).place(x= 180,y = 510)
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
def calBMR(height, weight,sex,age ):

    if sex.upper()=="NAM" :
        return round(66+(13.7*weight)+(5*height)-(6.8*age),2)
    if sex.upper()=='NỮ':
        return round(665+(9.6*weight)+(1.8*height)-(4.7*age),2)
def showAdvice(root,sex, height, weight, excercise, sleep, age,BMI):
    
    

    top = tk.Toplevel(root)
     
    top.title("Advices")
    BMR= calBMR(height=height,weight=weight,sex=sex,age=age)
    if sleep<6 and BMI<18.5 and excercise<2:
         tk.Label(top, 
          text =textwrap.fill(f'Chỉ số bmr của bạn là {BMR} và bạn đang thiếu cân, bạn cần tập luyện và ăn uống nhiều hơn để có thể cải thiện cân nặng của mình.Bạn đang ngủ hơi ít, bạn hãy ngủ trong khoảng 6-8 tiếng mỗi ngày',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
        
    if sleep<6 and BMI>25 and excercise<2:
        tk.Label(top, 
          text =textwrap.fill(f'Chỉ số bmr của bạn là {BMR} và bạn đang thừa cân, bạn cần tập luyện nhiều hơn  và ăn uống ít hơn để có thể cải thiện cân nặng của mình.Bạn đang ngủ hơi ít, bạn hãy ngủ trong khoảng 6-8 tiếng mỗi ngày',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
    if sleep >8 and BMI<18.5 and excercise<2:
        tk.Label(top, 
          text =textwrap.fill(f'Chỉ số bmr của bạn là {BMR} và bạn đang thiếu cân, bạn cần tập luyện nhiều hơn và ăn uống nhiều hơn để có thể cải thiện cân nặng của mình.Bạn đang ngủ hơi nhiều, bạn hãy ngủ trong khoảng 6-8 tiếng mỗi ngày',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
    if sleep >8 and BMI >25 and excercise<2:
        tk.Label(top, 
          text =textwrap.fill(f'Chỉ số bmr của bạn là {BMR} và bạn đang thừa cân, bạn cần tập luyện nhiều hơn và ăn uống ít hơn để có thể cải thiện cân nặng của mình.Bạn đang ngủ hơi nhiều, bạn hãy ngủ trong khoảng 6-8 tiếng mỗi ngày',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
    if sleep <6: 
        tk.Label(top, 
          text =textwrap.fill(f'Bạn đang ngủ hơi ít, bạn hãy ngủ trong khoảng 6-8 tiếng mỗi ngày',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
    if sleep >8:   
        tk.Label(top, 
          text =textwrap.fill(f'Bạn đang ngủ hơi nhiều, bạn hãy ngủ trong khoảng 6-8 tiếng mỗi ngày',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
    if BMI <18.5 :
        if excercise <= 2:
            tk.Label(top, 
          text =textwrap.fill(f'Bạn đang thiếu cân, bạn hãy ăn ở mức calo là {round(BMR*1.3+500,1)} để có thể tăng cân và hãy nhớ tăng cường tập thể dục nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))            
        if excercise>2 and excercise<=4:
             tk.Label(top,
            text =textwrap.fill(f'Bạn đang thiếu cân, bạn hãy ăn ở mức calo là {round(BMR*1.55+500,1)} để có thể tăng cân nhé!',width=40) , font=("Arial",15)).pack(pady=(20,0),padx=(20,0))            
        if excercise >4:   
             tk.Label(top,
            text =textwrap.fill(f'Bạn đang thiếu cân, bạn hãy ăn ở mức calo là {round(BMR*1.7+500,1)} để có thể tăng cân nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))     
    if BMI >25 :
        if excercise < 2:
            tk.Label(top, 
          text =textwrap.fill(f'Bạn đang thừa cân, bạn hãy ăn ở mức calo là {roung(BMR*1.3-500,1)} để có thể giảm cân và hãy nhớ tăng cường tập thể dục nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))            
        if excercise>=2 and excercise<=4:
            tk.Label(top,
            text =textwrap.fill(f'Bạn đang thừa cân, bạn hãy ăn ở mức calo là {BMR*1.55-500} để có thể giảm cân nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))            
        if excercise >4:
            tk.Label(top,   
            text =textwrap.fill(f'Bạn đang thừa cân, bạn hãy ăn ở mức calo là {round(BMR*1.7-500,1)} để có thể giảm cân nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))   
    if excercise <=2:      
        tk.Label(top, 
          text =textwrap.fill(f'Hãy tăng cường tập thể dục để cải thiện sức khỏe nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0)) 
    if excercise>2 and excercise<=4:
        tk.Label(top, 
          text =textwrap.fill(f'Bạn tập thể dục khá tốt, hãy cố gắng phát huy nhé',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))  
    if excercise >4:
        tk.Label(top, 
          text =textwrap.fill(f'Chế độ tập thể dục của bạn đang rất tốt.Hãy cố gắng duy trì nhé!',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))  
    if excercise >=4 and sleep>6 and sleep <10:
        tk.Label(top, 
          text =textwrap.fill(f'Chế độ sinh hoạt của bạn đang khá tốt.Hãy cố gắng duy trì nó nhé! ',width=40) , font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))                                                       
    top.geometry("480x570")

    tk.Button(top, text='Một số nơi dành cho bạn', padx=20, command=lambda: Destination(top,) ).place(x= 180,y = 510)
    tk.Button(top, text='BMR là gì ', padx=20, command=lambda: WhatisBMR(top,) ).place(x= 180,y = 480)
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
def Destination(root):
    top = tk.Toplevel(root)
     
    top.title("Destination")
    tk.Button(top, text='Nơi tập gym uy tín, giá rẻ',font=("Arial",20),bg='blue',fg='white', padx=20, command=lambda: Gym(top,) ).pack(pady=(50,0))
    tk.Button(top, text='Nơi bán đồ ăn tươi sạch',font=("Arial",20),bg='blue',fg='white', padx=20, command=lambda: Food(top,) ).pack(pady=(50,0))
    top.geometry("480x570")
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
def Gym(root):
    top = tk.Toplevel(root)
     
    top.title("Gym")
    tk.Button(top, text='WAYSTAION GYM',font=("Arial",20),bg='blue',fg='white', padx=20, command=lambda: Waygym(top,) ).pack(pady=(50,0))
    tk.Button(top, text='CITY GYM',font=("Arial",20),bg='red',fg='white', padx=20, command=lambda: Citygym(top,) ).pack(pady=(80,0))
    tk.Button(top, text='S LIFE GYM',font=("Arial",20),bg='green',fg='white', padx=20, command=lambda: Slifegym(top,) ).pack(pady=(100,0))

    
    
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)



    top.geometry("480x570")

def Waygym(root):
    top = tk.Toplevel(root)
    

    top.title("Waysation Gym ")
    tk.Label(top, 
          text =f'Chi nhánh Bình thạnh:\nSố 60-Hoàng Hoa Thám-Phường 7 ', bg='blue',fg='white' , font=("Arial", 15)).pack(pady=(50,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Gò vấp:\nSố 770-Quang-Phường 8 ', bg='blue',fg='white' , font=("Arial", 15)).pack(pady=(80,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Thủ Đức:\nSố 56f-Dân Chủ-Bình Thọ ', bg='blue',fg='white' , font=("Arial", 15)).pack(pady=(100,0),padx=(20,0))




    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")
def Citygym(root):
    top = tk.Toplevel(root)
    

    top.title("CityGym ")
    tk.Label(top, 
          text =f'Chi nhánh quận 10:\nSố 52-Thành Thái-Phường 12 ', bg='red',fg='white' , font=("Arial", 15)).pack(pady=(50,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Phú Nhuận:\nSố 119-Phổ Quang-Phường 9 ', bg='red',fg='white' , font=("Arial", 15)).pack(pady=(80,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Bình Thạnh:\nSố 526-Điện Biên Phủ-Phường 21 ', bg='red',fg='white' , font=("Arial", 15)).pack(pady=(100,0),padx=(20,0))




    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")
def Slifegym(root):
    top = tk.Toplevel(root)
    

    top.title("S Life Gym ")
    tk.Label(top, 
          text =f'Chi nhánh Gò Vấp:\nSố 652-Quang Trung-Phường 11 ', bg='Green',fg='white' , font=("Arial", 15)).pack(pady=(50,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Phú Nhuận:\nSố 210-Huỳnh Văn Bánh-Phường 12 ', bg='Green',fg='white' , font=("Arial", 15)).pack(pady=(80,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Bình Thạnh:\nSố 26-Nguyễn Huy Lượng- Phường 14 ', bg='Green',fg='white' , font=("Arial", 15)).pack(pady=(100,0),padx=(20,0))




    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")


   



def Food(root):
    top = tk.Toplevel(root)
     
    top.title("Food")
    tk.Button(top, text='CO.OP FOOD',font=("Arial",20),bg='green',fg='white', padx=20, command=lambda: coopfood(top,) ).pack(pady=(50,0))
    tk.Button(top, text='Winmart',font=("Arial",20),bg='red',fg='white', padx=20, command=lambda: winmart(top,) ).pack(pady=(80,0))
    tk.Button(top, text='Organic Food ',font=("Arial",20),bg='green',fg='white', padx=20, command=lambda: organic(top,) ).pack(pady=(100,0))


    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")

    
def coopfood(root):
    top = tk.Toplevel(root)
     
    top.title("Co.op Food")
    tk.Label(top, 
          text =f'Chi nhánh Quận 1:\nSố 95-Pasteur', bg='green',fg='white' , font=("Arial", 15)).pack(pady=(50,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Quận 3:\nSố 209-Lê Văn Sỹ-Phường 13 ', bg='green',fg='white' , font=("Arial", 15)).pack(pady=(80,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Tân Bình:\nSố 405-Hoàng Văn Thụ- Phường 2 ', bg='green',fg='white' , font=("Arial", 15)).pack(pady=(100,0),padx=(20,0))
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")

def winmart(root):
    top = tk.Toplevel(root)
     
    top.title("Winmart")
    tk.Label(top, 
          text =f'Chi nhánh Quận 1:\nSố 33-Lý Văn Phức-phường Tân Định', bg='red',fg='white' , font=("Arial", 15)).pack(pady=(50,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Quận 3:\nSố 107A-Vườn Chuối-Phường 4 ', bg='red',fg='white' , font=("Arial", 15)).pack(pady=(80,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Tân Bình:\nSố 81-Bầu Cát 8- Phường 11 ', bg='red',fg='white' , font=("Arial", 15)).pack(pady=(100,0),padx=(20,0))
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")
def organic(root):
    top = tk.Toplevel(root)
     
    top.title("Organic Food")
    tk.Label(top, 
          text =f'Chi nhánh Quận 1:\nSố 123-Đinh Tiên Hoàng-Phường Đa Kao', bg='green',fg='white' , font=("Arial", 15)).pack(pady=(50,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Phú Nhuận:\nSố 146-Phan Đình Phùng-Phường 2 ', bg='green',fg='white' , font=("Arial", 15)).pack(pady=(80,0),padx=(20,0))
    tk.Label(top, 
          text =f'Chi nhánh Quận 3:\nSố 130-Nguyễn Đình Chiểu- Phường 6 ', bg='green',fg='white' , font=("Arial", 15)).pack(pady=(100,0),padx=(20,0))
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")
def WhatisBMR(root):
    top = tk.Toplevel(root)
     
    top.title("What is BMR ?")
    tk.Label(top, 
          text =textwrap.fill(f'Chỉ số BMR (Basal Metabolic Rate) là tỷ lệ trao đổi chất cơ bản trong cơ thể con người. Chỉ số này cho biết mức năng lượng tối thiểu mà cơ thể cần, để thực hiện các chức năng cơ bản nhằm đảm bảo duy trì sự sống của cơ thể, khi bạn ở trạng thái nghỉ ngơi. Các chức năng này bao gồm các hoạt động của các cơ quan tim, gan, phổi, não, thận, gan, cơ, mỡ',width=40), font=("Arial", 15)).pack(pady=(20,0),padx=(20,0))
    
    tk.Button(top, text='Back', padx=20, command=top.destroy).place(x= 0,y = 510)
    top.geometry("480x570")

def MainGUI():
    root = tk.Tk()
    root.geometry("450x570")

    root.title('GUI')

    bg = tk.PhotoImage( file = "image.png")

    label1 = tk.Label( root, image = bg) 
    label1.place(x = 0,y = 0)

    label2 = tk.Label( root, text = "Health Management App", font=("Arial", 20) , background='#e4eaed' ) 
    label2.pack(pady=(220, 0)) 

    
    frame1 = tk.Frame(root, bg = "#e4eaed") 
    frame1.pack(pady=(100,0)) 

    startButton = tk.Button(frame1, text='START', padx=20, command=lambda: handleStart(root))
    startButton.pack(pady=0)

    endButton = tk.Button(frame1, text='END', padx=20, command=root.destroy)
    endButton.pack(pady=50)
    root.mainloop()

if __name__=="__main__": 

    MainGUI()




    
    

    
  


    




 