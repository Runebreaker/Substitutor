import PIL.Image
import gradio as gr

presets = {}
encoded_text = []


def add_symbol(input_img: PIL.Image.Image):
    pass


typing_interface = gr.Interface(lambda name: "Hello " + name, "text", "text")
substitution_interface = gr.Interface(lambda name: "Bye " + name, "text", "text")
with gr.Blocks() as image_interface:
    gr.Dropdown(list(presets.keys()), label="New Symbol", info="Upload an image of a symbol to add it to the current key set.")
    gr.Image()
    gr.Button("Add")

demo = gr.TabbedInterface([typing_interface, substitution_interface, image_interface], ["Hello World", "Bye World", "Alphabets"])

if __name__ == "__main__":
    demo.launch()
