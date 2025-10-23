import json
import os
import time
import google.generativeai as genai
from prompts import SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')

def process_prompt(prompt: str) -> dict:
    
    system_prompt = SYSTEM_PROMPT
    
    full_prompt = f"{system_prompt}\n\nPrompt: {prompt}"
    
    try:
        # Rate limiting: Sleep 2 seconds to avoid exceeding API limits (e.g., 60 RPM)
        time.sleep(2)
        response = model.generate_content(full_prompt)
        result_text = response.text.strip()
        # Extract JSON from the response (after planning text)
        import re
        json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            structure = json.loads(json_str)
            
            # Extract data for planning
            components = structure.get('components', [])
            routes = structure.get('routes', [])
            styling = structure.get('styling', 'minimal')
            layout = structure.get('layout', 'single-page')
            comp_names = [c['name'] for c in components] if components else []
            
            # Friendly planning output (4-5 lines)
            print("📋 Planning:")
            print(f"  • Layout: {layout} with {styling} styling")
            print(f"  • Components: {len(components)} ({', '.join(comp_names[:3])}...)" if len(comp_names) > 3 else f"  • Components: {', '.join(comp_names)}")
            print(f"  • Routes: {', '.join(routes)}")
            print("  • Generating files and integrating dependencies...")
            print("🎉 Ready to build!")
        else:
            raise ValueError("No JSON found in response")
        return structure
    except Exception as e:
        print(f"Error processing prompt with AI: {e}")
        # Fallback to dummy structure
        return {
            "components": [{"name": "HomePage", "type": "page", "content": "Welcome to the home page"}],
            "routes": ["/"],
            "dirs": ["lib"],
            "styling": "tailwind",
            "layout": "single-page"
        }

def suggest_command(project_context, user_query):
    
    prompt = SUGGESTION_PROMPT.replace('[PROJECT_CONTEXT]', project_context)
    full_prompt = f"{prompt}\n\nUser Query: {user_query}"
    
    try:
        time.sleep(2)
        response = model.generate_content(full_prompt)
        suggestion = response.text.strip()
        return suggestion
    except:
        return "exit"
