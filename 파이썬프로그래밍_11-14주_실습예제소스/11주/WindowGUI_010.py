# WindowGUI_010.py
from tkinter import *

window = Tk()
window.geometry("640x400")
window.resizable(True, True)
window.title("Text ��Ʈ�� ����ϱ�")

text = Text(window)
text.insert(CURRENT, "�ȳ��ϼ���.\n") # CURRENT�� Ŀ���� ���� ��ġ�� ����Ŵ
text.insert(CURRENT, "�ݰ����ϴ�.")
text.insert(2.0, "�ſ� ")    # 2.0 �� 2��° �� ù��° ���� ��ġ�� ����Ŵ

text.pack()

text.tag_add("����", "1.0", "1.6")
text.tag_config("����", background="light green")
text.tag_remove("����", "1.1", "1.2")

window.mainloop()

