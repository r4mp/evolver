#/bin/python
# -*- coding: utf-8 -*-

__author__    = 'Gerrit Giehl <gerrit.giehl@email-versand.net>'
__contact__   = 'gerrit.giehl@email-versand.net'
__date__      = '29 March 2015'


import sys
import os.path

from loginframe import LoginFrame
from helper import Helper

try:
    from gi.repository import Gtk
except:
    print("GTK Not Available")
    sys.exit(1)

APPDIR = os.path.dirname(os.path.abspath(__file__))

class MyWindow(Gtk.Window):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("assets/ui/evolver.glade")
        self.window = self.builder.get_object("windowMain")
        self.dic = {}
        self.frameSearch = self.builder.get_object("frameSearch")

        if self.window:
            self.window.connect("destroy", Gtk.main_quit)
            self.loginFrame = LoginFrame(self.builder, self.dic)

        self.dic.update({
            "on_imagemenuitemQuit_activate" : self.quit,
            "on_buttonAdd_clicked" : self.add,
            "on_windowMain_destroy": self.quit,
        })

        self.builder.connect_signals(self.dic)

    def quit(self, widget):
        sys.exit(0)


if __name__ == '__main__':
    win = MyWindow()
    win.window.show()
    Gtk.main()
