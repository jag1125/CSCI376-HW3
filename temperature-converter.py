from nicegui import ui

ui.colors(
      primary='#3b2f2a',
      secondary='#58807c',
      accent='#7a7a7a',
      positive='#394a3d',
      negative='#c2848b',
      info='#423e66',
      warning='#c2874f'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: Changes the text color to that of our positive definition in ui.colors
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold !text-negative mt-4")
        # text-negative: Changes the text color to that of our negative definition in ui.colors

def celc_update_label():
    value = int(celc_dropdown.value)
    celc_label.set_text(f"From {value}°C to {value * 9/5 + 32:.2f}°F.")

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-300 p-5 shadow-xl mx-auto mt-20 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Changes the padding of the element to be 6
        # shadow-xl: Creates an xl size shadow effect on the element
        # mx-auto: Sets the margins to the auto value
        # mt-10: Sets the top margin to 10
        # rounded-xl: Rounds the border corner of the element by xl
        ui.label("Temperature Converter").classes("text-2xl font-bold font-serif text-accent mb-4")
        # text-2xl: Sets the text size to xl
        # font-bold: Sets the text font type to bold
        # text-accent: Sets the text color to the accent color in our ui.colors
        # mb-4: Sets the bottom margin to 4
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-warning border-black")
        # w-full: Sets the width of the element to the full amount
        # border: Sets/creates border values
        # rounded: Sets rounded border
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded animate-pulse")
        # text-white: Changes text color to white
        # py-2: Sets y padding to 2
        # px-4: Sets x padding to 4
        result_label = ui.label("").classes("text-lg mt-4")
    with ui.card().classes("w-300 p-5 shadow-xl mx-auto mt-20 rounded-xl"):
        ui.label("Temperature Converter").classes("text-2xl font-bold font-serif text-accent mb-4")
        celc_dropdown = ui.select(["0", "10", "20", "30"], value="0")
        celc_label = ui.label("Select a celsius value.")
        convert_button2 = ui.button("Convert", on_click=celc_update_label).classes("text-white font-bold py-2 px-4 rounded animate-pulse")
ui.run()