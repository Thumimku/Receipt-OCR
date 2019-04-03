import os
from PIL import Image

def main():
    ## defining the directories which we have to work with
    images_dir = r'/home/thumilan/Desktop/FYP/Img-DataBank'
    output_images_dir = r'/home/thumilan/Desktop/FYP/Img-DataBank-Output'



    images_list= os.listdir(images_dir)


    ## creating the test_menu_output folder if it does not exists
    if not os.path.exists(output_images_dir):
        os.makedirs(output_images_dir)

    new_images_list=[images_dir + '/' + x for x in images_list]
    print(new_images_list[0])    #
    ########################################################################

    '''
    Now to automate the task of cleaning the image
    '''
    ### traversing the images list
    i = 0

    # with open(error_files, 'w') as f:
    #     try:
    for img in new_images_list:
        image_name = images_list[i]
        new_image_name = output_images_dir + '/' + image_name[:-4]

        print('cleaning image : ' + new_image_name)

        #############################################
        ## Cleaning the image
        # greyscaling the image

        col = Image.open(img)
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x < 150 else 250, '1')
        cleaned_image_name = new_image_name + '_cleaned.jpg'
        bw.save(cleaned_image_name)

                ##############################################
        i += 1
        # except Exception as e:
        #     var = img
        #     f.write(var)
        #     ## this will write a log file about the images which could not be opened and will
        #     ## append the absolute path to those images in the directory
        #     f.write('\n')


########################################################################


if __name__ == '__main__':
    main()