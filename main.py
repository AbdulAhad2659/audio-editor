import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog,
    QLabel, QSlider, QPushButton, QLineEdit,
    QVBoxLayout, QWidget, QProgressBar, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5 import uic
from pydub import AudioSegment

from utils.audio_utils import trim_audio, fade_in_audio, fade_out_audio, boost_volume

# UI file path (make sure this is correct)
UI_FILE = os.path.join(os.path.dirname(__file__), "ui", "mainwindow.ui")

class AudioEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_FILE, self)  # Load UI file

        # UI elements (make sure object names match those in Qt Designer)
        self.filePathLineEdit = self.findChild(QLineEdit, "filePathLineEdit")
        self.browseButton = self.findChild(QPushButton, "browseButton")
        self.startTimeSlider = self.findChild(QSlider, "startTimeSlider")
        self.endTimeSlider = self.findChild(QSlider, "endTimeSlider")
        self.trimButton = self.findChild(QPushButton, "trimButton")
        self.fadeInButton = self.findChild(QPushButton, "fadeInButton")
        self.fadeOutButton = self.findChild(QPushButton, "fadeOutButton")
        self.volumeBoostButton = self.findChild(QPushButton, "volumeBoostButton")
        self.statusLabel = self.findChild(QLabel, "statusLabel")
        self.startTimeLabel = self.findChild(QLabel, "startTimeLabel")
        self.endTimeLabel = self.findChild(QLabel, "endTimeLabel")

        # Initial setup
        self.audio_file = None
        self.duration = 0

        # Connections
        self.browseButton.clicked.connect(self.browse_file)
        self.trimButton.clicked.connect(self.trim_and_save)
        self.fadeInButton.clicked.connect(self.apply_fade_in)
        self.fadeOutButton.clicked.connect(self.apply_fade_out)
        self.volumeBoostButton.clicked.connect(self.apply_volume_boost)
        self.startTimeSlider.valueChanged.connect(self.update_start_time_label)
        self.endTimeSlider.valueChanged.connect(self.update_end_time_label)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open MP3 File", "", "MP3 Files (*.mp3)")
        if file_name:
            self.audio_file = file_name
            print(self.audio_file)
            self.filePathLineEdit.setText(file_name)
            self.load_audio_file()

    def load_audio_file(self):
        if self.audio_file:
            try:
                audio = AudioSegment.from_file(self.audio_file)
                self.duration = audio.duration_seconds
                self.startTimeSlider.setMaximum(int(self.duration))
                self.endTimeSlider.setMaximum(int(self.duration))
                self.endTimeSlider.setValue(int(self.duration))
                self.statusLabel.setText(f"Loaded file: {os.path.basename(self.audio_file)}")
            except Exception as e:
                self.statusLabel.setText(f"Error loading file: {e}")

    def update_start_time_label(self):
        start_time = self.startTimeSlider.value()
        self.startTimeLabel.setText(f"Start Time (s): {start_time}")

    def update_end_time_label(self):
        end_time = self.endTimeSlider.value()
        self.endTimeLabel.setText(f"End Time (s): {end_time}")

    def trim_and_save(self):
        if not self.audio_file:
            QMessageBox.warning(self, "Error", "Please select an audio file.")
            return
        start_time = self.startTimeSlider.value()
        end_time = self.endTimeSlider.value()

        if start_time >= end_time:
            QMessageBox.warning(self, "Error", "Start time must be less than end time.")
            return

        output_file, _ = QFileDialog.getSaveFileName(self, "Save Trimmed File", "", "MP3 Files (*.mp3)")
        if output_file:
            success, message = trim_audio(self.audio_file, output_file, start_time, end_time)
            if success:
                self.statusLabel.setText(message)
            else:
                QMessageBox.critical(self, "Error", f"Failed to trim audio: {message}")

    def apply_fade_in(self):
        if not self.audio_file:
            QMessageBox.warning(self, "Error", "Please select an audio file.")
            return
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Audio with Fade In", "", "MP3 Files (*.mp3)")
        if output_file:
            success, message = fade_in_audio(self.audio_file, output_file)
            if success:
                self.statusLabel.setText(message)
            else:
                QMessageBox.critical(self, "Error", f"Failed to apply fade-in: {message}")

    def apply_fade_out(self):
        if not self.audio_file:
            QMessageBox.warning(self, "Error", "Please select an audio file.")
            return
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Audio with Fade Out", "", "MP3 Files (*.mp3)")
        if output_file:
            success, message = fade_out_audio(self.audio_file, output_file)
            if success:
                self.statusLabel.setText(message)
            else:
                QMessageBox.critical(self, "Error", f"Failed to apply fade-out: {message}")

    def apply_volume_boost(self):
        if not self.audio_file:
            QMessageBox.warning(self, "Error", "Please select an audio file.")
            return
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Audio with Volume Boost", "", "MP3 Files (*.mp3)")
        if output_file:
            success, message = boost_volume(self.audio_file, output_file)
            if success:
                self.statusLabel.setText(message)
            else:
                QMessageBox.critical(self, "Error", f"Failed to boost volume: {message}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioEditor()
    window.show()
    sys.exit(app.exec_())