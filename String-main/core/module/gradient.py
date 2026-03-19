from rich.console import Console
from core.injector import injector_settings, injectro_gradient_color

string = Console()
one, two = injectro_gradient_color()

def log_message(action):

    username = injector_settings("username")

    text_to_gradient = f"_> String/@{username}"
    start_rgb = (one)
    end_rgb = (two)
    
    gradient_str = ""
    n = len(text_to_gradient)
    
    for i, char in enumerate(text_to_gradient):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / n)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / n)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / n)
        gradient_str += f"[rgb({r},{g},{b})]{char}[/]"

    string.print(f"{gradient_str} > {action}")

def api(action, api):

    text_to_gradient = f"_> StringAPI/{api}"
    start_rgb = (one)
    end_rgb = (two)
    
    gradient_str = ""
    n = len(text_to_gradient)
    
    for i, char in enumerate(text_to_gradient):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / n)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / n)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / n)
        gradient_str += f"[rgb({r},{g},{b})]{char}[/]"
        
    string.print(f"{gradient_str} > {action}")