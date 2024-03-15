import pyautogui
import webbrowser
import time


tipoA = [
    "291023431533714/",
    "1177563919046807",
    "2181698618663963",
    "499150751918738",
    "1708408125934238",
    "CasasInmueblesVentaRentaChihuahua",
    "986907898096489",
    "873418623570687",
    "223923178253429",
    "2229502370620610",
    "198564130574862",
    "1190596824475178",
    "623641318133093",
    "500097517751230",
    "544406562760209",
    "625587830903523",
    
]

tipoB = [
    "880774768956092/",
    "361748050852994/",
    "361748050852994/",
    "1502792500008296/",
    "685724071967118/",
    "462008994826589/",
    "h613735356021981/",
    "664924183604743/",
    "1934475956803265/",
    "943478485765428/",
                                # "482495098893972/ -----------------------------",
                                # "168694743743036",
                                # "646549472687341",
                                # "275912376196539",
    # "291056657659117",
                                    # "TerrenosChihuahua",
                                # "469308887335336",
    "1999901403562987",
    "884843275343758",
    "468410970359736",
    "707062663352022",
    "877226983009797",
    "221367584676123",
    "411197747430583",
    "234598563864750",
    "sichinmobiliaria",
    "332099667663913",
    "171750986622424",
    "2009141792646189",
    "150262495374841",
    "411101062694679",
    "494583453898689",
    "1769792103157997",
    "1589560057932781",
    "ventadecasasenchihuahua",
    "394238037379125",
    "1436297839943804",
    "371469740644550",
    "179362146216895",
    "427716181591922",
    "1452980664995539",
    "2290820314540615",
    "Inmuebla.Ideal",
    "117450205608487",
    "807545789298753",
    "ventacasas30"
]

postFile = "./publicaciones/primer.txt"


def posting(postFile: str)->None:
    x,y = pyautogui.size()
    pyautogui.click(770,550)
    time.sleep(2)
    pyautogui.click(770,637)
    time.sleep(2)
    pyautogui.click(700,500)
    time.sleep(2)
    with open(postFile,"r") as file:
        content = file.read()
        pyautogui.typewrite(content)
        time.sleep(3)
        pyautogui.click(950,880)
        time.sleep(3)

    # pyautogui.hotkey('ctrl','v')

def publishPost(url: str, group: str) -> None:
    currentUrl = url + group
    webbrowser.open(currentUrl)
    time.sleep(3)
    posting(postFile)
    return

def main():
    urlPrefix = "https://www.facebook.com/groups/"  

    # for _ in tipoA:
    for _ in tipoB:
        pyautogui.moveTo(10,10)
        publishPost(urlPrefix,_)
        
    pyautogui.click(1910,0)
        
    
    



if __name__ == "__main__":
    main()