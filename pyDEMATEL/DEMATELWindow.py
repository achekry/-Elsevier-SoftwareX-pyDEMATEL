import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from DEMATELSolver import DEMATELSolver
from FuzzyDEMATELSolver import FuzzyDEMATELSolver
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DEMATELWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("pyDEMATEL")
        self.window.geometry("1200x700")
        self.window.state('zoomed')  # Maximize the window (on Windows)
        self.window.attributes("-fullscreen", False)  # Ensure fullscreen is not set
        self.window.grid_columnconfigure(0, weight=1)
        self.MatrixX=[]         
        #self.noInfuence="No influence 0"     
        
        titre = tk.Label(self.window, text="pyDEMATEL : DEMATEL & Fuzzy DEMATEL Solver", font=('Helvetica', 20, 'bold'), fg='#2E4053')
        titre.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        # frame input numbers of experts and factors & fill factors & experts
        self.createInputFrames()

        
    
        
    def usingDematel(self):
        self.MatrixX=[]         
        self.noInfuence="No influence 0"
        self.dim=0
        self.solver = DEMATELSolver()
        self.influeceIndiceFactor = {
            "No influence 0":0, "Very low influence 1":1, "Low influence 2":2, 
            "High influence 3":3, "Very high influence 4":4
        }    
    def usingFuzzyDematel(self):
        self.MatrixX=[]         
        self.solver = FuzzyDEMATELSolver()
        self.noInfuence="No influence (0,0,0.25)"   
        self.dim=3        
        self.influeceIndiceFactor = {
         "No influence (0,0,0.25)":[0,0,0.25], "Very low influence (0, 0.25, 0.5)":[0, 0.25, 0.5], "Low influence (0.25, 0.5, 0.75)":[0.25, 0.5, 0.75], 
            "High influence (0.5, 0.75, 1)":[0.5, 0.75, 1], "Very high influence (0.75, 1, 1)":[0.75, 1, 1]
        }
          
    def createInputFrames(self):
        self.inputFrames = tk.Frame(self.window)
        self.inputFrames.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="nsew")
        self.inputFrames.grid_columnconfigure((0, 1), weight=1)    
        self.createInputNumbersFrame()
        self.createInputNamesFrame()
        self.createButtonsDMATELFrame()
        
     # frame input numbers of experts and factors
    def createInputNumbersFrame(self):
        frmNumbers = tk.LabelFrame(self.inputFrames,text="Input Numbers", bg="#ECF0F1", padx=10, pady=10, relief='groove', bd=2)
        frmNumbers.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="nsew")
        #défilement
        
        
        
        label1 = tk.Label(frmNumbers, text="Number of experts:",font=('sans serif', 10, 'bold'))
        label1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtExperts = tk.Entry(frmNumbers,font=('sans serif', 10, 'bold'), bg='#D2D4CF')
        self.txtExperts.grid(row=1, column=1, padx=10, pady=5)    
   
       
        label2 = tk.Label(frmNumbers, text="Number of factors:",font=('sans serif', 10, 'bold'))
        label2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtFactors = tk.Entry(frmNumbers,font=('sans serif', 10, 'bold'), bg='#D2D4CF')
        self.txtFactors.grid(row=2, column=1, padx=10, pady=5)
        
       
        btnAdd = tk.Button(frmNumbers, text="           Add           ", font=("sans serif", 10, "bold"), command=self.on_btnAdd_click, bg="#CDD3C4", fg="black", relief="flat", padx=10, pady=5)
        btnAdd.grid(row=3, column=1, columnspan=2, padx=10, pady=(0, 5))
    
    # frame input experts and factors    
    def createInputNamesFrame(self):
        self.frmNames = tk.LabelFrame(self.inputFrames,text="Input Names", bg="#ECF0F1", padx=10, pady=10, relief='groove', bd=2)
        self.frmNames.grid(row=0, column=1,padx=10, pady=(0, 5), sticky="nsew")
        
        scrollbar = ttk.Scrollbar( self.frmNames, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        canvas = tk.Canvas( self.frmNames , yscrollcommand=scrollbar.set, height=100)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=canvas.yview)
        self.frmInnerNames = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.frmInnerNames, anchor="nw")
        self.frmInnerNames.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
 
    # frame boutons DMATEL And Fuzzy DEMATEL resolve  
    def createButtonsDMATELFrame(self):
        self.frmButtons = tk.Frame(self.inputFrames,bg="#ECF0F1", padx=10, pady=10, relief='groove')
        self.frmButtons.grid(row=0, column=2,padx=10, pady=(0, 5), sticky="nsew")
        
                 

    def createInputValuesAndResaulsFrames(self):
        self.InputValuesAndResaulsFrames = tk.Frame(self.window)
        self.InputValuesAndResaulsFrames.grid(row=3, column=0, padx=10, pady=(0, 5), sticky="nsew")
        self.InputValuesAndResaulsFrames.grid_columnconfigure((0, 1), weight=1)    
        self.createInputValuesFrame()
        self.createResultsFrame()               
        
    def createInputValuesFrame(self):    
        self.frmValues = tk.LabelFrame(self.InputValuesAndResaulsFrames,text="Input Values",height=400,width=400)
        self.frmValues.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frmValues.pack_propagate(False)
        self.frmValues.grid_columnconfigure((0, 1), weight=1)           
        vSscrollbar = ttk.Scrollbar( self.frmValues, orient="vertical")
        vSscrollbar.pack(side="right", fill="y")
        hScrollbar = ttk.Scrollbar( self.frmValues, orient="horizontal")
        hScrollbar.pack(side="bottom", fill="x")     
        canvas = tk.Canvas( self.frmValues , yscrollcommand=vSscrollbar.set, xscrollcommand=hScrollbar.set, height=100)
        canvas.pack(side="left", fill="both", expand=True)
        vSscrollbar.config(command=canvas.yview)
        hScrollbar.config(command=canvas.xview)
        self.frmInnerValues = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.frmInnerValues, anchor="nw")
        self.frmInnerValues.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        
        
    def createResultsFrame(self):
        self.frmResults = tk.LabelFrame(self.InputValuesAndResaulsFrames,text="Results",height=400,width=400)
        self.frmResults.grid(row=0, column=1, padx=10, pady=(0, 5), sticky="nsew")
        self.frmResults.grid_columnconfigure((0, 1), weight=1)  
        
        vSscrollbar = ttk.Scrollbar( self.frmResults, orient="vertical")
        vSscrollbar.pack(side="right", fill="y")
        hScrollbar = ttk.Scrollbar( self.frmResults, orient="horizontal")
        hScrollbar.pack(side="bottom", fill="x")  
        canvas = tk.Canvas( self.frmResults ,  yscrollcommand=vSscrollbar.set, xscrollcommand=hScrollbar.set, height=100)
        canvas.pack(side="left", fill="both", expand=True)
        vSscrollbar.config(command=canvas.yview)
        hScrollbar.config(command=canvas.xview)
        self.frmInnerResults = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.frmInnerResults, anchor="nw")
        self.frmInnerResults.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
    
       
 
    def generate_table(self, parent_frame, nbFactors,nCol):
        table_frames = []
        for i in range(nbFactors + 1):  # +1 for titles
            row_frames = []
            for j in range(nCol + 1):  # +1 for titles
                outer_frame = tk.Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
                outer_frame.grid(row=i, column=j, sticky="nsew")
                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack(fill="both", expand=True, padx=1, pady=1)
                row_frames.append(inner_frame)
            table_frames.append(row_frames)
        return table_frames
    

    def createExperts(self):
          self.expertNames=[]
          for i in range(self.num_experts):
              lblNameExpert = tk.Label(self.frmInnerNames, text="Expert "+ str(i+1), font=('sans serif', 10, 'bold'))
              lblNameExpert.grid(row=1+i, column=0, padx=10, pady=5, sticky="w")
              self.expertNames.append(tk.Entry(self.frmInnerNames ,font=('sans serif', 10, 'bold'), bg='#D2D4CF'))
              self.expertNames[i].insert(0,"Expert"+str(i))
              self.expertNames[i].grid(row=1+i, column=1, padx=10, pady=5)
              
            
    def createFactors(self):
          self.FactorsNames=[]
          for i in range(self.num_factors):
              lblNameFactor = tk.Label(self.frmInnerNames, text="Factor "+ str(i+1),font=('sans serif', 10, 'bold'))
              lblNameFactor.grid(row=1+i, column=2, padx=10, pady=5, sticky="w")
              self.FactorsNames.append(tk.Entry(self.frmInnerNames,font=('sans serif', 10, 'bold'), bg='#D2D4CF'))
              
              self.FactorsNames[i].insert(0,"Factor"+str(i))
              self.FactorsNames[i].grid(row=1+i, column=3, padx=10, pady=5)     
                    
        # tabs        
    def createTabs(self):

        btnResolve = tk.Button(self.window, text="              Resolve              ", command=self.on_btnResolve_click, font=("sans serif", 10, "bold"), bg="#CDD3C4", fg="black", relief="flat", padx=10, pady=5)
        btnResolve.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 5))
        

        self.notebook = ttk.Notebook(self.frmInnerValues)
        self.notebook.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        

        titlesTabs = [entry.get() for entry in self.expertNames]
        for i, title in enumerate(titlesTabs):
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=title)
            table_frames = self.generate_table(frame, self.num_factors, self.num_factors)
            self.matrixExpertTab(table_frames, self.num_factors)
        
    def fillFactors(self):
        titles = [entry.get() for entry in self.FactorsNames]
        for j, title in enumerate(titles):
            self.solver.factors.append(title)
        self.solver.numberOfFactors = len(self.solver.factors)
        
    def fillExperts(self):
        titles = [entry.get() for entry in self.expertNames]
        for j, title in enumerate(titles):
            self.solver.experts.append(title)
        self.solver.numberOfExperts = len(self.solver.experts)
    
    def fillMatrix(self):
        if self.dim==3:
            self.solver.matrix= np.zeros((self.num_experts, self.num_factors, self.num_factors,self.dim))  
        else:
            self.solver.matrix= np.zeros((self.num_experts, self.num_factors, self.num_factors))  
        k=0
        for M in self.MatrixX:
            i=0
            for row in M:
                j=0
                for v in row:
                    self.solver.matrix[k][i][j]=self.influeceIndiceFactor[v.get()]
                    j+=1
                i+=1
            k+=1
        
    def fillMatrixZ(self, tab_name):                  #fillDirect-influence matrix Z
        tab_frame = self.tabsIDs.get(tab_name)
        
        # Générer le tableau
        if tab_frame:
            table_frames = self.generate_table(tab_frame, self.num_factors, self.num_factors)
            
            # Titres de la première ligne
            titles = [entry.get() for entry in self.FactorsNames]
            for j, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[0][j + 1], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
        
            # Titres de la première colonne
            for i, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[i + 1][0], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
          
        for i in range(1, self.num_factors + 1):
            for j in range(1, self.num_factors + 1):
                value = self.solver.Z[i-1, j-1] 
                if self.dim==3:
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}")+',' +str(f"{value[2]:.2f}") +')'
                else:
                    txt=f"{value:.2f}"
                lblValue = ttk.Label(table_frames[i][j], text=txt) 
                lblValue.grid(row=0, column=0, padx=5, pady=5)


    def fillMatrixX(self, tab_name):                  

        tab_frame = self.tabsIDs.get(tab_name)
        
        # Générer le tableau
        if tab_frame:
            table_frames = self.generate_table(tab_frame, self.num_factors, self.num_factors)
            
            # Titres de la première ligne
            titles = [entry.get() for entry in self.FactorsNames]
            for j, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[0][j + 1], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
        
            # Titres de la première colonne
            for i, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[i + 1][0], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
          
        for i in range(1, self.num_factors + 1):
            for j in range(1, self.num_factors + 1):
                value = self.solver.X[i-1, j-1]  
                if self.dim==3:
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}")+',' +str(f"{value[2]:.2f}") +')'
                else:
                    txt=f"{value:.2f}"
                lblValue = ttk.Label(table_frames[i][j], text=txt)  
                lblValue.grid(row=0, column=0, padx=5, pady=5)     

    def fillMatrixT(self, tab_name):                  #fill Direct-influence matrix X
        tab_frame = self.tabsIDs.get(tab_name)
        
        # Générer le tableau
        if tab_frame:
            table_frames = self.generate_table(tab_frame, self.num_factors, self.num_factors)
            
            titles = [entry.get() for entry in self.FactorsNames]
            for j, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[0][j + 1], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
        
            for i, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[i + 1][0], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
          

        for i in range(1, self.num_factors + 1):
            for j in range(1, self.num_factors + 1):
                value = self.solver.T[i-1][j-1]  
                if self.dim==3:
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}") +','+str(f"{value[2]:.2f}") +')'
                else:
                    txt=f"{value:.2f}"
                lblValue = ttk.Label(table_frames[i][j], text=txt)  
                lblValue.grid(row=0, column=0, padx=5, pady=5)

    
    def fillMatrixIRM(self, tab_name):                  
        indicators = ["R","C","R+C","R-C"]
        tab_frame = self.tabsIDs.get(tab_name)

        if tab_frame:
            table_frames = self.generate_table(tab_frame, self.num_factors,len(indicators))

            titles = [entry.get() for entry in self.FactorsNames]
            for j, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[j + 1][0], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)

            for i in range(len(indicators)):
                lblTitleFactorInTableTab = ttk.Label(table_frames[0][i + 1], text=indicators[i])
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
            for i in range(1, self.num_factors + 1):
                    lblValueR = ttk.Label(table_frames[i][1], text=f"{self.solver.R[i-1]:.2f}")  
                    lblValueR.grid(row=0, column=0, padx=5, pady=5)
                    lblValueC = ttk.Label(table_frames[i][2], text=f"{self.solver.C[i-1]:.2f}")  
                    lblValueC.grid(row=0, column=1, padx=5, pady=5)
                    lblValueRelation = ttk.Label(table_frames[i][3], text=f"{self.solver.prominence[i-1]:.2f}")  
                    lblValueRelation.grid(row=0, column=3, padx=5, pady=5)
                    lblValueProminence = ttk.Label(table_frames[i][4], text=f"{self.solver.relation[i-1]:.2f}")  
                    lblValueProminence.grid(row=0, column=2, padx=5, pady=5)
       
    def fillMatrixFuzzyIRM(self, tab_name):                  #fill Direct-influence matrix IRM
        indicators = ["R","C","R+C","R-C"]
        #self.solver.step4()
        tab_frame = self.tabsIDs.get(tab_name)
        # Générer le tableau
        if tab_frame:
            table_frames = self.generate_table(tab_frame, self.num_factors,len(indicators))
            titles = [entry.get() for entry in self.FactorsNames]
            for j, title in enumerate(titles):
                lblTitleFactorInTableTab = ttk.Label(table_frames[j + 1][0], text=title)
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
            for i in range(len(indicators)):
                lblTitleFactorInTableTab = ttk.Label(table_frames[0][i + 1], text=indicators[i])
                lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
            for i in range(1, self.num_factors + 1):
                    value = self.solver.FR[i-1] 
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}") +','+str(f"{value[2]:.2f}") +')'
                    lblValueR = ttk.Label(table_frames[i][1], text=txt)  
                    lblValueR.grid(row=0, column=0, padx=5, pady=5)
                    
                    value = self.solver.FC[i-1] 
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}") +','+str(f"{value[2]:.2f}") +')'
                    lblValueC = ttk.Label(table_frames[i][2], text=txt)  
                    lblValueC.grid(row=0, column=1, padx=5, pady=5)
                    
                    value = self.solver.FRelation[i-1] 
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}") +str(f"{value[2]:.2f}") +')'
                    lblValueProminence = ttk.Label(table_frames[i][3], text=txt)  
                    lblValueProminence.grid(row=0, column=2, padx=5, pady=5)
                    
                    value = self.solver.FProminence[i-1] 
                    txt='('+str(f"{value[0]:.2f}") +','+str(f"{value[1]:.2f}") +','+str(f"{value[2]:.2f}") +')'
                    lblValueRelation = ttk.Label(table_frames[i][4], text=txt)  
                    lblValueRelation.grid(row=0, column=3, padx=5, pady=5)
        
    def drawCurve(self, tab_name):
        tab_frame = self.tabsIDs.get(tab_name)
        if tab_frame:
            fig, ax = plt.subplots(figsize=(2, 2))  
            ax.scatter(self.solver.prominence,  self.solver.relation, marker='o', s=50)  
            for name,p,r in zip(self.solver.factors, self.solver.prominence, self.solver.relation):
                ax.text(p, r, name, ha='center', va='bottom')
            ax.set_xlabel('R+C')
            ax.set_ylabel('R-C')

            ax.axhline(0, color='black', linestyle='--')

            plt.tight_layout()  

            canvas = FigureCanvasTkAgg(fig, master=tab_frame)
            canvas.draw()
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill=tk.BOTH, expand=True)
            canvas_widget.config(width=350, height=450)
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


    
    def matrixExpertTab(self, table_frames, nbFactors):
        # Titres de la première ligne
        titles = [entry.get() for entry in self.FactorsNames]
        for j, title in enumerate(titles):
            lblTitleFactorInTableTab = ttk.Label(table_frames[0][j + 1], text=title)
            lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
    

        titles = [entry.get() for entry in self.FactorsNames]
        for i, title in enumerate(titles):
            lblTitleFactorInTableTab = ttk.Label(table_frames[i + 1][0], text=title)
            lblTitleFactorInTableTab.grid(row=0, column=0, padx=5, pady=5)
      
        
        M=[]
        for i in range(1, nbFactors + 1):
            row=[]
            for j in range(1, nbFactors + 1):
                if i == j:
                    combo_values = [self.noInfuence]
                    combo = ttk.Combobox(table_frames[i][j], values=combo_values, state="readonly")
                    combo.current(0) 
                    combo.grid(row=0, column=0, padx=5, pady=5)
                    row.append(combo)
                else:
                    row.append(ttk.Combobox(table_frames[i][j],  values=list(self.influeceIndiceFactor.keys()), state="readonly"))
                    row[j-1].grid(row=0, column=0, padx=5, pady=5)

            M.append(row)
        self.MatrixX.append(M)
    
   
    def createResultTabs(self):

        self.notebookResult = ttk.Notebook(self.frmInnerResults)     
        values_ResultTabsTitles= [
            "Causal Diagram", "Influential Relation Map IRM", "Direct-influence matrix Z", 
            "Normalized direct-influence matrix X", "Total-influence matrix T" ]
        nb=5
        if self.dim==3:
            nb=6
            values_ResultTabsTitles+=["Fuzzy IRM"]
        self.notebookResult.grid(row=1, column=0, columnspan=nb, padx=10, pady=10, sticky="nsew")
        
        #Titres des onglets
        self.tabsIDs = {}
        titlesTabs = [entry.get() for entry in self.expertNames]
        for title in values_ResultTabsTitles:
            self.frame = ttk.Frame(self.notebookResult)
            self.notebookResult.add(self.frame, text=title)
            self.tabsIDs[title] = self.frame
            
        for tab_name in values_ResultTabsTitles:
            self.tab_frame = self.tabsIDs.get(tab_name)
    

        self.fillMatrixIRM("Influential Relation Map IRM")
        self.fillMatrixZ("Direct-influence matrix Z")
        self.fillMatrixX("Normalized direct-influence matrix X")
        self.fillMatrixT("Total-influence matrix T")
        self.fillMatrixFuzzyIRM("Fuzzy IRM")
        self.drawCurve("Causal Diagram")
        
        btnExport = tk.Button(self.window, text="   Export Results   ", command=self.on_btnExport_click, font=("sans serif", 10, "bold"), bg="#CDD3C4", fg="black", relief="flat", padx=10, pady=5)
        btnExport.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 5))
   
    def on_btnExport_click(self):
        folder_path = filedialog.askdirectory()
        self.solver.savexl(folder_path)
        msg = tk.Label(self.window, text="Your file has been saved at: "+folder_path+"/DEMATELAnalysis.xlsx", font=('Helvetica', 12, 'bold'), fg='#2E4053')
        msg.grid(row=6, column=0, columnspan=4, padx=10, pady=(0, 5))

    def on_btnAdd_click(self):
        self.num_experts = int(self.txtExperts.get())
        self.num_factors = int(self.txtFactors.get())
        self.createExperts()
        self.createFactors()
            
        btnGenerate = tk.Button(self.frmButtons, text="      DEMATEL Solver    ", command=self.on_btnGenerate_click, font=("sans serif", 10, "bold"), bg="#CDD3C4", fg="black", relief="flat", padx=10, pady=5)
        btnGenerate.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 5)) 
        
        btnGenerate = tk.Button(self.frmButtons, text="Fuzzy DEMATEL Solver", command=self.on_btnGenerateFuzzy_click, font=("sans serif", 10, "bold"),  bg="#CDD3C4", fg="black", relief="flat", padx=10, pady=5)
        btnGenerate.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 5)) 


    def on_btnGenerate_click(self):
        self.usingDematel()
        self.createInputValuesAndResaulsFrames()     
        self.createTabs() 

    def on_btnGenerateFuzzy_click(self):
        self.usingFuzzyDematel()
        self.createInputValuesAndResaulsFrames()
        self.createTabs()  

         
        
    # Fonction appelée lors du clic sur le bouton "Resolve"
    def on_btnResolve_click(self):
        self.fillExperts()
        self.fillFactors()
        self.fillMatrix()
        self.solver.step1()
        self.solver.step2()
        self.solver.step3()
        self.solver.step4()
        
        
        self.createResultTabs()     

            
# Lancement de la boucle principale
app = DEMATELWindow()
app.window.mainloop()