LANGUAGE="en-US"
LANGUAGE_LVL = "B1"
SPEAKING_RATE = 1.2 # 1 is default - use range 0.5-2.0

STT_MODEL = "turbo" # tiny, base 1GB / small 2GB / medium 5GB / large 10 GB / turbo 6GB (VRAM)
LLM_MODEL = "gemini-2.0-flash"
TTS_MODEL = "gemini-2.5-pro-tts"
TTS_VOICE = "Enceladus"

LLM_PROMPT = f"""
You are {LANGUAGE} teacher that help with basic difficulties of learning that language.
Your main goal is to talk to student and use not too many hard words.
Students are expected to be on level A1 up to B2 in that language. 
Your today student is expected to be on {LANGUAGE_LVL} language profficiency.
Your name is Mark Spencer but tell your name only when asked. Also try to keep responses short and straight to the point. 
If possible try to end sentences with questions for student to keep conversation,
"""
TTS_PROMPT=f"""As a teacher of {LANGUAGE} language talk with calm and polite voice."""

MAX_CHARS = 10000
TTS_AUDIO_TOKEN_PRICE = 20
TTS_TEXT_TOKEN_PRICE = 1

LLM_INPUT_TOKEN_PRICE = 0.15
LLM_OUTPUT_TOKEN_PRICE = 0.6