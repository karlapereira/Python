from modulos import *
from validentry import Validadores
from frameGrad import GradientFrame
from reports import Relatorios
from funcionalidades import Funcs
from placeholder import EntPlaceHolder
import pycep_correios


root = tix.Tk()
      
class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()
    
    def cepCorreios(self):
        try:
            self.cidade_entry.delete(0, END)
            self.endereco_entry.delete(0, END)
            self.cidade_entry.delete(0, END)
            
            zipcode = self.cep_entry.get()
            dadosCep = pycep_correios.get_address_from_cep(zipcode)
            print(dadosCep)
            
            self.cidade_entry.insert(END, dadosCep['cidade'])
            self.endereco_entry.insert(END, dadosCep['logradouro'])
            self.bairro_entry.insert(END, dadosCep['bairro'])
        except:
            messagebox.showinfo("Erro CEP", "Cep não encontrado")
            
    
    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='#0B2F3A')
        self.root.geometry("750x800")
        self.root.resizable(False, False)
        self.root.maxsize(width=900, height=700)
        #frames - caixas conjuntos que separa os itens da tela       
    def frames_da_tela(self):
        #place - trabalha como x e y, trabalha com % da tela | pack |grid - trabalha como planilha, linha e coluna
        self.frame_1 = Frame(self.root, bd=4, bg='#A9E2F3', 
                             highlightbackground='#81BEF7', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)
        
        self.frame_2 = Frame(self.root, bd=4, bg='#A9E2F3', 
                             highlightbackground='#81BEF7', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth= 0.96, relheight= 0.46)        
    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = GradientFrame(self.abas)
        self.aba2 = Frame(self.abas)
        
        self.aba1.configure(background="#A9E2F3")
        self.aba2.configure(background="lightgray")
        
        self.abas.add(self.aba1, text = "Aba 1")
        self.abas.add(self.aba2, text = "Aba 2")
        
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)
        
        self.canvas_bt = Canvas(self.aba1, bd=0, bg='black', highlightbackground='gray',
                               highlightthickness=5)
        self.canvas_bt.place(relx=0.19, rely=0.08, relwidth=0.22, relheight=0.19)
        
        ### Botão limpar
        self.btn_limpar = Button(self.aba1, text='Limpar', bd=2, bg = '#0A2A29', fg='white', 
                                activebackground='#108ecb', activeforeground='white',
                                font = ('Arial', 8, 'bold'), command=self.limpa_tela)
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ### Botão buscar
        self.btn_buscar = Button(self.aba1, text='Buscar', bd=2, bg = '#0A2A29', fg='white', 
                                font = ('Arial', 8, 'bold'), command=self.tela2)
        self.btn_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        texto_balao_buscar = 'Digite no campo nome o cliente que deseja buscar'
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.btn_buscar, balloonmsg=texto_balao_buscar)


        
        ### Botão novo
        ## imgNovo
        self.btnovo = PhotoImage(data=base64.b64decode(self.btnovo_base64), width=60, height=30)
        #elf.imgNovo = self.imgNovo.subsample(1,1)
        #self.style = ttk.Style()
        #self.style.configure("BW.TButton", relwidth=1, relheight=1, foreground='gray',
        #                 borderwidth=0, bordercolor='gray', background='#dfe3ee',
        #                        image=self.imgNovo)
        
        #self.btn_novo = ttk.Button(self.frame_1, style='BW.TButton', command=self.add_cliente)
        #self.btn_novo.config(image=self.imgNovo)
        
        self.btn_novo = Button(self.aba1, image= self.btnovo, bd = 0, command=self.add_cliente)
        
        #self.btn_novo = Button(self.frame_1, text='Novo', bd=2, bg = '#0A2A29', fg='white', 
        #                            font = ('Arial', 8, 'bold'), command=self.add_cliente)
        self.btn_novo.place(relx=0.6, rely=0.1)
        
        ### Botão alterar
        self.btn_alterar = Button(self.aba1, text='Alterar', bd=2, bg = '#0A2A29', fg='white', 
                                font = ('Arial', 8, 'bold'), command=self.altera_cliente)
        self.btn_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ### Botão apagar
        self.btn_apagar = Button(self.aba1, text='Apagar', bd=2, bg = '#0A2A29', fg='white', 
                                font = ('Arial', 8, 'bold'), command=self.deleta_cliente)
        self.btn_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ## Criação da label e entrada do codigo
        self.lbl_codigo = Label(self.aba1, text = "Código", bg='#A9E2F3', fg = '#0B2F3A',
                               font = ('bold'))
        self.lbl_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.aba1, validate = "key", validatecommand=self.vcm2)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        
        ## Criação da label e entrada do nome
        self.lbl_nome = Label(self.aba1, text = "Nome", bg='#A9E2F3', fg = '#0B2F3A',
                               font = ('bold'))
        self.lbl_nome.place(relx=0.05, rely=0.30)
        
        self.nome_entry = EntPlaceHolder(self.aba1, 'Digite o nome do cliente')
        self.nome_entry.place(relx=0.05, rely=0.40, relwidth=0.4)
        
        ## Criação da label e entrada CEP
        self.btn_cep = Button(self.aba1, text = "CEP", bg='#ccccff', fg = '#0B2F3A',
                               font = ('bold'), command=self.cepCorreios)
        self.btn_cep.place(relx=0.50, rely=0.40, relheight=0.115)
        
        self.cep_entry = Entry(self.aba1)
        self.cep_entry.place(relx=0.60, rely=0.40, relwidth=0.3)        
        
        ## Criação da label e entrada do telefone
        self.lbl_telefone = Label(self.aba1, text = "Telefone", bg='#A9E2F3', fg = '#0B2F3A',
                               font = ('bold'))
        self.lbl_telefone.place(relx=0.05, rely=0.55)
        
        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.65, relwidth=0.4)
        
        ## Criação da label e entrada da cidade
        self.lbl_cidade = Label(self.aba1, text = "Cidade", bg='#ccccff', fg = '#0B2F3A',
                               font = ('bold'))
        self.lbl_cidade.place(relx=0.5, rely=0.55)
        
        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.65, relwidth=0.4)
        
        ## Criação da label e entrada do Endereço
        self.lbl_endereco = Label(self.aba1, text = "Endereço", bg='#A9E2F3', fg = '#0B2F3A',
                               font = ('bold'))
        self.lbl_endereco.place(relx=0.05, rely=0.75)
        
        self.endereco_entry = Entry(self.aba1)
        self.endereco_entry.place(relx=0.05, rely=0.85, relwidth=0.4)
        
        ## Criação da label e entrada da Bairro
        self.lbl_bairro = Label(self.aba1, text = "Bairro", bg='#ccccff', fg = '#0B2F3A',
                               font = ('bold'))
        self.lbl_bairro.place(relx=0.5, rely=0.75)
        
        self.bairro_entry = Entry(self.aba1)
        self.bairro_entry.place(relx=0.5, rely=0.85, relwidth=0.4)
        
        ### drop down button
        self.Tipvar = StringVar()
        self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
        self.Tipvar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)        
        
        ### Calendario
        self.bt_calendario = Button(self.aba2, text = "Data", command=self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.02)
        self.entry_data = Entry(self.aba2, width=10)
        self.entry_data.place(relx=0.5, rely=0.2)
        
        
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height = 3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.reziable=(False, False)
        self.listaCli.heading('#0', text = "")
        self.listaCli.heading('#1', text = "Codigo")
        self.listaCli.heading('#2', text = "Nome")
        self.listaCli.heading('#3', text = "Telefone")
        self.listaCli.heading('#4', text = "Cidade")
        
        self.listaCli.column("#0", width=1, anchor="n")
        self.listaCli.column("#1", width=50, anchor="n")
        self.listaCli.column("#2", width=200, anchor="n")
        self.listaCli.column("#3", width=125, anchor="n")
        self.listaCli.column("#4", width=125, anchor="n")

        
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        def Quit(): self.root.destroy()
        menubar.add_cascade(label= "Opções", menu = filemenu)
        menubar.add_cascade(label= "Relatórios", menu = filemenu2)
        
        filemenu.add_command(label="Sair", command = Quit)
        filemenu.add_command(label="Limpa Cliente", command = self.limpa_tela)
        
        filemenu2.add_command(label="Ficha do cliente", command = self.geraRelatCliente)

    def tela2(self):
        self.root2 = Toplevel()
        self.root2.title("Janela 2")
        self.root2.configure(background='lightblue')
        self.root2.geometry("400x200")
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.root2.grab_set()
    def validaEntradas(self):
        self.vcm2 = (self.root.register(self.validate_entry2), "%P")    
        
Application()
