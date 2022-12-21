
#               ***************Importando Lib**************
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#                    ***************Cores**************
cor1 = "#1E1F1E" #Cor preta
cor2 = "#FEFFFF" #Cor branca
cor3 = "#38576B" #Cor azul
cor4 = "#ECEFF1" #Cor cinza
cor5 = "#FFAB40" #Cor laranja

#               ***************Criando janela**************
janela =Tk()
janela.title("Calculadora") 
janela.geometry("255x320") #tamanho da calculadora
janela.config(bg=cor1) #cor do fundo da janela

#               ***************Criando frames**************
frame_tela = Frame(janela, width=255, height=50, bg=cor3) #frame do visor da calculadora
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=255, height=275) #frame do "corpo" da calculadora
frame_corpo.grid(row=1, column=0)


todos_valores = '' #Variavel todos valores

valor_texto = StringVar() 

#               ***************Criando funções**************

#função para entrar valores na label 
def entrar_valores(event):

  global todos_valores 
  todos_valores = todos_valores + str(event)
  
  #passando valor para tela
  valor_texto.set(todos_valores)
  
#função para calcular os valores
def calcular():
  global todos_valores
  try:
    resultado = str(eval(todos_valores))  
    valor_texto.set(resultado)
                    
  except ZeroDivisionError as ERROR:
      limpar_tela()

      valor_texto.set("Não divide por 0")
      
  
#função limpar tela

def limpar_tela():
  global todos_valores
  todos_valores =""
  valor_texto.set("0")

#Criando label 
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 17'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#               ***************Criando botões**************
#Botões da primeira linha

b1 = Button(frame_corpo,command = limpar_tela, text="C", width=9, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao clean da calculadora
b1.place(x=0, y=0) # x = horizontal e y = vertical

b2 = Button(frame_corpo, command = lambda: entrar_valores('%'),text="%", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao porcentagem da calculadora
b2.place(x=118, y=0) # x = horizontal e y = vertical

b3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao divisão da calculadora
b3.place(x=177, y=0) # x = horizontal e y = vertical 

#Botões da segunda linha

b4 = Button(frame_corpo, command = lambda: entrar_valores('7'),text="7", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 7 da calculadora
b4.place(x=0, y=55) # x = horizontal e y = vertical

b5 = Button(frame_corpo,command = lambda: entrar_valores('8'), text="8", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 8 da calculadora
b5.place(x=59, y=55) # x = horizontal e y = vertical

b6 = Button(frame_corpo,command = lambda: entrar_valores('9'), text="9", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 9 da calculadora
b6.place(x=118, y=55) # x = horizontal e y = vertical

b7 = Button(frame_corpo,command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao multiplicação da calculadora
b7.place(x=177, y=55) # x = horizontal e y = vertical 

#Botões da terceira linha

b8 = Button(frame_corpo,command = lambda: entrar_valores('4'), text="4", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 4 da calculadora
b8.place(x=0, y=110) # x = horizontal e y = vertical

b9 = Button(frame_corpo,command = lambda: entrar_valores('5'), text="5", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 5 da calculadora
b9.place(x=59, y=110) # x = horizontal e y = vertical

b10 = Button(frame_corpo, command = lambda: entrar_valores('6'),text="6", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 6 da calculadora
b10.place(x=118, y=110) # x = horizontal e y = vertical

b11 = Button(frame_corpo, command = lambda: entrar_valores('-'),text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao subtração da calculadora
b11.place(x=177, y=110) # x = horizontal e y = vertical 

#Botões da quarta linha

b12 = Button(frame_corpo, command = lambda: entrar_valores('1'),text="1", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 1 da calculadora
b12.place(x=0, y=165) # x = horizontal e y = vertical

b13 = Button(frame_corpo, command = lambda: entrar_valores('2'),text="2", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 2 da calculadora
b13.place(x=59, y=165) # x = horizontal e y = vertical

b14 = Button(frame_corpo, command = lambda: entrar_valores('3'),text="3", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 3 da calculadora
b14.place(x=118, y=165) # x = horizontal e y = vertical

b15 = Button(frame_corpo, command = lambda: entrar_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao soma da calculadora
b15.place(x=177, y=165) # x = horizontal e y = vertical 

#Botões da quinta linha

b16 = Button(frame_corpo,command = lambda: entrar_valores('0'), text="0", width=9, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao 0 da calculadora
b16.place(x=0, y=220) # x = horizontal e y = vertical

b17 = Button(frame_corpo,command = lambda: entrar_valores('.'), text=".", width=3, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao pontuação da calculadora
b17.place(x=118, y=220) # x = horizontal e y = vertical

b18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao igual da calculadora
b18.place(x=177, y=220) # x = horizontal e y = vertical 

janela.mainloop()