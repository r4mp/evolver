import sys

class LoginFrame(object):

    def __init__(self, builder, dic):
        self.builder = builder
        self.dic = dic

        self.frameLogin = self.builder.get_object("frameLogin")
        self.paned1 = self.builder.get_object("paned1")
        
        self.linkbuttonResetPassword = self.builder.get_object("linkbuttonResetPassword")
        self.linkbuttonResetPassword.set_label("Reset Password")
    
        self.paned1.add(self.frameLogin)
        
        self.dic.update({
            "on_buttonLogin_clicked" : self.login,
        })
        
    def login(self, widget):
        sys.exit(0) 
