from PySide6.QtWidgets import QFrame, QLabel, QFormLayout


class InfoPanel(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""

        QFrame{

            background:#2b2b2b;

            border-radius:12px;

            padding:10px;

        }

        QLabel{

            color:white;

            font-size:14px;

        }

        """)

        layout = QFormLayout(self)

        self.nome = QLabel("-")
        self.resolucao = QLabel("-")
        self.fps = QLabel("-")
        self.duracao = QLabel("-")
        self.tamanho = QLabel("-")

        layout.addRow("📄 Nome:", self.nome)
        layout.addRow("📺 Resolução:", self.resolucao)
        layout.addRow("🎞 FPS:", self.fps)
        layout.addRow("⏱ Duração:", self.duracao)
        layout.addRow("💾 Tamanho:", self.tamanho)

    def update_info(self, info):

        self.nome.setText(info["arquivo"])
        self.resolucao.setText(f'{info["largura"]} x {info["altura"]}')
        self.fps.setText(str(info["fps"]))
        self.duracao.setText(str(info["duracao"]))
        self.tamanho.setText(f'{info["tamanho"]} MB')