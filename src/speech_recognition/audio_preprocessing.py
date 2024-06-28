# audio_preprocessing.py

import librosa
import numpy as np
import soundfile as sf

def load_audio(audio_file):
    """
    Load audio file and return the audio data and sample rate.
    """
    audio_data, sr = librosa.load(audio_file, sr=None)
    return audio_data, sr

def preprocess_audio(audio_data, sr):
    """
    Perform preprocessing on audio data.
    Example: Normalization and resampling.
    """
    # Normalize audio data
    audio_data = librosa.util.normalize(audio_data)

    # Resample audio to target sample rate (if necessary)
    target_sr = 16000  # Example target sample rate
    if sr != target_sr:
        audio_data = librosa.resample(audio_data, sr, target_sr)

    return audio_data, target_sr

def save_processed_audio(audio_data, sr, output_file):
    """
    Save processed audio data to a new file.
    """
    sf.write(output_file, audio_data, sr)

# Example usage
if __name__ == "__main__":
    input_audio_file = "path/to/your/input/audio_file.wav"
    output_audio_file = "path/to/your/output/processed_audio.wav"

    # Load audio file
    audio_data, sr = load_audio(input_audio_file)

    # Preprocess audio data
    processed_audio, new_sr = preprocess_audio(audio_data, sr)

    # Save processed audio to a new file
    save_processed_audio(processed_audio, new_sr, output_audio_file)
