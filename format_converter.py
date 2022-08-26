import glob
import pandas as pd
import cv2
import numpy as np


def resize(image, width, height):
    print('Original Dimensions : ',image.shape)
    image_plane_list = [image[:,:,0], image[:,:,1], image[:,:,2]]
    for x in range(0, 3): 
        dim = (width, height)
        image_plane_list[x] = cv2.resize(image_plane_list[x], dim, interpolation = cv2.INTER_AREA)
        
    resized_image = np.dstack((image_plane_list[0],image_plane_list[1],image_plane_list[2]))
    print('Resized Dimensions : ',resized_image.shape)
    print()
    return resized_image


if __name__=="__main__":
    image_name = []
    image_path = []
    image_size = []
    
    image_new_name_id_512x512 = []
    image_512x512_path = []
    image_512x512_size = []
    
    image_new_name_id_256x256 = []
    image_256x256_path = []
    image_256x256_size = []
    
    image_new_name_id_128x128 = []
    image_128x128_path = []
    image_128x128_size = []
    
    counter = 1
    for file in glob.glob("Standard Input Images\Original Input Images/*"):
        image = cv2.imread(file)
        x, y, z = image.shape
        image_name.append(file.split("\\")[1].split(".")[0])
        image_path.append(file)
        image_size.append((x,y,z))
        
        image = resize(image, 512, 512)
        x, y, z = image.shape
        cv2.imwrite("Standard Input Images/(512,512)/(512x512)image" + str(counter) + ".png", image)
        image_new_name_id_512x512.append("(512x512)image" + str(counter))
        image_512x512_path.append("(512,512)/(512x512)image" + str(counter) + ".png")
        image_512x512_size.append((x,y,z))
        
        image = resize(image, 256, 256)
        x, y, z = image.shape
        cv2.imwrite("Standard Input Images/(256,256)/(256x256)image" + str(counter) + ".png", image)
        image_new_name_id_256x256.append("(256x256)image" + str(counter))
        image_256x256_path.append("(256,256)/(256x256)image" + str(counter) + ".png")
        image_256x256_size.append((x,y,z))
        
        image = resize(image, 128, 128)
        x, y, z = image.shape
        cv2.imwrite("Standard Input Images/(128,128)/(128x128)image" + str(counter) + ".png", image)
        image_new_name_id_128x128.append("(128x128)image" + str(counter))
        image_128x128_path.append("(128,128)/(128x128)image" + str(counter) + ".png")
        image_128x128_size.append((x,y,z))
        
        counter+=1
    
    
    df = pd.DataFrame({"Image Name": image_name,
                       "Image Path":image_path,
                       "Size": image_size,
                       
                       "Image Name (128,128)": image_new_name_id_128x128,
                       "Image Path (128,128)": image_128x128_path,
                       "Size (128,128)": image_128x128_size,
                       
                       "Image Name (256,256)": image_new_name_id_256x256,
                       "Image Path (256,256)": image_256x256_path,
                       "Size (256,256)": image_256x256_size,
                       
                       "Image Name (512,512)": image_new_name_id_512x512,
                       "Image Path (512,512)": image_512x512_path,
                       "Size (512,512)": image_512x512_size})
    
    writer = pd.ExcelWriter("Standard Image Dataset.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Sheet1")
    writer.save()