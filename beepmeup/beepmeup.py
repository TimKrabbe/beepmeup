import platform
import subprocess


def beep(frequency=440, duration=500):
    system = platform.system()

    if system == "Windows":
        import winsound
        winsound.Beep(frequency, duration)

    elif system == "Linux":
        subprocess.run(["beep", "-f", str(frequency), "-l", str(duration)], 
                      check=False)

    elif system == "Darwin":  # Mac
        # frequency und duration werden hier ignoriert, afplay spielt eine Audiodatei
        subprocess.run(["afplay", "/System/Library/Sounds/Ping.aiff"], 
                      check=False)