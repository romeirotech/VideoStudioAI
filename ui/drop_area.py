from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class DropArea(QFrame):

    def __init__(self, callback):

        super().__init__()

        self.callback = callback

        self.setAcceptDrops(True)

        self.setStyleSheet("""

        QFrame{

            border:3px dashed #4A90E2;

            border-radius:15px;

            background:#2b2b2b;

        }

        QLabel{

            color:white;

            font-size:22px;

        }

        """)

        layout = QVBoxLayout(self)

        self.label = QLabel(

            "📹\n\nArraste seu vídeo aqui\n\nou clique em Selecionar"

        )

        self.label.setAlignment(Qt.AlignCenter)

        layout.addStretch()

        layout.addWidget(self.label)

        layout.addStretch()

    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls():

            event.acceptProposedAction()

    def dropEvent(self, event):

        arquivo = event.mimeData().urls()[0].toLocalFile()

        self.callback(arquivo)

    def setVideo(self, arquivo):

        self.label.setText(

            "✅\n\n"

            + arquivo

        )