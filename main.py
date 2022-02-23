from PIL import Image, ImageDraw, ImageFont, ImageTk
import PySimpleGUI as sg
import matplotlib.pyplot as plt

main_layout = [
    [sg.Text('Welcome to my Watermarking Program!')],
    [sg.Text('Select your image')],
    [sg.Input(),
     sg.FileBrowse(file_types=(('JPG', '.jpg'), ('PNG', '.png')))],
    [sg.Button('Enter', key='-ENTER-', visible=True),
     sg.pin(sg.Button('Text', key='-TEXT-', visible=False)),
     sg.pin(sg.Button('Logo', key='-LOGO-', visible=False))],
    [sg.Image(key='-IMAGE-')]
]

window = sg.Window('Watermark', main_layout, resizable=True, element_justification='c')

while True:
    event, values = window.read()
    image = Image.open(values[0])
    photo = ImageTk.PhotoImage(image)

    if event == '-ENTER-':
        # Trying to get the image to display in the window
        # window.Element('-IMAGE-').update(filename=photo)
        window['-ENTER-'].update(visible=False)
        window['-TEXT-'].update(visible=True)
        window['-LOGO-'].update(visible=True)
        plt.imshow(image)
        plt.show()

    if event == '-TEXT-':
        text = sg.popup_get_text('Enter text to add to your image')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('Zachery.otf', size=50)
        draw.text((0, 0), text, font=font, fill='black', stroke_width=0)
        image.show()
        plt.imshow(image)
        plt.show()
    elif event == '-LOGO-':
        logo = sg.popup_get_file('Select logo to add to your image')
        image.show()
        watermark = Image.open(logo)
        watermark.thumbnail((round(image.size[0] / 2), round(image.size[0] / 2)))
        image.paste(watermark, (0, 0))
        plt.imshow(image)
        plt.show()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()
