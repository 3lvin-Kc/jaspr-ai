from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def preview_project(project_path: str, structure: dict):
    """
    Display a list of generated files.
    """
    project_dir = Path(project_path)
    files = structure.get('files', [])
    
    console.print("\n[bold green]Generated files:[/bold green]")
    
    for file_info in files:
        file_path = file_info['path']
        full_path = project_dir / file_path
        if full_path.exists():
            size = full_path.stat().st_size
            console.print(f"  • {file_path} ({size} bytes)")
        else:
            console.print(f"  • {file_path} (not found)")
