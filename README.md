# Jaspr CLI Generator
A rough AI-powered CLI that generates client-side Jaspr web apps from text prompts. Built with Python, Google Gemini, and Rich for CLI output.

Right now:

Many features are incomplete or unreliable

AI project generation isn’t consistent

The pipeline needs refactoring

Some generated code doesn’t run without manual fixes

So if you open the repo and think “why is this written like this?”
…the answer is: because I was trying things 😂


## Installation

### Prerequisites
- Python 3.8+
- Dart SDK (for running generated Jaspr projects)
- Google Gemini API key

### Setup
1. Clone or download the repository:
   ```bash
   git clone <repo-url>
   cd jaspr-cli-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or, for global installation (recommended):
   ```bash
   pip install . (Run as administrator )
   ```
   (Run as administrator on Windows for system-wide installation, making `jasprai` available globally)

3. Set up environment:
   - Create a `.env` file with your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Get the key from [Google AI Studio](https://aistudio.google.com/)

4. Run the CLI:
   ```bash
   jasprai
   ```
   (If installed locally, use `python cli.py`)

## Usage

### Interactive Shell
- Start with `jasprai`.
- Enter prompts like:
  - `build a portfolio site`
  - `create an e-commerce landing page`
- Use `help` for commands, `exit` to quit.

### Generated Project Structure
```
project_name/
├── lib/
│   ├── main.dart          # Entry point
│   ├── app.dart           # Main app component
│   ├── pages/             # Page components
│   └── components/        # Reusable components
├── web/
│   ├── index.html         # HTML template
│   ├── styles.css         # Custom styles
│   └── tailwind.css       # Tailwind CSS (if used)
└── pubspec.yaml           # Dependencies and config
```

### Running Generated Projects
1. Navigate to the project:
   ```bash
   cd project_name
   ```

2. Install dependencies:
   ```bash
   dart pub get
   ```

3. Serve the app:
   ```bash
   dart run jaspr serve
   ```

4. Build for production:
   ```bash
   dart run jaspr build
   ```

## How It Works

### Architecture
- **ai.py**: Handles AI prompts using Gemini API, parses JSON responses.
- **generator.py**: Writes files from AI-generated structure, skips directories.
- **cli.py**: Interactive shell with Rich UI for user interaction.
- **prompts.py**: Contains SYSTEM_PROMPT for guiding AI generation.
- **previews/preview.py**: Rich-formatted file previews.

### AI Generation Flow
1. User enters prompt (e.g., "build a blog").
2. AI analyzes prompt, plans structure, outputs JSON with `files` and `commands`.
3. Generator creates files, runs commands (e.g., `dart pub get`).
4. Preview shows results.


## Troubleshooting

- **Import Errors**: Clear `__pycache__` and restart.
- **AI No Response**: Check API key, internet, or prompt length.
- **Generation Issues**: Ensure prompts are descriptive (e.g., "build a simple website").
- **Rich UI Not Working**: Install `rich` via pip.

## Contributing
## 🤝 Welcome Contributors!

Thanks for stopping by! Whether you’re fixing a bug, improving documentation, adding features, or just exploring — you’re welcome here.  
Your contributions, ideas, and feedback mean a lot and help this project grow stronger.

Feel free to open an issue, start a discussion, or submit a pull request anytime.  
Let’s build something awesome together! 🚀

1. Fork the repo.
2. Create a feature branch.
3. Make changes, test with `jasprai`.
4. Submit a PR with description.

### Guidelines
- Keep code clean, add comments.
- Update docs for new features.
- Test AI prompts thoroughly.

## License

MIT License. See LICENSE file for details.



NOTE: I built this README in a bit of a hurry, so if you notice anything missing or have suggestions, feel free to reach out. You can message me on Discord (ID on my profile).
