def main():
        import numpy as np
        import cv2
        import os

        

        import tkinter as tk
        from tkinter import simpledialog

        ROOT = tk.Tk()

        ROOT.withdraw()
        name = simpledialog.askstring(title="Test",prompt="Enter Your Name: ")
        
        
        numberofpics=60
        img_num = -10
        #name = str(input("what is your name: "))
        if (name!= None) and name!='' :
                name = (name.lower()).replace(" ", "-")

                base_dir = os.path.dirname(os.path.abspath(__file__))
                image_dir = os.path.join(base_dir, "images")
                specified_dir = os.path.join(image_dir, name)


                if os.path.exists(specified_dir):#checking if student already_exists
                        pass
                else:
                        os.makedirs(specified_dir)

                Face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

                cap=cv2.VideoCapture(0)
                status = True
                while status:
                        ret, frame = cap.read()
                        faces = Face_cascade.detectMultiScale(frame,1.3, 5)

                        if img_num>0 and img_num<numberofpics+1:
                                cv2.imwrite(os.path.join(specified_dir,(("img#")+str(img_num)+(".png"))),frame)
                        elif img_num>numberofpics+1:
                                cv2.putText(frame,("press q to exit"),(40,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2, cv2.LINE_AA)
                        img_num+=1
                        if cv2.waitKey(20) & 0xFF == ord("q"):
                                break
                        cv2.imshow("frame", frame)
                        


                cap.release()
                cv2.destroyAllWindows()


                        


