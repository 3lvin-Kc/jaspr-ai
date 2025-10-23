# Jaspr CLI Generator
A simple AI-powered command-line tool to quickly build Jaspr (Dart web) websites from your text prompts. Powered by Python, Google Gemini AI, and Rich for colorful terminal feedback.

What It Does
AI Project Builder: Just tell it what you want (e.g., "build a portfolio site")—it designs and builds your Jaspr project using Google Gemini.

Client-Side Focus: Creates Jaspr web apps for the browser (not SSR).

Clean File Organization: Puts pages, components, and support files in the right folders (lib/pages/, lib/components/, web/).

Smart Dependencies: Automatically adds the latest Jaspr, Router, and Tailwind to your pubspec.yaml.

Colorful Interactive Shell: Uses Rich for readable help, previews, and error messages.

Easy To Extend: You can add new features with just a little code.

## Features

- **AI-Driven Generation**: Uses Google Gemini 2.0 to create complete Jaspr projects from simple prompts (e.g., "build a portfolio site").
- **Client-Side Only**: Generates pure client-side Jaspr apps (no server-side rendering).
- **Modular Structure**: Organizes projects into `lib/pages/`, `lib/components/`, `web/` for scalability.
- **Dependency Management**: Automatically includes required dependencies (Jaspr, Router, Tailwind) with latest versions.
- **Interactive Shell**: Rich-colored CLI with help, previews, and error handling.
- **Extensible**: Easy to add new features or modify prompts.

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

### Key Components
- **SYSTEM_PROMPT**: Detailed guide for AI to generate client-side Jaspr code.
- **File Schema**: `'files': [{'path': str, 'content': str}]` for full file generation.
- **Dependency Rules**: Minimal, latest versions, client-only.

## Troubleshooting

- **Import Errors**: Clear `__pycache__` and restart.
- **AI No Response**: Check API key, internet, or prompt length.
- **Generation Issues**: Ensure prompts are descriptive (e.g., "build a simple website").
- **Rich UI Not Working**: Install `rich` via pip.

## Contributing

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

## Future Enhancements

- Add more styling options (e.g., Material Design).
- Support for multi-page apps with SSR.
- Integration with CI/CD for auto-deployment.
- Custom themes and components library.

For questions or issues, open a GitHub issue.
