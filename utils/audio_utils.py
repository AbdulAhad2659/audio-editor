from pydub import AudioSegment

def trim_audio(input_file, output_file, start_time, end_time):
    """Trims the audio file."""
    try:
        audio = AudioSegment.from_file(input_file)
        start_ms = int(start_time * 1000)
        end_ms = int(end_time * 1000)
        trimmed_audio = audio[start_ms:end_ms]
        trimmed_audio.export(output_file, format="mp3")
        return True, "Audio trimmed successfully!"
    except Exception as e:
        return False, str(e)

def fade_in_audio(input_file, output_file, duration_seconds=2):
    """Applies a fade-in effect to the audio."""
    try:
        audio = AudioSegment.from_file(input_file)
        fade_in_duration_ms = duration_seconds * 1000
        faded_audio = audio.fade_in(fade_in_duration_ms)
        faded_audio.export(output_file, format="mp3")
        return True, "Fade-in applied successfully!"
    except Exception as e:
        return False, str(e)

def fade_out_audio(input_file, output_file, duration_seconds=2):
    """Applies a fade-out effect to the audio."""
    try:
        audio = AudioSegment.from_file(input_file)
        fade_out_duration_ms = duration_seconds * 1000
        faded_audio = audio.fade_out(fade_out_duration_ms)
        faded_audio.export(output_file, format="mp3")
        return True, "Fade-out applied successfully!"
    except Exception as e:
        return False, str(e)

def boost_volume(input_file, output_file, volume_change_db=5):
    """Increases the volume of the audio."""
    try:
        audio = AudioSegment.from_file(input_file)
        louder_audio = audio + volume_change_db
        louder_audio.export(output_file, format="mp3")
        return True, "Volume boosted successfully!"
    except Exception as e:
        return False, str(e)