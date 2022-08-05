from pynput.keyboard import Key, Listener
import pyautogui

save_path = "YOUR_SAVE_PATH"  # for example 'D:\\programming\\circuits\\hw_{}.png'

im_num = 0


def key_handle(key):
    global im_num, save_path
    if key == Key.f3:
        im_num += 1

    elif key == Key.f4:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(save_path.format(im_num))
    elif key == Key.f5:
        print(save_path.format(im_num))
    elif key == Key.f6:
        exit(0)


if __name__ == '__main__':
    listener = Listener(on_release=key_handle)
    listener.start()
    listener.join()
