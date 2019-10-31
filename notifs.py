
from win10toast import ToastNotifier
toast=ToastNotifier()

def loginSuccess(userName):
    toast.show_toast("Light","Welcome "+userName,duration=3)

def notify(t):
    toast.show_toast(t,duration=3)




