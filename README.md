# ScriptorAInuli


**ScriptorAInuli** is an AI-powered tool for generating textual descriptions of historical rings (or other objects). This project was developed as part of my methods paper at the University of Zurich in the field of digital history & AI.
<br> Für Deutsch siehe unten. 

## How to use

- Make sure you have the API-Key set.
	- If you are not sure see **Installation** or run the `check_for_key.py` file.

- Save your images as .jpg in the `\images` folder. Create one if it doesn't exist.

- If needed change the variables `start_num` and `num_of_images` to change where you want to start and how many images you want described.

- Run `img_to_description.py`.
  
  
## File Overview

-  `.gitattributes`

-  `.gitignore`

-  `README.md` This documentation file

-  `check_for_key.py` Checks for the presence of required API keys

-  `img_to_description.py` Main logic for converting ring images into descriptive text using AI. For converting other object you only need to change the prompt.

-  `instructions.py`: Contains the prompt and the model instruction

  

## Installation

  

### 1. **Clone the repository:**

  

```bash

git  clone  https://github.com/your-username/ScriptorAInuli.git

cd  ScriptorAInuli

```

  

### 2. **Create a virtual environment (recommended):**

  

```bash

git  clone  https://github.com/your-username/ScriptorAInuli.git

cd  ScriptorAInuli

```

  

### 3. **Install dependencies:**

  

```bash

pip  install  -r  requirements.txt

```

  

### 4. **Check for API Key**

Run `check_for_key.py` to see if an API key is already saved in your environment.

  

> ⚠️ **Note:** This script only checks whether the `OPENAI_API_KEY` environment variable is set. It does **not** verify if the key is valid for the OpenAI API.

  

If the key is **not set**, run the following command in your Windows **Command Prompt** (CMD):

```bash

setx  OPENAI_API_KEY  "your_api_key_here"

```

> 📌 **Important:** This adds the key to your user environment variables. You’ll need to **restart your terminal** for it to take effect in new sessions.

  

To use the key immediately in the current CMD window:

```bash

set  OPENAI_API_KEY=your_api_key_here

```

You can verify if it is set by running:

```bash

echo  %OPENAI_API_KEY%

```
---



# ScriptorAInuli[^1]

**ScriptorAInuli** ist ein KI-gestütztes Tool zur Generierung von Textbeschreibungen historischer Ringe (oder anderer Objekte). Dieses Projekt wurde im Rahmen meiner Methodenseminararbeit an der Universität Zürich im Bereich der Digital History & KI entwickelt.

## Nutzung

-   Stelle sicher, dass der API-Schlüssel gesetzt ist.
    
    -   Falls du dir unsicher bist, siehe **Installation** oder führe die Datei `check_for_key.py` aus.
        
-   Speichere deine Bilder als .jpg im Ordner `\images`. Erstelle ihn, falls er nicht existiert.
    
-   Falls nötig, ändere die Variablen `start_num` und `num_of_images`, um festzulegen, bei welchem Bild du starten und wie viele Bilder du beschreiben lassen möchtest.
    
-   Führe `img_to_description.py` aus.
    

## Dateiübersicht

-   `.gitattributes`
    
-   `.gitignore`
    
-   `README.md` Diese Dokumentationsdatei
    
-   `check_for_key.py` Prüft das Vorhandensein des benötigten API-Schlüssels
    
-   `img_to_description.py` Hauptlogik zur Umwandlung von Ringbildern in beschreibenden Text mithilfe von KI. Um andere Objekte zu beschreiben, musst du nur den Prompt ändern.
    
-   `instructions.py`: Enthält den Prompt und die Modellanweisungen
    

## Installation

### 1. **Repository klonen:**

```bash
git  clone  https://github.com/your-username/ScriptorAInuli.git
cd  ScriptorAInuli

```

### 2. **Virtuelle Umgebung erstellen (empfohlen):**

```bash
git  clone  https://github.com/your-username/ScriptorAInuli.git
cd  ScriptorAInuli

```

### 3. **Abhängigkeiten installieren:**

```bash
pip  install  -r  requirements.txt

```

### 4. **API-Schlüssel prüfen**

Führe `check_for_key.py` aus, um zu prüfen, ob ein API-Schlüssel bereits in deiner Umgebung gespeichert ist.

> ⚠️ **Hinweis:** Dieses Skript prüft nur, ob die Umgebungsvariable `OPENAI_API_KEY` gesetzt ist. Es prüft **nicht**, ob der Schlüssel für die OpenAI API gültig ist.

Wenn der Schlüssel **nicht gesetzt** ist, führe im Windows **Command Prompt** (CMD) den folgenden Befehl aus:

```bash
setx  OPENAI_API_KEY  "your_api_key_here"

```

> 📌 **Wichtig:** Dieser Befehl fügt den Schlüssel zu den Umgebungsvariablen deines Benutzers hinzu. Du musst dein Terminal **neu starten**, damit er in neuen Sitzungen verfügbar ist.

Um den Schlüssel sofort im aktuellen CMD-Fenster zu verwenden:

```bash
set  OPENAI_API_KEY=your_api_key_here

```

Du kannst überprüfen, ob er gesetzt ist, indem du folgendes eingibst:

```bash
echo  %OPENAI_API_KEY%

```

---
[^1]: Diese Übersetztung wurde mit ChatGPT generiert.