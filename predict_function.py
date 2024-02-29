# import models
# view result function
# take image as a parameter
# predict using CNN model
# if result normal 
# predict using ANN
# finaly send mail and out report


from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import report_gen
import emailing
import image_segmentation

cnn_classifier = load_model('models/CNN.h5')
ann_classifier = load_model('models/ANN.h5')
email_to = "mahmoudmansour1082003@gmail.com"


def prediction(p_id, img_path, gender, age, hyper, heart, avg_g, obs, smk, eye, verb, mot):
    test_case = image.load_img(img_path, target_size = (100, 100))
    test_case = image.img_to_array(test_case)
    test_case = np.expand_dims(test_case, axis = 0)
    result = cnn_classifier.predict(test_case)
    image_segmentation.unsupervised_segmentation(img_path)
    image_segmentation.chan_vese_segmentation(img_path)
    image_segmentation.supervised_segmentation(img_path)
    image_segmentation.Adaptive_thresh(img_path)
    print("image segmentation is done")
    if result[0][0] == 0:
      print("Hemorrhage")
      report_gen.convert_html_to_pdf(p_id, gender, age, hyper, heart, avg_g, obs, smk, eye, verb, mot, "Hemorrhage")
      emailing.send_emails(email_to)
      return "Hemorrhage"
      
    else:
        result = ann_classifier.predict([[gender, age, hyper, heart, avg_g, obs, smk]])
        if [0][0] > 0.5:
            report_gen.convert_html_to_pdf(p_id, gender, age, hyper, heart, avg_g, obs, smk, eye, verb, mot, "Strock")
            emailing.send_emails(email_to)
            return "Stroke"
        else:
            return "Normal"
        
