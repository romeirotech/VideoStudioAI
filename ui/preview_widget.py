import cv2

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout


class PreviewWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.setMinimumHeight(320)

        self.setStyleSheet("""

        QFrame{

            background:#1f1f1f;

            border:2px solid #444;

            border-radius:12px;

        }

        QLabel{

            color:white;

            font-size:18px;

        }

        """)

        layout = QVBoxLayout(self)

        self.label = QLabel("Nenhum vídeo carregado")

        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

    def load_video(self, arquivo):

        cap = cv2.VideoCapture(arquivo)

        ok, frame = cap.read()

        cap.release()

        if not ok:
            self.label.setText("Não foi possível gerar o preview.")
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = frame.shape

        image = QImage(
            frame.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(image)

        pixmap = pixmap.scaled(
            700,
            300,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.label.setPixmap(pixmap)