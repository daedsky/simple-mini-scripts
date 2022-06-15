from pynput.keyboard import Listener
import pyautogui
from threading import Thread
from porn_sites import all as all_porn_sites


class PornKeystrokeBlocker:
    keys = []

    def on_press(self, key):
        try:
            word = "".join(self.keys)

            sites = all_porn_sites

            for site in sites:
                if site in word:
                    pyautogui.hotkey('ctrl', 'backspace')
                    pyautogui.press('backspace')
                    pyautogui.hotkey('ctrl', 'backspace')
                    pyautogui.hotkey('alt', 'f4')
                    self.keys = []

            self.keys.append(key.char)

        except Exception as e:
            pass

    def on_release(self, key):
        pass

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


if __name__ == "__main__":
    p = PornKeystrokeBlocker()
    t = Thread(target=p.start)
    t.start()
