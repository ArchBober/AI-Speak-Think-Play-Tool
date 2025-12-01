from google import genai
from google.genai import types
import whisper

import sys
import os

from dotenv import load_dotenv

print("got init")

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        # TODO implement args
        print("Audio-Text-Speach AI - no args")
        sys.exit(1)

    api_key = os.environ.get("YOUR_VERTEX_AI_API_KEY")

    # ctrl+c ctrl+v from wshiper readme but work perfectly

    model_audio = whisper.load_model("turbo")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("Samples/message_accepted.wav")
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model_audio.dims.n_mels).to(model_audio.device)

    # detect the spoken language
    # TODO add loop if lang != EN or enforce EN transciption
    _, probs = model_audio.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result_audio_trans = whisper.decode(model_audio, mel, options)

    # print the recognized text
    print(result_audio_trans)


    client = genai.Client(
            vertexai=True, api_key=api_key,
        )

    print("Client initialized. Sending request...")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=result_audio_trans.text
        )
        
        print("\n--- Response ---")
        print(response.text)
        print("----------------")

        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
        
    except Exception as e:
        print(f"\nError: {e}")



if __name__ == "__main__":
    main()