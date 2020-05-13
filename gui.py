import PySimpleGUI as sg


def low_val(starting, offset=0):
    return float(format((.5 + offset) * float(starting), '.2f'))


def high_val(starting, offset=0):
    return float(format((1.5 - offset) * float(starting), '.2f'))


def mid_val(starting, new):
    return float(format((starting + new) / 2, '.2f'))


sg.theme('Reddit')
# sg.preview_all_look_and_feel_themes()

layout = [
    [sg.Text('Starting Sensitivity'), sg.Input(key='-IN-', size=(8, 1)), sg.Button('Show'), sg.Text('Iteration:'),
     sg.Text(key='-ITER-', size=(4, 1), relief='groove')],
    [sg.Button('Lower', key='-LOWER-'), sg.Text(key='-LOW-', size=(8, 1), relief='groove'), sg.Text(key='-MID-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER-')],
    [sg.Button('Lower', key='-LOWER1-'), sg.Text(key='-LOW1-', size=(8, 1), relief='groove'), sg.Text(key='-MID1-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH1-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER1-')],
    [sg.Button('Lower', key='-LOWER2-'), sg.Text(key='-LOW2-', size=(8, 1), relief='groove'), sg.Text(key='-MID2-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH2-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER2-')],
    [sg.Button('Lower', key='-LOWER3-'), sg.Text(key='-LOW3-', size=(8, 1), relief='groove'), sg.Text(key='-MID3-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH3-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER3-')],
    [sg.Button('Lower', key='-LOWER4-'), sg.Text(key='-LOW4-', size=(8, 1), relief='groove'), sg.Text(key='-MID4-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH4-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER4-')],
    [sg.Button('Lower', key='-LOWER5-'), sg.Text(key='-LOW5-', size=(8, 1), relief='groove'), sg.Text(key='-MID5-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH5-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER5-')],
    [sg.Button('Lower', key='-LOWER6-'), sg.Text(key='-LOW6-', size=(8, 1), relief='groove'), sg.Text(key='-MID6-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH6-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER6-')],
    [sg.Button('Lower', key='-LOWER7-'), sg.Text(key='-LOW7-', size=(8, 1), relief='groove'), sg.Text(key='-MID7-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH7-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER7-')],
    [sg.Button('Lower', key='-LOWER8-'), sg.Text(key='-LOW8-', size=(8, 1), relief='groove'), sg.Text(key='-MID8-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH8-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER8-')],
    [sg.Text('Final Sensitivity: ', justification='center'), sg.Text(key='-FINAL-', size=(8, 1), relief='groove', justification='center')],
    [sg.Button('Exit')]]

window = sg.Window('Sensitivity Calculator', layout)
iteration_count = 0
mid = float()
high = float()
low = float()
print(sg.theme_button_color())
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        iteration_count += 1
        mid = float(values['-IN-'])
        high = high_val(mid)
        low = low_val(mid)
        window['-ITER-'].update(iteration_count)
        window['-LOW-'].update(low)
        window['-MID-'].update(mid)
        window['-HIGH-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER-').Update(button_color=('white', 'red'))



    # iter 1

    if event == '-LOWER-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid)
        low = low_val(mid)
        window['-ITER-'].update(iteration_count)
        window['-LOW1-'].update(low)
        window['-MID1-'].update(mid)
        window['-HIGH1-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER1-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER1-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid)
        low = low_val(mid)
        window['-MID1-'].update(mid)
        window['-LOW1-'].update(low)
        window['-HIGH1-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER1-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER1-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER-').Update(button_color=('white', '#0079d3'))

    # iter 2

    if event == '-LOWER1-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .1)
        low = low_val(mid, .1)
        window['-ITER-'].update(iteration_count)
        window['-LOW2-'].update(low)
        window['-MID2-'].update(mid)
        window['-HIGH2-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER1-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER1-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER1-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .1)
        low = low_val(mid, .1)
        window['-MID2-'].update(mid)
        window['-LOW2-'].update(low)
        window['-HIGH2-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER1-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER1-').Update(button_color=('white', '#0079d3'))
        # iter 2

    if event == '-LOWER2-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .2)
        low = low_val(mid, .2)
        window['-ITER-'].update(iteration_count)
        window['-LOW3-'].update(low)
        window['-MID3-'].update(mid)
        window['-HIGH3-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER2-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .2)
        low = low_val(mid, .2)
        window['-MID3-'].update(mid)
        window['-LOW3-'].update(low)
        window['-HIGH3-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', '#0079d3'))

    # iter 3

    if event == '-LOWER3-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .3)
        low = low_val(mid, .3)
        window['-ITER-'].update(iteration_count)
        window['-LOW4-'].update(low)
        window['-MID4-'].update(mid)
        window['-HIGH4-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER3-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .3)
        low = low_val(mid, .3)
        window['-MID4-'].update(mid)
        window['-LOW4-'].update(low)
        window['-HIGH4-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', '#0079d3'))
    # iter 4

    if event == '-LOWER4-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .4)
        low = low_val(mid, .4)
        window['-ITER-'].update(iteration_count)
        window['-LOW5-'].update(low)
        window['-MID5-'].update(mid)
        window['-HIGH5-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER4-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .4)
        low = low_val(mid, .4)
        window['-MID5-'].update(mid)
        window['-LOW5-'].update(low)
        window['-HIGH5-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', '#0079d3'))
    # iter 5

    if event == '-LOWER5-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .45)
        low = low_val(mid, .45)
        window['-ITER-'].update(iteration_count)
        window['-LOW6-'].update(low)
        window['-MID6-'].update(mid)
        window['-HIGH6-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER5-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .45)
        low = low_val(mid, .45)
        window['-MID6-'].update(mid)
        window['-LOW6-'].update(low)
        window['-HIGH6-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', '#0079d3'))
    # iter 6

    if event == '-LOWER6-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .48)
        low = low_val(mid, .48)
        window['-ITER-'].update(iteration_count)
        window['-LOW7-'].update(low)
        window['-MID7-'].update(mid)
        window['-HIGH7-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER6-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .48)
        low = low_val(mid, .48)
        window['-MID7-'].update(mid)
        window['-LOW7-'].update(low)
        window['-HIGH7-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', '#0079d3'))
    # iter 7

    if event == '-LOWER7-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .49)
        low = low_val(mid, .49)
        window['-ITER-'].update(iteration_count)
        window['-LOW8-'].update(low)
        window['-MID8-'].update(mid)
        window['-HIGH8-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER8-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER8-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER7-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .49)
        low = low_val(mid, .49)
        window['-MID8-'].update(mid)
        window['-LOW8-'].update(low)
        window['-HIGH8-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER8-').Update(button_color=('white', 'red'))
        window.FindElement('-HIGHER8-').Update(button_color=('white', 'red'))
        # Change back color of previous buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', '#0079d3'))

    # iter 8

    if event == '-LOWER8-':
        iteration_count += 1
        mid += low
        mid = mid / 2
        window['-ITER-'].update(iteration_count)
        window['-FINAL-'].update(mid)
        # Change back color of previous buttons
        window.FindElement('-LOWER8-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER8-').Update(button_color=('white', '#0079d3'))

    if event == '-HIGHER8-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid += high
        mid = mid / 2
        window['-FINAL-'].update(mid)
        # Change back color of previous buttons
        window.FindElement('-LOWER8-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER8-').Update(button_color=('white', '#0079d3'))

window.close()
