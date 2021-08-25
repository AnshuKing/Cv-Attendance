#1)Open image location
#2)Making a label for it= file name
#3)converting image into numpy array
#4)making number id for each person
#5)getting training data
#6)feeing trained data in recognizer

def main():
        import os
        from PIL import Image
        import numpy as np
        import cv2
        import pickle


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))#File location
        image_dir = os.path.join(BASE_DIR, "images")#image file location #Dont capitalize thr folder name
        Face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids={}
        y_labels = []
        x_train = []

        for root, dirs, files in os.walk(image_dir):#iterating through folder, sub-folders and files
                for file in files: #iteratin through files
                        if file.endswith("png") or file.endswith("jpg"): #checking if its a picture
                                path = os.path.join(root, file) #creating its location
                                label = os.path.basename(root).replace(" ", "-").lower()#folder name
                                #print(label_ids)
                                if not label in label_ids: #making a number id for each person
                                        label_ids[label] = current_id
                                        current_id+=1
                                id_ = label_ids[label]

                                PIL_IMAGE = Image.open(path).convert("L")#converting it into grayscale
                                image_array = np.array(PIL_IMAGE, "uint8")
                                print(label,path,image_array)
                                faces = Face_cascade.detectMultiScale(image_array,1.3, 5)
                                size = (550,550)
                                final_image = PIL_IMAGE.resize(size, Image.ANTIALIAS)

                                for (x,y,w,h) in faces:
                                        roi = image_array[y:y+h, x:x+h]
                                        x_train.append(roi)#appending face's numpy array as training data
                                        y_labels.append(id_)

        with open("labels.pickle", "wb") as f:
                pickle.dump(label_ids, f)

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("trainner.yml")
        print(x_train)
        print(label_ids)
        print("Training Done")


