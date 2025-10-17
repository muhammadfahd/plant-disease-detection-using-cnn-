import gradio as gr
from tensorflow.keras.models import load_model
from PIL import Image

MODEL = load_model('beans_classifier.h5')
CLASSES = class_names
IMG_SIZE = 128

def predict(img):
    img = Image.fromarray(img).resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    preds = MODEL.predict(img)
    class_idx = np.argmax(preds[0])
    return CLASSES[class_idx]

iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=3, label="Predicted Disease"),
    title="Bean Leaf Disease Classifier",
    description="Upload a photo of a bean leaf (healthy or diseased). The model predicts: healthy, angular leaf spot or bean rust."
)
iface.launch(debug=True)  # For local testing
