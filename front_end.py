import tkinter as tk
from tkinter import ttk, messagebox
from ciee import clica_site
from Tabela import tela_resultados_vagas

def tela_dados_vaga():
    # Atualiza a lista de áreas profissionais com base no nível de ensino
    def atualizar_areas_profissionais(event=None):
        nivel = combo_nivel_ensino.get()
        if nivel == "Ensino Fundamental":
            combo_area_profissional['values'] = ["Proeja-Ens.Fundamental"]
        elif nivel == "Ensino Médio":
            combo_area_profissional['values'] = ["Ensino Médio"]
        elif nivel == "Técnico":
            combo_area_profissional['values'] = [
                "Todas", "Administrativa - Téc.", "Agropecuária - Téc.", "Alimentos - Téc.", "Artes - Téc.",
                "Audiovisual - Téc.", "Comércio - Téc.", "Comércio Exterior - Téc.", "Comunicação - Téc.",
                "Construção Civil - Téc.", "Design - Téc.", "Educação - Téc.", "Educação Especial - Téc.",
                "Elétrica-Eletrônica - Téc.", "Embelezamento/Estética - Téc.", "Farmacia - Téc.",
                "Geomática - Téc.", "Indústria - Téc.", "Informática - Téc.", "Jurídica - Téc.",
                "Lazer/Desenv. Social - Téc.", "Marketing - Téc.", "Mecânica", "Mecânica - Téc.",
                "Meio Ambiente - Téc.", "Mineração - Téc.", "Moda - Téc.", "Projetos - Téc.", "Química - Téc.",
                "Recursos Humanos", "Recursos Pesqueiros - Téc.", "Saúde - Téc.", "Segurança - Téc.",
                "Técnico Mecânica", "Telecomunicações - Téc.", "Transportes - Téc.", "Turismo - Téc.",
                "Veterinária - Téc."
            ]
        elif nivel == "Superior":
            combo_area_profissional['values'] = [
                "Todas", "Administrativa", "Agropecuária", "Alimentos", "Arquitetura e Urbanismo", "Arquivologia",
                "Artes", "Atendimento ao Cliente", "Biologia", "Biblioteca", "Comunicação", "Comércio Exterior",
                "Construção Civil", "Contabilidade", "Design de Interiores", "Design", "Economia", "Educação",
                "Educação | Química", "Elétrica-Eletrônica", "Embelezamento/Estética", "Engenharia Ambiental",
                "Engenharia Civil", "Engenharia de Alimentos", "Engenharia de Produção",
                "Engenharia de Tecnologia da Informação", "Engenharia de Minas", "Esportes", "Financeiro",
                "Farmácia", "Gastronomia", "Geociências", "Geomática", "Indústria", "Informática", "Jurídica",
                "Letras", "Licenciatura", "Marketing", "Meio Ambiente", "Mineração", "Moda", "Museologia",
                "Nutrição", "Odontologia", "Produção", "Pesquisa", "Produção Mecânica", "Projetos - Superior",
                "Psicologia", "Química", "Relações Internacionais", "Recursos Humanos", "Recursos Operacionais",
                "Recursos Pesqueiros", "Religião", "Serviço Social", "Saúde", "Secretariado", "Segurança", "Social",
                "Telecomunicações", "Transportes", "Turismo/Lazer", "Veterinária"
            ]
        combo_area_profissional.set("")  # Limpa seleção anterior

    # Atualiza os níveis de ensino conforme o tipo de vaga escolhido
    def atualizar_niveis_ensino(event=None):
        tipo = combo_tipo_vaga.get()
        if tipo == "Aprendiz":
            combo_nivel_ensino['values'] = ["Todos", "Ensino Fundamental", "Ensino Médio"]
        elif tipo == "Estágio":
            combo_nivel_ensino['values'] = ["Todos", "Ensino Médio", "Técnico", "Superior"]
        else:
            combo_nivel_ensino['values'] = ["Ensino Fundamental", "Ensino Médio", "Técnico", "Superior"]
        combo_nivel_ensino.set("")

    # Envia os dados preenchidos pelo usuário
    def enviar_dados():
        tipo_vaga = combo_tipo_vaga.get()
        formato_vaga = combo_formato_vaga.get()
        estado = combo_estado.get()
        nivel_ensino = combo_nivel_ensino.get()
        area_profissional = combo_area_profissional.get()

        print(f"""
        Tipo de Vaga: {tipo_vaga}
        Formato da Vaga: {formato_vaga}
        Estado: {estado}
        Nível de Ensino: {nivel_ensino}
        Área Profissional: {area_profissional}
        """)
        # Chama a função que interage com o site
        verificador = clica_site(tipo_vaga, nivel_ensino, area_profissional, estado)

        if verificador == 'Nenhum dado na lista':
            messagebox.showinfo("Aviso", "Não há Vagas dessa área ou na região escolhida!")

    # Função placeholder para o botão Carregar Excel
    def carregar_planilha():
        janela.destroy()
        tela_resultados_vagas()

    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Dados da Vaga")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    # Centralizar a janela na tela
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    window_width = int(screen_width * 0.45)
    window_height = int(screen_height * 0.75)
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Cabeçalho da janela
    top_frame = tk.Frame(janela, bg="#0052cc", height=int(window_height * 0.2))
    top_frame.pack(fill="x")
    titulo = tk.Label(top_frame, text="Informações da Vaga", font=("Helvetica", 24, "bold"), fg="white", bg="#0052cc")
    titulo.place(relx=0.5, rely=0.5, anchor="center")

    # Área do formulário principal
    frame_form = tk.Frame(janela, bg="#ffffff", padx=30, pady=30)
    frame_form.place(relx=0.5, rely=0.58, anchor="center")

    # Tipo de vaga (Nova opção adicionada)
    tk.Label(frame_form, text="Tipo de Vaga", bg="white", font=("Helvetica", 12)).pack(anchor="w")
    combo_tipo_vaga = ttk.Combobox(
        frame_form,
        values=["Todas", "Aprendiz", "Estágio", "Processos Públicos", "Soluções Especiais", "PCD"],
        font=("Helvetica", 12),
        state="readonly"
    )
    combo_tipo_vaga.pack(pady=5)
    combo_tipo_vaga.current(0)
    combo_tipo_vaga.bind("<<ComboboxSelected>>", atualizar_niveis_ensino)  # Quando mudar tipo de vaga

    # Formato da vaga (Presencial, Remoto, Híbrido)
    tk.Label(frame_form, text="Formato da Vaga", bg="white", font=("Helvetica", 12)).pack(anchor="w")
    combo_formato_vaga = ttk.Combobox(
        frame_form,
        values=["Todas", "Presencial", "Remoto", "Híbrido"],
        font=("Helvetica", 12),
        state="readonly"
    )
    combo_formato_vaga.pack(pady=5)
    combo_formato_vaga.current(0)

    # Estado (cidade - UF)
    tk.Label(frame_form, text="Estado (Cidade - UF)", bg="white", font=("Helvetica", 12)).pack(anchor="w")
    cidades = [  # lista completa como no seu código...
        "SÃO PAULO - SP", "Osasco - SP", "Barueri - SP", "Campinas - SP", "Sorocaba - SP", "Ribeirão Preto - SP",
        # ...
        "Palmas - TO"
    ]
    combo_estado = ttk.Combobox(frame_form, values=cidades, font=("Helvetica", 12), state="readonly", width=40)
    combo_estado.pack(pady=5)

    # Nível de Ensino
    tk.Label(frame_form, text="Nível de Ensino", bg="white", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0))
    combo_nivel_ensino = ttk.Combobox(
        frame_form,
        values=["Ensino Fundamental", "Ensino Médio", "Técnico", "Superior"],
        font=("Helvetica", 12),
        state="readonly"
    )
    combo_nivel_ensino.pack(pady=5)
    combo_nivel_ensino.bind("<<ComboboxSelected>>", atualizar_areas_profissionais)

    # Área Profissional
    tk.Label(frame_form, text="Área Profissional", bg="white", font=("Helvetica", 12)).pack(anchor="w")
    combo_area_profissional = ttk.Combobox(frame_form, font=("Helvetica", 12), state="readonly", width=40)
    combo_area_profissional.pack(pady=5)

    # Frame para os botões lado a lado
    frame_botoes = tk.Frame(frame_form, bg="white")
    frame_botoes.pack(pady=20)

    # Botão Enviar
    botao_enviar = tk.Button(
        frame_botoes,
        text="Enviar",
        font=("Helvetica", 12, "bold"),
        bg="#0052cc",
        fg="white",
        width=12,
        height=2,
        command=enviar_dados
    )
    botao_enviar.pack(side="left", padx=10)

    botao_carregar_planilha = tk.Button(
        frame_botoes,
        text="Planilha",
        font=("Helvetica", 12, "bold"),
        bg="#00802b",
        fg="white",
        width=12,
        height=2,
        command=carregar_planilha
    )
    botao_carregar_planilha.pack(side="left", padx=10)

    janela.mainloop()

if __name__ == '__main__':
    pass