# WindowGUI_025.py
from tkinter import *
import tkinter.messagebox

# �Լ� ����
def Msgbox1():
    tkinter.messagebox.showinfo("����",\
        "������ �˷��ִ� �뵵�� �޽��� ����\n(�Ķ��� i ������)")
def Msgbox2():
    tkinter.messagebox.showwarning("���",\
        "��� �˷��ִ� �뵵�� �޽��� ����\n(����� ����ǥ ������)")
def Msgbox3():
    tkinter.messagebox.showerror("����",\
        "������ �˷��ִ� �뵵�� �޽��� ����\n(������ X ������)")
def Msgbox4():
    tkinter.messagebox.askquestion("����",\
        "������ �Ҷ� ���� �߰� �ɼǿ� �޽��� ����\n(�Ķ��� ����ǥ ������)")
def Msgbox5():
    tkinter.messagebox.askokcancel("Ȯ��/���",\
        "Ȯ��(Ok)�� ���(Cancel) �� ����\n(�Ķ��� ����ǥ ������)")
def Msgbox6():
    tkinter.messagebox.askyesnocancel("��/�ƴϿ�/���",\
        "��(Yes), �ƴϿ�(No), ���(Cancel) �� ����\n(�Ķ��� ����ǥ ������)")
def Msgbox7():
    tkinter.messagebox.askretrycancel("�ٽýõ�/���",\
        "�ٽ� �õ�����, ��������� ���� �޽��� ����\n(����� ����ǥ ������)")
def close_win():
    win.destroy()
    win.quit()

# main
win = Tk()
win.title("�޽����ڽ�")
# ������ ����
base_frm = Frame(win)
base_frm.pack()
# ��ư ����
btn_info=Button(base_frm, text="Info", width="20", command=Msgbox1)
btn_info.pack(padx="50", pady="10")
btn_warning=Button(base_frm, text="Warning", width="20", command=Msgbox2)
btn_warning.pack(pady="10")
btn_error=Button(base_frm, text="Error", width="20", command=Msgbox3)
btn_error.pack(pady="10")
btn_ask_question=Button(base_frm, text="Question", width="20", command=Msgbox4)
btn_ask_question.pack(pady="10")
btn_ask_cancel=Button(base_frm, text="Ok/Cancel", width="20", command=Msgbox5)
btn_ask_cancel.pack(pady="10")
btn_ask_YNC=Button(base_frm, text="Yes/No/Cancel", width="20", command=Msgbox6)
btn_ask_YNC.pack(pady="10")
btn_ask_try=Button(base_frm, text="Try", width="20", command=Msgbox7)
btn_ask_try.pack(pady="10")
btn_cls=Button(base_frm, text="Close", width="20", command=close_win)
btn_cls.pack(pady="10")

win.mainloop()

