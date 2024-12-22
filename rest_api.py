import requests
import json

def translate_text(text, target_lang='cs'):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"en|{target_lang}"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        translated_text = data['responseData']['translatedText']
        print(f"Translated Text (Czech): {translated_text}")
        return translated_text
    except requests.exceptions.RequestException as e:
        print(f"Error during translation: {e}")
        return None

def analyze_text_with_udpipe(text, model='czech-pdt-ud-2.5-191206'):
    url = "https://lindat.mff.cuni.cz/services/udpipe/api/process"
    params = {
        "model": model,
        "data": text,
        "tokenizer": "yes",
        "tagger": "yes",
        "parser": "yes"
    }
    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during UDPipe analysis: {e}")
        return None

def display_analysis(analysis):
    
    if analysis and "result" in analysis:
        print("\nAnalysis:")
        for line in analysis["result"].split("\n"):
            if not line.startswith("#") and line.strip():
                parts = line.split("\t")
                if len(parts) >= 8:
                    token, lemma, upos, xpos, feats, head, deprel = parts[1:8]
                    print(f"Token: {token}, Lemma: {lemma}, POS: {upos}, Dependency Relation: {deprel}")
    else:
        print("No analysis results available.")

def main():
    # Input text to be translated and analyzed
    input_text = "Hi, My name is Naeem. I am a student and I live in Prague"

    print(f"Original Text: {input_text}\n")

    # Translate the text from English to Czech
    translated_text = translate_text(input_text)
    if not translated_text:
        print("Translation failed. Exiting.")
        return

    # Analyze the translated text using UDPipe
    analysis_result = analyze_text_with_udpipe(translated_text)
    if not analysis_result:
        print("Analysis failed. Exiting.")
        return

    # Analysis results
    display_analysis(analysis_result)

if __name__ == "__main__":
    main()
