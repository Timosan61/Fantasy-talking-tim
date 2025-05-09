import cog
import subprocess

class Predictor(cog.Predictor):
    def setup(self):
        # Здесь можно загрузить модель, если нужно
        pass

    @cog.input("audio", type=str, help="Path to input audio file")
    def predict(self, audio):
        output_path = "output.mp4"
        
        # Здесь вставь свою команду для запуска fantasy-talking
        # Пример (замени на свой скрипт!)
        command = [
            "python",
            "main.py",
            "--audio_input", audio,
            "--output_file", output_path
        ]
        
        subprocess.run(command, check=True)
        
        return output_path