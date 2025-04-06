# transcriber
Containerized transcriber using whisper

## Other ways to do this
- Windows + H.
- Other packaged dictation apps (like on Word with Office365).

This project provides a Docker container for transcribing audio files using OpenAI's Whisper.

## Prerequisites

* **Docker Desktop:** Ensure Docker Desktop is installed and running on your system.
* **Audio File:** You'll need an audio file (e.g., `.m4a`, `.wav`) that you want to transcribe.

## Installation and Usage

1.  **Clone the Repository (Optional):**

    * If you've cloned the repository from GitHub, navigate to the project directory in your terminal.

2.  **Place Audio File:**

    * Place your audio file (e.g., `test_audio.m4a`) in a directory named `audio` within the project directory (the same location as the `Dockerfile`).

3.  **Build the Docker Image:**

    * Open your terminal or command prompt and navigate to the project directory.
    * Run the following command to build the Docker image:

        ```bash
        docker build -t whisper-test .
        ```

4.  **Run the Docker Container:**

    * Execute the following command to run the container and transcribe your audio file:

        * **PowerShell:**

            ```powershell
            docker run -v "C:\Users\Kieran\Documents\Diary\transcriber\audio:/audio" -v "C:\Users\Kieran\Documents\Diary\transcriber\output:/output" whisper-test
            ```

        * **Command Prompt (cmd.exe):**

            ```batch
            docker run -v "%cd%/audio:/audio" -v "%cd%:/output" whisper-test
            ```

    * The transcribed text will be saved to a file named `transcription.txt` in the same directory as your audio file.

## Notes

* The container uses `ffmpeg` to handle various audio formats.
* The `CMD` instruction in the `Dockerfile` is configured to transcribe the audio file named `test_audio.m4a`. If your file has a different name, make sure to update the `CMD` within the `Dockerfile`, and then rebuild the docker image.
* The output directory is mounted to the current directory, so the `transcription.txt` file will be created in the same directory where you run the docker command.
* If you encounter any file not found errors, double check the names of the files, and the location of the audio directory.