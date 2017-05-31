from tkinter import  *
from synth import constantes as ctes
from synth import sintetizador as sintetizador

class Gui:
    def __init__(self, master=None):


        self.fontePadrao = ("Arial", "10")
        self.mainContainer = Frame(master)
        self.mainContainer["pady"] = 10
        self.mainContainer.pack()

        self.nomeArquivoContainer = Frame(master)
        self.nomeArquivoContainer["padx"] = 20
        self.nomeArquivoContainer.pack()

        self.tempoSimulacaoContainer = Frame(master)
        self.tempoSimulacaoContainer["padx"] = 20
        self.tempoSimulacaoContainer.pack()

        self.variacaoF0Container = Frame(master)
        self.variacaoF0Container["padx"] = 20
        self.variacaoF0Container.pack()

        self.variacaoKContainer = Frame(master)
        self.variacaoKContainer["padx"] = 20
        self.variacaoKContainer.pack()

        self.ganhoRuidoContainer = Frame(master)
        self.ganhoRuidoContainer["padx"] = 20
        self.ganhoRuidoContainer.pack()

        self.anContainer = Frame(master)
        self.anContainer["padx"] = 20
        self.anContainer.pack()

        self.a1Container = Frame(master)
        self.a1Container["padx"] = 20
        self.a1Container.pack()

        self.b4Container = Frame(master)
        self.b4Container["padx"] = 20
        self.anContainer.pack()

        self.b5Container = Frame(master)
        self.b5Container["padx"] = 20
        self.b5Container.pack()

        self.fgpContainer = Frame(master)
        self.fgpContainer["padx"] = 20
        self.fgpContainer.pack()

        self.bgpContainer = Frame(master)
        self.bgpContainer["padx"] = 20
        self.bgpContainer.pack()

        self.fgzContainer = Frame(master)
        self.fgzContainer["padx"] = 20
        self.fgzContainer.pack()

        self.bgzContainer = Frame(master)
        self.bgzContainer["padx"] = 20
        self.bgzContainer.pack()

        self.fnpContainer = Frame(master)
        self.fnpContainer["padx"] = 20
        self.fnpContainer.pack()

        self.bnpContainer = Frame(master)
        self.bnpContainer["padx"] = 20
        self.bnpContainer.pack()

        self.bnzContainer = Frame(master)
        self.bnzContainer["padx"] = 20
        self.bnzContainer.pack()

        self.fgsContainer = Frame(master)
        self.fgsContainer["padx"] = 20
        self.fgsContainer.pack()

        self.bgsContainer = Frame(master)
        self.bgsContainer["padx"] = 20
        self.bgsContainer.pack()

        self.f0Container = Frame(master)
        self.f0Container["padx"] = 20
        self.f0Container.pack()

        self.f1Container = Frame(master)
        self.f1Container["padx"] = 20
        self.f1Container.pack()

        self.b1Container = Frame(master)
        self.b1Container["padx"] = 20
        self.b1Container.pack()

        self.f2Container = Frame(master)
        self.f2Container["padx"] = 20
        self.f2Container.pack()

        self.b2Container = Frame(master)
        self.b2Container["padx"] = 20
        self.b2Container.pack()

        self.f3Container = Frame(master)
        self.f3Container["padx"] = 20
        self.f3Container.pack()

        self.b3Container = Frame(master)
        self.b3Container["padx"] = 20
        self.b3Container.pack()

        self.sintetizarContainer = Frame(master)
        self.sintetizarContainer["pady"] = 20
        self.sintetizarContainer.pack()

        self.titulo = Label(self.mainContainer, text="Sintetizador de voz")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeArquivoLabel = Label(self.nomeArquivoContainer, text="Nome do arquivo", font=self.fontePadrao)
        self.nomeArquivoLabel.pack(side=LEFT)
        self.nomeArquivo = Entry(self.nomeArquivoContainer)
        self.nomeArquivo["width"] = 30
        self.nomeArquivo["font"] = self.fontePadrao
        self.nomeArquivo.pack(side=LEFT)

        self.tempoSimulacaoLabel = Label(self.tempoSimulacaoContainer, text="Tempo de simulação (s)", font=self.fontePadrao)
        self.tempoSimulacaoLabel.pack(side=LEFT)
        self.tempoSimulacao = Entry(self.tempoSimulacaoContainer, textvariable=StringVar(root, value=str(ctes.Gerais.TEMPO_SIMULACAO)))
        self.tempoSimulacao["width"] = 30
        self.tempoSimulacao["font"] = self.fontePadrao
        self.tempoSimulacao.pack(side=LEFT)

        self.variacaoF0Label = Label(self.variacaoF0Container, text="Variação máxima de F0 (1 sendo o máximo)",
                                         font=self.fontePadrao)
        self.variacaoF0Label.pack(side=LEFT)
        self.variacaoF0 = Entry(self.variacaoF0Container,
                                    textvariable=StringVar(root, value=str(ctes.Gerais.VARIACAO_F0)))
        self.variacaoF0["width"] = 30
        self.variacaoF0["font"] = self.fontePadrao
        self.variacaoF0.pack(side=LEFT)

        self.variacaoKLabel = Label(self.variacaoKContainer, text="Variação máxima de k (1 sendo o máximo)",
                                     font=self.fontePadrao)
        self.variacaoKLabel.pack(side=LEFT)
        self.variacaoK = Entry(self.variacaoKContainer,
                                textvariable=StringVar(root, value=str(ctes.Gerais.VARIACAO_K)))
        self.variacaoK["width"] = 30
        self.variacaoK["font"] = self.fontePadrao
        self.variacaoK.pack(side=LEFT)

        self.ganhoRuidoLabel = Label(self.ganhoRuidoContainer, text="Ganho do ruído (1 sendo o máximo)",
                                    font=self.fontePadrao)
        self.ganhoRuidoLabel.pack(side=LEFT)
        self.ganhoRuido = Entry(self.ganhoRuidoContainer,
                               textvariable=StringVar(root, value=str(ctes.Gerais.GANHO_RUIDO)))
        self.ganhoRuido["width"] = 30
        self.ganhoRuido["font"] = self.fontePadrao
        self.ganhoRuido.pack(side=LEFT)

        self.anLabel = Label(self.anContainer, text="AN", font=self.fontePadrao)
        self.anLabel.pack(side=LEFT)
        self.an = Entry(self.anContainer, textvariable= StringVar(root, value=str(ctes.ParametrosConstantes.AN)))
        self.an["width"] = 30
        self.an["font"] = self.fontePadrao
        self.an.pack(side=LEFT)

        self.f1Label = Label(self.f1Container, text="F1", font=self.fontePadrao)
        self.f1Label.pack(side=LEFT)
        self.f1 = Entry(self.f1Container, textvariable=StringVar(root, value=str(ctes.VogalA.F1)))
        self.f1["width"] = 30
        self.f1["font"] = self.fontePadrao
        self.f1.pack(side=LEFT)

        self.a1Label = Label(self.a1Container, text="A1", font=self.fontePadrao)
        self.a1Label.pack(side=LEFT)
        self.a1 = Entry(self.a1Container, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.A1)))
        self.a1["width"] = 30
        self.a1["font"] = self.fontePadrao
        self.a1.pack(side=LEFT)

        self.b1Label = Label(self.b1Container, text="B1", font=self.fontePadrao)
        self.b1Label.pack(side=LEFT)
        self.b1 = Entry(self.b1Container, textvariable=StringVar(root, value=str(ctes.VogalA.B1)))
        self.b1["width"] = 30
        self.b1["font"] = self.fontePadrao
        self.b1.pack(side=LEFT)

        self.b4Label = Label(self.b4Container, text="B4", font=self.fontePadrao)
        self.b4Label.pack(side=LEFT)
        self.b4 = Entry(self.b4Container, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.B4)))
        self.b4["width"] = 30
        self.b4["font"] = self.fontePadrao
        self.b4.pack(side=LEFT)

        self.f2Label = Label(self.f2Container, text="F2", font=self.fontePadrao)
        self.f2Label.pack(side=LEFT)
        self.f2 = Entry(self.f2Container, textvariable=StringVar(root, value=str(ctes.VogalA.F2)))
        self.f2["width"] = 30
        self.f2["font"] = self.fontePadrao
        self.f2.pack(side=LEFT)

        self.b5Label = Label(self.b5Container, text="B4", font=self.fontePadrao)
        self.b5Label.pack(side=LEFT)
        self.b5 = Entry(self.b5Container, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.B5)))
        self.b5["width"] = 30
        self.b5["font"] = self.fontePadrao
        self.b5.pack(side=LEFT)

        self.fgpLabel = Label(self.fgpContainer, text="B4", font=self.fontePadrao)
        self.fgpLabel.pack(side=LEFT)
        self.fgp = Entry(self.fgpContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.B5)))
        self.fgp["width"] = 30
        self.fgp["font"] = self.fontePadrao
        self.fgp.pack(side=LEFT)

        self.bgpLabel = Label(self.bgpContainer, text="B4", font=self.fontePadrao)
        self.bgpLabel.pack(side=LEFT)
        self.bgp = Entry(self.bgpContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.B5)))
        self.bgp["width"] = 30
        self.bgp["font"] = self.fontePadrao
        self.bgp.pack(side=LEFT)

        self.fgzLabel = Label(self.fgzContainer, text="B4", font=self.fontePadrao)
        self.fgzLabel.pack(side=LEFT)
        self.fgz = Entry(self.fgzContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.B5)))
        self.fgz["width"] = 30
        self.fgz["font"] = self.fontePadrao
        self.fgz.pack(side=LEFT)

        self.bgzLabel = Label(self.bgzContainer, text="B4", font=self.fontePadrao)
        self.bgzLabel.pack(side=LEFT)
        self.bgz = Entry(self.bgzContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.B5)))
        self.bgz["width"] = 30
        self.bgz["font"] = self.fontePadrao
        self.bgz.pack(side=LEFT)

        self.fnpLabel = Label(self.fnpContainer, text="FNP", font=self.fontePadrao)
        self.fnpLabel.pack(side=LEFT)
        self.fnp = Entry(self.fnpContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.FNP)))
        self.fnp["width"] = 30
        self.fnp["font"] = self.fontePadrao
        self.fnp.pack(side=LEFT)

        self.bnpLabel = Label(self.bnpContainer, text="BNP", font=self.fontePadrao)
        self.bnpLabel.pack(side=LEFT)
        self.bnp = Entry(self.bnpContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.FNP)))
        self.bnp["width"] = 30
        self.bnp["font"] = self.fontePadrao
        self.bnp.pack(side=LEFT)

        self.bnzLabel = Label(self.bnzContainer, text="BNZ", font=self.fontePadrao)
        self.bnzLabel.pack(side=LEFT)
        self.bnz = Entry(self.bnzContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.BNZ)))
        self.bnz["width"] = 30
        self.bnz["font"] = self.fontePadrao
        self.bnz.pack(side=LEFT)

        self.fgsLabel = Label(self.fgsContainer, text="FGS", font=self.fontePadrao)
        self.fgsLabel.pack(side=LEFT)
        self.fgs = Entry(self.fgsContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.FGS)))
        self.fgs["width"] = 30
        self.fgs["font"] = self.fontePadrao
        self.fgs.pack(side=LEFT)

        self.bgsLabel = Label(self.bgsContainer, text="BGS", font=self.fontePadrao)
        self.bgsLabel.pack(side=LEFT)
        self.bgs = Entry(self.bgsContainer, textvariable=StringVar(root, value=str(ctes.ParametrosConstantes.BGS)))
        self.bgs["width"] = 30
        self.bgs["font"] = self.fontePadrao
        self.bgs.pack(side=LEFT)

        self.f0Label = Label(self.f0Container, text="F0", font=self.fontePadrao)
        self.f0Label.pack(side=LEFT)
        self.f0 = Entry(self.f0Container, textvariable= StringVar(root, value=str(ctes.ParametrosConstantes.F0)))
        self.f0["width"] = 30
        self.f0["font"] = self.fontePadrao
        self.f0.pack(side=LEFT)

        self.b2Label = Label(self.b2Container, text="B2", font=self.fontePadrao)
        self.b2Label.pack(side=LEFT)
        self.b2 = Entry(self.b2Container, textvariable=StringVar(root, value=str(ctes.VogalA.B2)))
        self.b2["width"] = 30
        self.b2["font"] = self.fontePadrao
        self.b2.pack(side=LEFT)

        self.f3Label = Label(self.f3Container, text="F3", font=self.fontePadrao)
        self.f3Label.pack(side=LEFT)
        self.f3 = Entry(self.f3Container, textvariable=StringVar(root, value=str(ctes.VogalA.F3)))
        self.f3["width"] = 30
        self.f3["font"] = self.fontePadrao
        self.f3.pack(side=LEFT)

        self.b3Label = Label(self.b3Container, text="B3", font=self.fontePadrao)
        self.b3Label.pack(side=LEFT)
        self.b3 = Entry(self.b3Container, textvariable=StringVar(root, value=str(ctes.VogalA.B3)))
        self.b3["width"] = 30
        self.b3["font"] = self.fontePadrao
        self.b3.pack(side=LEFT)

        self.autenticar = Button(self.sintetizarContainer)
        self.autenticar["text"] = "Sintetizar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.sintetizar
        self.autenticar.pack()
        self.mensagem = Label(self.sintetizarContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Listener para sintetizar
    def sintetizar(self):
        nomeArquivo = self.nomeArquivo.get()
        try:
            if nomeArquivo != "":
                self.mensagem["text"] = "Sintetizando"
                ctes.Gerais.TEMPO_SIMULACAO = float(self.tempoSimulacao.get())
                ctes.Gerais.VARIACAO_F0 = float(self.variacaoF0.get())
                ctes.Gerais.VARIACAO_K = float(self.variacaoK.get())
                ctes.Gerais.GANHO_RUIDO = float(self.ganhoRuido.get())
                ctes.ParametrosConstantes.F0 = float(self.f0.get())
                ctes.ParametrosConstantes.B4 = float(self.b4.get())
                ctes.ParametrosConstantes.B5 = float(self.b5.get())
                ctes.ParametrosConstantes.FGP = float(self.fgp.get())
                ctes.ParametrosConstantes.BGP = float(self.bgp.get())
                ctes.ParametrosConstantes.FGZ = float(self.fgz.get())
                ctes.ParametrosConstantes.BGZ = float(self.bgz.get())
                ctes.ParametrosConstantes.FNP = float(self.fnp.get())
                ctes.ParametrosConstantes.BNP = float(self.bnp.get())
                ctes.ParametrosConstantes.BNZ = float(self.bnz.get())
                ctes.ParametrosConstantes.FGS = float(self.fgs.get())
                ctes.ParametrosConstantes.BGS = float(self.bgs.get())
                ctes.VogalA.F1 = float(self.f1.get())
                ctes.VogalA.B1 = float(self.b1.get())
                ctes.VogalA.F2 = float(self.f2.get())
                ctes.VogalA.B2 = float(self.b2.get())
                ctes.VogalA.F3 = float(self.f3.get())
                ctes.VogalA.B3 = float(self.b3.get())
                sintetizador.sintetizar(nomeArquivo, 'a')
                self.mensagem["text"] = "Áudio sintetizado!"
            else:
                self.mensagem["text"] = "Nome de arquivo vazio"
        except:
            self.mensagem["text"] = "Erro: " + sys.exc_info()[0]

if __name__ == "__main__":
    root = Tk()
    root.title('Sintetizador de voz')
    Gui(root)
    root.mainloop()