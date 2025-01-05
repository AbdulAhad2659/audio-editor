# Audio Editor

This is a Python-based audio editor application with a graphical user interface (GUI) built using PyQt5 and `pydub`. It allows you to load MP3 files, trim them, apply fade-in/fade-out effects, and adjust the volume.

## Features

*   **MP3 File Support:** Loads and processes MP3 audio files.
*   **Trimming:** Trim audio files by selecting start and end times using sliders.
*   **Fade In/Out:** Apply fade-in and fade-out effects to the audio.
*   **Volume Boost:** Increase the volume of the audio file.
*   **GUI Interface:** User-friendly interface built with PyQt5.
*   **Status Updates:** Displays status messages to inform the user about the processing.

## Installation

1. **Prerequisites:**

    *   Python 3.x
    *   FFmpeg (required by `pydub` for audio processing)

2. **Install FFmpeg:**

    *   **Windows:**
        *   Download a static build from the official website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
        *   Extract the downloaded archive (e.g., to `C:\ffmpeg`).
        *   Add the `bin` directory of the extracted folder to your system's `PATH` environment variable (e.g., `C:\ffmpeg\bin`).
        *   Restart your computer for the changes to take effect.
    *   **macOS:**
        *   Install using Homebrew (if you have it): `brew install ffmpeg`
        *   Or download and install from the FFmpeg website.
    *   **Linux:**
        *   Use your distribution's package manager. For example, on Ubuntu/Debian: `sudo apt-get install ffmpeg`

3. **Clone the Repository:**

    ```bash
    git clone https://github.com/AbdulAhad2659/audio-editor.git
    cd audio-editor
    ```

4. **Create and Activate a Virtual Environment (Recommended):**

    *   **Windows:**

        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    *   **macOS/Linux:**

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

5. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (Make sure to create a `requirements.txt` file with the following content: `PyQt5`, `pydub`)

## Usage

1. **Run the Application:**

    ```bash
    python main.py
    ```

2. **Using the Application:**

    *   **Browse:** Click the "Browse" button to select an MP3 file.
    *   **Trim:** Adjust the "Start Time" and "End Time" sliders to select the portion you want to trim.
    *   **Trim:** Click the "Trim" button to create a new trimmed MP3 file.
    *   **Fade In/Out:** Use the respective buttons to apply fade-in or fade-out effects.
    *   **Volume Boost:** Use the "Volume Boost" button to increase the volume.
    *   **Status:** The status bar at the bottom will display messages about the processing.


## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin my-feature-branch`
5. Create a pull request.

## License

This project is licensed under the MIT License.