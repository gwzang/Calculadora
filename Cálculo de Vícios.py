import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Calculadora de Gastos com Vícios")
janela.geometry("1920x1080")
janela.grid_rowconfigure(list(range(12)), weight=1)
janela.grid_columnconfigure(0, weight=1)

# Título
titulo = ctk.CTkLabel(janela, text="Calculadora de Vícios",
                      font=ctk.CTkFont(size=20, weight="bold"))
titulo.grid(row=0, column=0, pady=20, sticky="ew")

# ---------------------- CIGARRO ----------------------
ctk.CTkLabel(janela, text="Cigarro", font=ctk.CTkFont(
    size=16, weight="bold")).grid(row=1, column=0, sticky="w", padx=20)

frame_cigarro = ctk.CTkFrame(janela)
frame_cigarro.grid(row=2, column=0, pady=5, padx=20, sticky="ew")
frame_cigarro.grid_columnconfigure((0, 1, 2), weight=1)

entrada_cigarros_dia = ctk.CTkEntry(
    frame_cigarro, placeholder_text="Cigarros por dia")
entrada_preco_carteira = ctk.CTkEntry(
    frame_cigarro, placeholder_text="Preço da carteira")
entrada_qtd_carteira = ctk.CTkEntry(
    frame_cigarro, placeholder_text="Cigarros por carteira")

entrada_cigarros_dia.grid(row=0, column=0, padx=5, sticky="ew")
entrada_preco_carteira.grid(row=0, column=1, padx=5, sticky="ew")
entrada_qtd_carteira.grid(row=0, column=2, padx=5, sticky="ew")

# ---------------------- ÁLCOOL ----------------------
ctk.CTkLabel(janela, text="Álcool", font=ctk.CTkFont(
    size=16, weight="bold")).grid(row=3, column=0, sticky="w", padx=20)

frame_alcool = ctk.CTkFrame(janela)
frame_alcool.grid(row=4, column=0, pady=5, padx=20, sticky="ew")
frame_alcool.grid_columnconfigure((0, 1), weight=1)

entrada_freq_alcool = ctk.CTkEntry(
    frame_alcool, placeholder_text="Consumo por semana")
entrada_gasto_alcool = ctk.CTkEntry(
    frame_alcool, placeholder_text="Gasto por vez")

entrada_freq_alcool.grid(row=0, column=0, padx=5, sticky="ew")
entrada_gasto_alcool.grid(row=0, column=1, padx=5, sticky="ew")

# ---------------------- JOGOS DE AZAR ----------------------
ctk.CTkLabel(janela, text="Jogos de Azar", font=ctk.CTkFont(
    size=16, weight="bold")).grid(row=5, column=0, sticky="w", padx=20)

frame_jogos_de_azar = ctk.CTkFrame(janela)
frame_jogos_de_azar.grid(row=6, column=0, pady=5, padx=20, sticky="ew")
frame_jogos_de_azar.grid_columnconfigure((0, 1), weight=1)

entrada_freq_jogos = ctk.CTkEntry(
    frame_jogos_de_azar, placeholder_text="Vezes por semana")
entrada_gasto_jogos = ctk.CTkEntry(
    frame_jogos_de_azar, placeholder_text="Gasto semanal")

entrada_freq_jogos.grid(row=0, column=0, padx=5, sticky="ew")
entrada_gasto_jogos.grid(row=0, column=1, padx=5, sticky="ew")

# ---------------------- FAST FOOD ----------------------
ctk.CTkLabel(janela, text="Fast Food / Junk Foood",
             font=ctk.CTkFont(size=16, weight="bold")).grid(row=7, column=0, sticky="w", padx=20)

frame_junk = ctk.CTkFrame(janela)
frame_junk.grid(row=8, column=0, pady=5, padx=20, sticky="ew")
frame_junk.grid_columnconfigure((0, 1), weight=1)

entrada_freq_junk = ctk.CTkEntry(
    frame_junk, placeholder_text="Vezes por semana")
entrada_gasto_junk = ctk.CTkEntry(
    frame_junk, placeholder_text="Gasto semanal")

entrada_freq_junk.grid(row=0, column=0, padx=5, sticky="ew")
entrada_gasto_junk.grid(row=0, column=1, padx=5, sticky="ew")

# ---------------------- RESULTADO ----------------------
resultado_label = ctk.CTkLabel(
    janela, text="", font=ctk.CTkFont(size=16))
resultado_label.grid(row=9, column=0, pady=10, padx=20, sticky="ew")

# ---------------------- BOTÃO ----------------------
botao = ctk.CTkButton(janela, text="Calcular Gastos",
                      command=lambda: calcular_gastos())
botao.grid(row=10, column=0, pady=10, padx=20, sticky="ew")

# ---------------------- FRAME DO GRÁFICO ----------------------
frame_grafico = ctk.CTkFrame(janela, height=200)
frame_grafico.grid(row=11, column=0, padx=20, pady=10, sticky="nsew")

# ---------------------- FUNÇÃO DE CÁLCULO ----------------------


def calcular_gastos():
    try:
        # Cigarro
        cigarros_dia = int(entrada_cigarros_dia.get() or 0)
        preco_carteira = float(entrada_preco_carteira.get() or 0)
        qtd_carteira = int(entrada_qtd_carteira.get() or 1)
        gasto_cigarro = (cigarros_dia * 30 / qtd_carteira) * preco_carteira

        # Álcool
        freq_alcool = int(entrada_freq_alcool.get() or 0)
        gasto_alcool = float(entrada_gasto_alcool.get() or 0)
        gasto_alcool_total = freq_alcool * 4 * gasto_alcool

        # Jogos de Azar
        freq_jogos = int(entrada_freq_jogos.get() or 0)
        gasto_jogos = float(entrada_gasto_jogos.get() or 0)
        gasto_jogos_total = gasto_jogos * 4

        # Junk Food
        freq_junk = int(entrada_freq_junk.get() or 0)
        gasto_junk = float(entrada_gasto_junk.get() or 0)
        gasto_junk_total = gasto_junk * 4

        total = gasto_cigarro + gasto_alcool_total + \
            gasto_jogos_total + gasto_junk_total

        resultado = (
            f"Gasto mensal estimado:\n"
            f"• Cigarro: R$ {gasto_cigarro:.2f}\n"
            f"• Álcool: R$ {gasto_alcool_total:.2f}\n"
            f"• Jogos de Azar: R$ {gasto_jogos_total:.2f}\n"
            f"• Fast Food: R$ {gasto_junk_total:.2f}\n\n"
            f"💰 Total: R$ {total:.2f}"
        )

        resultado_label.configure(text=resultado)

        # Limpa gráfico anterior
        for widget in frame_grafico.winfo_children():
            widget.destroy()

        # Gráfico de pizza
        labels = ['Cigarro', 'Álcool', 'Jogos de Azar', 'Fast Food']
        valores = [gasto_cigarro, gasto_alcool_total,
                   gasto_jogos_total, gasto_junk_total]
        cores = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']

        fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
        fig.patch.set_facecolor('grey')
        ax.set_facecolor('grey')
        ax.pie(valores, labels=labels, autopct='%1.1f%%', colors=cores)
        ax.set_title("Distribuição dos Gastos", fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    except ValueError:
        resultado_label.configure(
            text="❗ Preencha todos os campos corretamente.")


janela.mainloop()
