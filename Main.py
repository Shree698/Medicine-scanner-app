import cv2
import pytesseract
from googletrans import Translator
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.camera import Camera


class MedicineScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(MedicineScanner, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Camera widget for capturing image
        self.camera = Camera(play=True)
        self.add_widget(self.camera)

        # Button to capture image
        self.capture_button = Button(text="Capture Medicine Image")
        self.capture_button.bind(on_press=self.capture_image)
        self.add_widget(self.capture_button)

        # Label to show OCR output
        self.output_label = Label(text="Scan a medicine to see its information.")
        self.add_widget(self.output_label)

        # Language selection spinner
        self.lang_spinner = Spinner(
            text='en', values=('en', 'es', 'fr', 'de', 'it')
        )
        self.lang_spinner.bind(text=self.change_language)
        self.add_widget(self.lang_spinner)

        # Translator
        self.translator = Translator()

    def capture_image(self, instance):
        ret, frame = self.camera._camera.get_frame()
        if ret:
            cv2.imwrite("captured.jpg", frame)
            self.process_image("captured.jpg")

    def process_image(self, img_path):
        img = cv2.imread(img_path)
        text = pytesseract.image_to_string(img)
        translated_text = self.translator.translate(text, dest=self.lang_spinner.text).text
        self.output_label.text = f"Scanned Text:\n{translated_text}"

    def change_language(self, spinner, text):
        self.output_label.text = f"Language changed to {text}"


class MedicineApp(App):
    def build(self):
        return MedicineScanner()


if __name__ == '__main__':
    MedicineApp().run()
