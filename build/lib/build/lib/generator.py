import os

def get_project_context(project_path):
    context = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(('.dart', '.yaml')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        context.append(f"File: {path}\nContent:\n{content}\n")
                except:
                    pass
    return "\n".join(context)

def generate_jaspr_project(structure, project_name="jaspr_app"):
    """
    Generate a Jaspr project based on the structure dict.
    """
    project_path = os.path.join(".", project_name)
    os.makedirs(project_path, exist_ok=True)
    
    # Write all files from structure
    for file_info in structure.get('files', []):
        path = file_info['path']
        # Skip directories or invalid paths (must have extension and not end with /)
        if path.endswith('/') or '.' not in path:
            continue
        file_path = os.path.join(project_path, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_info['content'])
    
    print(f"Jaspr project generated at {project_path}")
