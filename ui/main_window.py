import os

from core.video_info import VideoInfo
from core.converter import Converter

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QFileDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

class DropArea(QFrame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.setAcceptDrops(True)

        self.setStyleSheet("""
        QFrame{
            border:3px dashed #4A90E2;
            border-radius:15px;
            background:#2b2b2b;
        }

        QLabel{
            color:white;
            font-size:20px;
        }
        """)

        layout = QVBoxLayout(self)

        self.label = QLabel(
            "📹\n\nArraste um vídeo MP4 aqui\n\nou clique no botão abaixo"
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

        self.parent.video_loaded(arquivo)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.resize(900,600)
        self.setMinimumSize(900,600)

        self.setWindowTitle("VideoStudio AI")

        self.create_menu()

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.drop = DropArea(self)
        self.drop.setMaximumHeight(330)




        layout.addWidget(self.drop, 1)

        self.button = QPushButton("Selecionar Vídeo")

        self.button.setFixedHeight(45)

        self.button.clicked.connect(self.open_video)
#aqui
        buttons = QHBoxLayout()

        buttons.addWidget(self.button)

        self.convert_button = QPushButton("🚀 Converter")
        self.convert_button.setFixedHeight(45)
        self.convert_button.clicked.connect(self.convert_video)
        buttons.addWidget(self.convert_button)
        layout.addLayout(buttons,0)
#at aqui
        self.statusBar().showMessage("Aguardando vídeo...")

        self.setStyleSheet("""

        QMainWindow{

        background:#202124;

    }

        QPushButton{

            background:#1976D2;

            color:white;

            font-size:16px;

            border:none;

            border-radius:8px;

            padding:10px;

        }

        QPushButton:hover{

            background:#2196F3;

        }

        QMenuBar{

            background:#2a2a2a;

            color:white;

        }

        QStatusBar{

            background:#2a2a2a;

            color:white;

        }

        """)

    def create_menu(self):

        menu=self.menuBar()

        arquivo=menu.addMenu("Arquivo")

        abrir=QAction("Abrir Vídeo",self)

        abrir.triggered.connect(self.open_video)

        arquivo.addAction(abrir)

    def open_video(self):

        arquivo,_=QFileDialog.getOpenFileName(

            self,

            "Selecionar vídeo",

            "",

            "Vídeos (*.mp4 *.mov *.avi *.mkv)"

        )

        if arquivo:

            self.video_loaded(arquivo)

    def video_loaded(self,arquivo):

       self.video = arquivo
       nome = os.path.basename(arquivo)
       self.drop.label.setText(f"✅\n\n{nome}")

       self.statusBar().showMessage("Vídeo carregado.")
       info = VideoInfo.get(arquivo)

       print(info)
    
    def convert_video(self):

        if not hasattr(self, "video"):
            self.statusBar().showMessage("Selecione um vídeo primeiro.")
            return

        saida = Converter.to_reels(self.video)

        self.statusBar().showMessage(f"Concluído: {saida}")