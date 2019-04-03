import numpy as np


def read_data_file(file_name):

    file_object = open(file_name, "r")
    data_string = file_object.read().replace("\n", " ")
    file_object.close()
    data_array = np.array(data_string.split(" "))
    return data_array


def evaluation(data_array, output_array, result_array):
    if (type(data_array) is np.ndarray) and (type(output_array) is np.ndarray) and (type(result_array) is np.ndarray):
        len_data_array= data_array.size
        len_output_array= output_array.size
        print("The number of words in actual text : " + str(len_data_array))
        print("The number of words in ocr text : " + str(len_output_array))
        print("The number of correct predicted words : " + str(np.sum(result_array)))
        print("OCR accuracy : " + str((np.sum(result_array))/len_data_array))


def comparision(data_array, output_array):
    if (type(data_array) is np.ndarray) and (type(output_array) is np.ndarray):
        result = np.in1d(data_array, output_array)
        evaluation(data_array, output_array, result)


comparision(read_data_file("data.txt"), read_data_file("outputG.txt"))

