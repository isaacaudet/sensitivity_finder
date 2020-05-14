import PySimpleGUI as sg


def low_val(starting, offset=0):
    return float(format((.5 + offset) * float(starting), '.2f'))


def high_val(starting, offset=0):
    return float(format((1.5 - offset) * float(starting), '.2f'))


def mid_val(starting, new):
    return float((starting + new) / 2)


sg.theme('Reddit')
# sg.preview_all_look_and_feel_themes()

layout = [
    [sg.Text('Starting Sensitivity'), sg.Input(key='-IN-', size=(8, 1)), sg.Button('Show'), sg.Text('Iteration:'),
     sg.Text(key='-ITER-', size=(4, 1))],
    [sg.Text('', size=(5, 1)), sg.Text('Lower', size=(8, 1), justification='center'),
     sg.Text('Mid', size=(8, 1), justification='center'),
     sg.Text('Upper', size=(8, 1), justification='center')],
    [sg.Button('Lower', key='-LOWER-'), sg.Text(key='-LOW-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER-')],
    [sg.Button('Lower', key='-LOWER1-'), sg.Text(key='-LOW1-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID1-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH1-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER1-')],
    [sg.Button('Lower', key='-LOWER2-'), sg.Text(key='-LOW2-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID2-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH2-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER2-')],
    [sg.Button('Lower', key='-LOWER3-'), sg.Text(key='-LOW3-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID3-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH3-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER3-')],
    [sg.Button('Lower', key='-LOWER4-'), sg.Text(key='-LOW4-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID4-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH4-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER4-')],
    [sg.Button('Lower', key='-LOWER5-'), sg.Text(key='-LOW5-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID5-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH5-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER5-')],
    [sg.Button('Lower', key='-LOWER6-'), sg.Text(key='-LOW6-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID6-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH6-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER6-')],
    [sg.Button('Lower', key='-LOWER7-'), sg.Text(key='-LOW7-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID7-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH7-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER7-')],
    [sg.Button('Lower', key='-LOWER8-'), sg.Text(key='-LOW8-', size=(8, 1), relief='groove'),
     sg.Text(key='-MID8-', size=(8, 1), relief='groove'),
     sg.Text(key='-HIGH8-', size=(8, 1), relief='groove'), sg.Button('Higher', key='-HIGHER8-')],
    [sg.Text('Final Sensitivity: ', justification='center'),
     sg.Text(key='-FINAL-', size=(8, 1), relief='groove', justification='center'),
     sg.Text('Previous Sensitivity: ', justification='center'),
     sg.Text(key='-PREV-', size=(8, 1), relief='groove', justification='center')],
    [sg.Button('Exit'), sg.Button('Clear')]]

window = sg.Window('Sensitivity Calculator', layout)
iteration_count = 0
mid = float()
high = float()
low = float()
keys_to_clear = ['-IN-', '-ITER-', '-HIGH-', '-MID-', '-LOW-', '-HIGH1-', '-MID1-', '-LOW1-', '-HIGH2-', '-MID2-',
                 '-LOW2-', '-HIGH3-', '-MID3-', '-LOW3-', '-HIGH4-', '-MID4-', '-LOW4-', '-HIGH5-', '-MID5-', '-LOW5-',
                 '-HIGH6-', '-MID6-', '-LOW6-', '-HIGH7-', '-MID7-', '-LOW7-', '-HIGH8-', '-MID8-', '-LOW8-', '-FINAL-']
while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Clear':
        iteration_count = 0
        window['-PREV-'].Update(format(float(mid), '.2f'))
        for key in keys_to_clear:
            window[key]('')
            window.FindElement(key).Update(text_color='black')

    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        iteration_count += 1
        mid = float(values['-IN-'])
        high = high_val(mid)
        low = low_val(mid)
        window['-ITER-'].update(iteration_count)
        window['-LOW-'].update(low)
        window['-MID-'].update(format(mid, '.2f'))
        window['-HIGH-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER-').Update(button_color=('white', '#07499D'))

    # iter 1

    if event == '-LOWER-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid)
        low = low_val(mid)
        window['-ITER-'].update(iteration_count)
        window['-LOW1-'].update(low)
        window['-MID1-'].update(format(mid, '.2f'))
        window['-HIGH1-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER1-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER1-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-HIGHER-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOWER-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW-').Update(text_color='#FE0303')

    if event == '-HIGHER-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid)
        low = low_val(mid)
        window['-MID1-'].update(format(mid, '.2f'))
        window['-LOW1-'].update(low)
        window['-HIGH1-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER1-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER1-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH-').Update(text_color='#FE0303')

    # iter 2

    if event == '-LOWER1-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .1)
        low = low_val(mid, .1)
        window['-ITER-'].update(iteration_count)
        window['-LOW2-'].update(low)
        window['-MID2-'].update(format(mid, '.2f'))
        window['-HIGH2-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-HIGHER1-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOWER1-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW1-').Update(text_color='#FE0303')

    if event == '-HIGHER1-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .1)
        low = low_val(mid, .1)
        window['-MID2-'].update(format(mid, '.2f'))
        window['-LOW2-'].update(low)
        window['-HIGH2-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-HIGHER1-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOWER1-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH1-').Update(text_color='#FE0303')
        # iter 2

    if event == '-LOWER2-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .2)
        low = low_val(mid, .2)
        window['-ITER-'].update(iteration_count)
        window['-LOW3-'].update(low)
        window['-MID3-'].update(format(mid, '.2f'))
        window['-HIGH3-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-HIGHER2-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOWER2-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW2-').Update(text_color='#FE0303')

    if event == '-HIGHER2-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .2)
        low = low_val(mid, .2)
        window['-MID3-'].update(format(mid, '.2f'))
        window['-LOW3-'].update(low)
        window['-HIGH3-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER2-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER2-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH2-').Update(text_color='#FE0303')

    # iter 3

    if event == '-LOWER3-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .3)
        low = low_val(mid, .3)
        window['-ITER-'].update(iteration_count)
        window['-LOW4-'].update(low)
        window['-MID4-'].update(format(mid, '.2f'))
        window['-HIGH4-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW3-').Update(text_color='#FE0303')

    if event == '-HIGHER3-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .3)
        low = low_val(mid, .3)
        window['-MID4-'].update(format(mid, '.2f'))
        window['-LOW4-'].update(low)
        window['-HIGH4-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER3-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER3-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH3-').Update(text_color='#FE0303')
    # iter 4

    if event == '-LOWER4-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .4)
        low = low_val(mid, .4)
        window['-ITER-'].update(iteration_count)
        window['-LOW5-'].update(low)
        window['-MID5-'].update(format(mid, '.2f'))
        window['-HIGH5-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW4-').Update(text_color='#FE0303')

    if event == '-HIGHER4-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .4)
        low = low_val(mid, .4)
        window['-MID5-'].update(format(mid, '.2f'))
        window['-LOW5-'].update(low)
        window['-HIGH5-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER4-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER4-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH4-').Update(text_color='#FE0303')
    # iter 5

    if event == '-LOWER5-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .45)
        low = low_val(mid, .45)
        window['-ITER-'].update(iteration_count)
        window['-LOW6-'].update(low)
        window['-MID6-'].update(format(mid, '.2f'))
        window['-HIGH6-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW5-').Update(text_color='#FE0303')

    if event == '-HIGHER5-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .45)
        low = low_val(mid, .45)
        window['-MID6-'].update(format(mid, '.2f'))
        window['-LOW6-'].update(low)
        window['-HIGH6-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER5-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER5-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH5-').Update(text_color='#FE0303')
    # iter 6

    if event == '-LOWER6-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .48)
        low = low_val(mid, .48)
        window['-ITER-'].update(iteration_count)
        window['-LOW7-'].update(low)
        window['-MID7-'].update(format(mid, '.2f'))
        window['-HIGH7-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW6-').Update(text_color='#FE0303')

    if event == '-HIGHER6-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .48)
        low = low_val(mid, .48)
        window['-MID7-'].update(format(mid, '.2f'))
        window['-LOW7-'].update(low)
        window['-HIGH7-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER6-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER6-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH6-').Update(text_color='#FE0303')
    # iter 7

    if event == '-LOWER7-':
        iteration_count += 1
        mid = mid_val(mid, low)
        high = high_val(mid, .49)
        low = low_val(mid, .49)
        window['-ITER-'].update(iteration_count)
        window['-LOW8-'].update(low)
        window['-MID8-'].update(format(mid, '.2f'))
        window['-HIGH8-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER8-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER8-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-LOW7-').Update(text_color='#FE0303')

    if event == '-HIGHER7-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = mid_val(mid, high)
        high = high_val(mid, .49)
        low = low_val(mid, .49)
        window['-MID8-'].update(format(mid, '.2f'))
        window['-LOW8-'].update(low)
        window['-HIGH8-'].update(high)
        # Change color of next buttons
        window.FindElement('-LOWER8-').Update(button_color=('white', '#07499D'))
        window.FindElement('-HIGHER8-').Update(button_color=('white', '#07499D'))
        # Change back color of previous buttons
        window.FindElement('-LOWER7-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGHER7-').Update(button_color=('white', '#0079d3'))
        # Change Text Color
        window.FindElement('-HIGH7-').Update(text_color='#FE0303')

    # iter 8

    if event == '-LOWER8-':
        iteration_count += 1
        mid = format((mid + high) / 2, '.2f')
        window['-ITER-'].update(iteration_count)
        window['-FINAL-'].update(mid)
        # Change back color of previous buttons
        window.FindElement('-HIGHER8-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOWER8-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOW8-').Update(text_color='#FE0303')

    if event == '-HIGHER8-':
        iteration_count += 1
        window['-ITER-'].update(iteration_count)
        mid = format((mid + high) / 2, '.2f')
        window['-FINAL-'].update(mid)
        # Change back color of previous buttons
        window.FindElement('-HIGHER8-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-LOWER8-').Update(button_color=('white', '#0079d3'))
        window.FindElement('-HIGH8-').Update(text_color='#FE0303')

window.close()
