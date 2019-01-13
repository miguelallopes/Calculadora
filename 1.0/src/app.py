#Módulos a importar
from tkinter import *
from math import pi
from math import sqrt
from math import factorial

#Abertura
from turtle import TurtleScreen, RawTurtle, TK as TKInit
from time import sleep

def main():
    root1 = TKInit.Tk()
    root1.title('Calculadora')
    try:
        root1.wm_iconbitmap('assents\calculadoralogo.ico')
    except:
        print('Ocorreu um erro interno!')
    cv1 = TKInit.Canvas(root1, width=270, height=186, bg="#ddffff")
    cv2 = TKInit.Canvas(root1, width=270, height=186, bg="#ffeeee")
    cv1.pack()
    cv2.pack()

    s1 = TurtleScreen(cv1)
    s1.bgcolor(0.85, 0.85, 1)
    s2 = TurtleScreen(cv2)
    s2.bgcolor(1, 0.85, 0.85)

    p = RawTurtle(s1)
    q = RawTurtle(s2)

    p.color("red", (1, 0.85, 0.85))
    p.width(3)
    q.color("blue", (0.85, 0.85, 1))
    q.width(3)

    for t in p,q:
        t.shape("turtle")
        t.lt(270)

    q.lt(0)

    for t in p, q:
        t.begin_fill()
        t.fd(5)
        t.lt(0)

        t.fd(20)
        sleep(0.1)

    p.write('     Carregando Módulos...')
    for t in p,q:
        t.end_fill()
        t.lt(0)
        sleep(0.5)
        q.write('     Iniciando Módulos...')
        sleep(0.5)
        t.bk(0)
        t.fd(360)
    root1.destroy()

main()

#Variáveis(Objetos e Funções)
root = Tk()

screen1state = None
screen2state = None

screenwidth = 28
buttonwidth = 7

#Funções
def media(*num):
    medialist = list(num)
    tnum = 0
    for n in medialist:
         tnum += n
    valoresmedialist = len(medialist)
    total = tnum / valoresmedialist
    return total

#Interface

class App:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        #Frames do ecrã da calculadora
        self.framescreen1 = Frame(master)
        self.framescreen1['padx'] = 20
        self.framescreen1['pady'] = 5
        self.framescreen1.pack()

        self.framescreen2 = Frame(master)
        self.framescreen2['padx'] = 20
        self.framescreen2['pady'] = 5
        self.framescreen2.pack()

        #Frame dos botões da calculadora
        self.framebutton1 = Frame(master)
        self.framebutton1['padx'] = 20
        self.framebutton1['pady'] = 5
        self.framebutton1.pack()

        self.framebuttonant = Frame(master)
        self.framebuttonant['padx'] = 20
        self.framebuttonant['pady'] = 5
        self.framebuttonant.pack()

        self.framebuttonfunction = Frame(master)
        self.framebuttonfunction['padx'] = 20
        self.framebuttonfunction['pady'] = 5
        self.framebuttonfunction.pack()

        self.framebuttonfunction2 = Frame(master)
        self.framebuttonfunction2['padx'] = 20
        self.framebuttonfunction2['pady'] = 5
        self.framebuttonfunction2.pack()

        self.framebuttonfunction3 = Frame(master)
        self.framebuttonfunction3['padx'] = 20
        self.framebuttonfunction3['pady'] = 5
        self.framebuttonfunction3.pack()

        self.framebuttonapos = Frame(master)
        self.framebuttonapos['padx'] = 20
        self.framebuttonapos['pady'] = 5
        self.framebuttonapos.pack()

        self.framebutton2 = Frame(master)
        self.framebutton2['padx'] = 20
        self.framebutton2['pady'] = 5
        self.framebutton2.pack()

        self.framebutton3 = Frame(master)
        self.framebutton3['padx'] = 20
        self.framebutton3['pady'] = 5
        self.framebutton3.pack()

        self.framebutton4 = Frame(master)
        self.framebutton4['padx'] = 20
        self.framebutton4['pady'] = 5
        self.framebutton4.pack()

        self.framebutton5 = Frame(master)
        self.framebutton5['padx'] = 20
        self.framebutton5['pady'] = 5
        self.framebutton5.pack()

        #Ecrã da calculadora
        self.screen1 = Label(self.framescreen1, text='', font=self.fonte, width=screenwidth)
        self.screen1.pack()

        self.screen2 = Label(self.framescreen2, text='0', font=self.fonte, width=screenwidth)
        self.screen2.pack()

        #Botões da calculadora
        self.buttonClearAll = Button(self.framebutton1, text="AC", font=self.fonte, width=buttonwidth)
        self.buttonClearAll["command"] = self.ClearAll
        self.buttonClearAll.pack(side=LEFT)

        self.buttonClearOne = Button(self.framebutton1, text="C", font=self.fonte, width=buttonwidth)
        self.buttonClearOne["command"] = self.ClearOne
        self.buttonClearOne.pack(side=LEFT)

        self.buttonPowerOff = Button(self.framebutton1, text="OFF", font=self.fonte, width=buttonwidth)
        self.buttonPowerOff["command"] = root.destroy
        self.buttonPowerOff.pack(side=LEFT)

        self.lblant = Label(self.framebuttonant, text='', font=self.fonte, width=buttonwidth * 4)
        self.lblant.pack()

        self.buttonelevado2 = Button(self.framebuttonfunction, text="x²", font=self.fonte, width=buttonwidth)
        self.buttonelevado2["command"] = self.ButtonElevado2
        self.buttonelevado2.pack(side=LEFT)

        self.buttonelevadooutro = Button(self.framebuttonfunction, text="xⁿ", font=self.fonte, width=buttonwidth)
        self.buttonelevadooutro["command"] = self.ButtonElevadoOutro
        self.buttonelevadooutro.pack(side=LEFT)

        self.buttonRaízQuadrada = Button(self.framebuttonfunction, text="√", font=self.fonte, width=buttonwidth)
        self.buttonRaízQuadrada["command"] = self.ButtonRaízQuadrada
        self.buttonRaízQuadrada.pack(side=LEFT)

        self.buttonSeven = Button(self.framebuttonfunction2, text="(", font=self.fonte, width=buttonwidth)
        self.buttonSeven["command"] = self.ButtonParentese1
        self.buttonSeven.pack(side=LEFT)

        self.buttonSeven = Button(self.framebuttonfunction2, text=")", font=self.fonte, width=buttonwidth)
        self.buttonSeven["command"] = self.ButtonParentese2
        self.buttonSeven.pack(side=LEFT)

        self.buttonPi = Button(self.framebuttonfunction2, text="π", font=self.fonte, width=buttonwidth)
        self.buttonPi["command"] = self.ButtonPi
        self.buttonPi.pack(side=LEFT)

        self.buttonPi = Button(self.framebuttonfunction2, text=",", font=self.fonte, width=buttonwidth)
        self.buttonPi["command"] = self.ButtonVirgula
        self.buttonPi.pack(side=RIGHT)

        self.buttonFactorial = Button(self.framebuttonfunction3, text="Factorial", font=self.fonte, width=buttonwidth)
        self.buttonFactorial["command"] = self.ButtonFactorial
        self.buttonFactorial.pack(side=LEFT)

        self.buttonMedia = Button(self.framebuttonfunction3, text="Média", font=self.fonte, width=buttonwidth)
        self.buttonMedia["command"] = self.ButtonMedia
        self.buttonMedia.pack(side=LEFT)

        self.lblapos = Label(self.framebuttonapos, text='', font=self.fonte, width=buttonwidth * 4)
        self.lblapos.pack()

        self.buttonSeven = Button(self.framebutton2, text="7", font=self.fonte, width=buttonwidth)
        self.buttonSeven["command"] = self.ButtonSeven
        self.buttonSeven.pack(side=LEFT)

        self.buttonEight = Button(self.framebutton2, text="8", font=self.fonte, width=buttonwidth)
        self.buttonEight["command"] = self.ButtonEight
        self.buttonEight.pack(side=LEFT)

        self.buttonNine = Button(self.framebutton2, text="9", font=self.fonte, width=buttonwidth)
        self.buttonNine["command"] = self.ButtonNine
        self.buttonNine.pack(side=LEFT)

        self.buttonMais = Button(self.framebutton2, text="+", font=self.fonte, width=buttonwidth)
        self.buttonMais["command"] = self.ButtonMais
        self.buttonMais.pack(side=RIGHT)

        self.buttonFour = Button(self.framebutton3, text="4", font=self.fonte, width=buttonwidth)
        self.buttonFour["command"] = self.ButtonFour
        self.buttonFour.pack(side=LEFT)

        self.buttonFive = Button(self.framebutton3, text="5", font=self.fonte, width=buttonwidth)
        self.buttonFive["command"] = self.ButtonFive
        self.buttonFive.pack(side=LEFT)

        self.buttonSix = Button(self.framebutton3, text="6", font=self.fonte, width=buttonwidth)
        self.buttonSix["command"] = self.ButtonSix
        self.buttonSix.pack(side=LEFT)

        self.buttonMenos = Button(self.framebutton3, text="-", font=self.fonte, width=buttonwidth)
        self.buttonMenos["command"] = self.ButtonMenos
        self.buttonMenos.pack(side=RIGHT)

        self.buttonOne = Button(self.framebutton4, text="1", font=self.fonte, width=buttonwidth)
        self.buttonOne["command"] = self.ButtonOne
        self.buttonOne.pack(side=LEFT)

        self.buttonTwo = Button(self.framebutton4, text="2", font=self.fonte, width=buttonwidth)
        self.buttonTwo["command"] = self.ButtonTwo
        self.buttonTwo.pack(side=LEFT)

        self.buttonThree = Button(self.framebutton4, text="3", font=self.fonte, width=buttonwidth)
        self.buttonThree["command"] = self.ButtonThree
        self.buttonThree.pack(side=LEFT)

        self.buttonMultiplicar = Button(self.framebutton4, text="×", font=self.fonte, width=buttonwidth)
        self.buttonMultiplicar["command"] = self.ButtonMultiplicar
        self.buttonMultiplicar.pack(side=RIGHT)

        self.buttonZero = Button(self.framebutton5, text="0", font=self.fonte, width=buttonwidth)
        self.buttonZero["command"] = self.ButtonZero
        self.buttonZero.pack(side=LEFT)

        self.buttonPoint = Button(self.framebutton5, text=".", font=self.fonte, width=buttonwidth)
        self.buttonPoint["command"] = self.ButtonPoint
        self.buttonPoint.pack(side=LEFT)

        self.buttonIgual = Button(self.framebutton5, text="=", font=self.fonte, width=buttonwidth)
        self.buttonIgual["command"] = self.ButtonIgual
        self.buttonIgual.pack(side=LEFT)

        self.buttonDividir = Button(self.framebutton5, text="÷", font=self.fonte, width=buttonwidth)
        self.buttonDividir["command"] = self.ButtonDividir
        self.buttonDividir.pack(side=RIGHT)


    #Funções
    def ClearAll(self):
        self.screen1.configure(text='')
        self.screen2.configure(text='0')

    def ClearOne(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            if self.screen1['text'] == '':
                pass
            else:
                screen1state = self.screen1['text']
                screen1state = screen1state[:-1]
                self.screen1.configure(text=screen1state)

    def ButtonPi(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + f'{pi}')

    def ButtonRaízQuadrada(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + 'sqrt(')

    def ButtonMedia(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + 'media(')

    def ButtonElevado2(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '**2')

    def ButtonElevadoOutro(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '**')

    def ButtonFactorial(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + 'factorial(')

    def ButtonParentese1(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '(')

    def ButtonParentese2(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + ')')

    def ButtonVirgula(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + ',')

    def ButtonMais(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '+')

    def ButtonMenos(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '-')

    def ButtonMultiplicar(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '*')

    def ButtonDividir(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state + '/')

    def ButtonIgual(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            try:
                self.screen2.configure(text=str(eval(screen1state)))
            except:
                self.screen1.configure(text='Syntax Error!')
                self.screen2.configure(text='')

    def ButtonPoint(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'.')

    def ButtonZero(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'0')

    def ButtonOne(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'1')

    def ButtonTwo(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'2')

    def ButtonThree(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'3')

    def ButtonFour(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'4')

    def ButtonFive(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'5')

    def ButtonSix(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'6')

    def ButtonSeven(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'7')

    def ButtonEight(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'8')

    def ButtonNine(self):
        if self.screen1['text'] == 'Syntax Error!':
            pass
        else:
            screen1state = self.screen1['text']
            self.screen1.configure(text=screen1state+'9')

#Informações da aplicação
root.title('Calculadora')

#Configurações da aplicação
root.resizable(width=540, height=186)


#Icone da aplicação
try:
    root.wm_iconbitmap('assents\calculadoralogo.ico')
except:
    print('Ocorreu um erro interno!')

#Desenhar a interface
App(root)
root.mainloop()
