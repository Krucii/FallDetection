import torch
import gradio as gr
from PIL import Image

file = 'best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=file).eval()

model.to('cpu')


def predict(img, size=640):
    g = (size / max(img.size))
    img = img.resize((int(x * g) for x in img.size), Image.Resampling.LANCZOS)
    result = model(img)
    result.render()
    return Image.fromarray(result.ims[0]), result.pandas().xyxy[0]


app = gr.Interface(
    fn=predict,
    inputs=gr.Image(label='Input image', type='pil'),
    outputs=[gr.Image(label='Output image', type='pil'), gr.Text(label='Prediction', type='text')],
    analytics_enabled=False
)

app.launch()
