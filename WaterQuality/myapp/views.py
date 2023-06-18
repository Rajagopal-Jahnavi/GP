from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('C:/Users/j2732/Downloads/GroupProject/path_to_saved_model')

class_names =['mud water', 'oil water', 'pure water']
@csrf_exempt
def predict_water_quality(request):
    if request.method == 'POST':
        image = request.FILES['image']
        img = Image.open(image)
        img = img.resize((180, 180)) 
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        img_array = img_array / 255.0

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        predicted_class_index = np.argmax(score)
        predicted_class_label = class_names[predicted_class_index]
        confidence = 100 * np.max(score)
        return render(request, 'prediction.html', {
            'prediction': predicted_class_label,
            'confidence': confidence,
            'uploaded_image': image
        })
        # return render(request, 'prediction.html', {'prediction': predicted_class_label, 'confidence': confidence})
    
    return render(request, 'index.html')