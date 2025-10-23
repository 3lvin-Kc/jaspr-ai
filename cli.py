import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Load environment variables from .env file
load_dotenv()

from ai import process_prompt
from generator import generate_jaspr_project
from previews.preview import preview_project

console = Console()

def main():
    # Welcome message with panel
    welcome_text = Text("Welcome to Jaspr CLI Interactive Shell!", style="bold blue")
    subtitle = Text("Type 'help' for commands or enter a prompt to build your Jaspr website.", style="italic cyan")
    panel = Panel.fit(f"{welcome_text}\n{subtitle}", title="🚀 Jaspr CLI", border_style="green")
    console.print(panel)
    
    while True:
        try:
            # Colored prompt
            console.print("\n[bold green]jaspr>[/bold green] ", end="")
            line = input().strip()
            if not line:
                continue
            
            if line == "exit":
                console.print("[bold red]Goodbye![/bold red]")
                break
            
            elif line == "help":
                help_text = """
[bold yellow]Jaspr CLI Interactive Shell[/bold yellow]
Commands:
  [cyan]<prompt>[/cyan]           - Generate Jaspr project from natural language prompt (e.g., 'build a portfolio site')
  [cyan]help[/cyan]               - Show this help
  [cyan]exit[/cyan]               - Exit the shell
                """
                console.print(help_text)
            
            else:
                #  build prompt
                prompt = line
                if line.startswith('build'):
                    prompt = line[6:].strip()
                    if not prompt:
                        console.print("[red]Usage: build <prompt>[/red]")
                        continue
                
                console.print(f"[bold magenta]Building Jaspr project for prompt:[/bold magenta] {prompt}")
                
                # prompt with AI
                structure = process_prompt(prompt)
                
                # Generate project
                project_name = prompt.replace(' ', '_').lower()[:20]  # Sanitize name
                generate_jaspr_project(structure, project_name=project_name)
                
                # Preview generated files
                project_path = f"./{project_name}"
                preview_project(project_path, structure)
                
                console.print(f"[bold green]Jaspr project '{project_name}' generated successfully![/bold green]")

        except KeyboardInterrupt:
            console.print("\n[bold red]Goodbye![/bold red]")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
