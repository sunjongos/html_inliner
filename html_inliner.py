import os
import re
import sys
import base64
import urllib.request
import mimetypes
from bs4 import BeautifulSoup

# Configure UTF-8 encoding for stdout/stderr to prevent encoding crashes on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def fetch_resource(path_or_url, base_dir=None):
    """
    Fetch content of a resource either from local filesystem or remote URL.
    """
    if path_or_url.startswith(('http://', 'https://')):
        print(f"Downloading remote resource: {path_or_url}")
        try:
            req = urllib.request.Request(path_or_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                return response.read()
        except Exception as e:
            print(f"Error downloading {path_or_url}: {e}", file=sys.stderr)
            return None
    else:
        # Local file
        local_path = path_or_url
        if base_dir and not os.path.isabs(local_path):
            local_path = os.path.join(base_dir, local_path)
        
        # Strip query parameters or hashes if present in relative path (e.g. style.css?v=1.2)
        local_path = local_path.split('?')[0].split('#')[0]
        
        if os.path.exists(local_path):
            print(f"Reading local resource: {local_path}")
            try:
                with open(local_path, 'rb') as f:
                    return f.read()
            except Exception as e:
                print(f"Error reading {local_path}: {e}", file=sys.stderr)
                return None
        else:
            print(f"Warning: Local resource not found: {local_path}", file=sys.stderr)
            return None

def inline_html(html_path, output_path=None):
    if not os.path.exists(html_path):
        print(f"Error: HTML file '{html_path}' not found.", file=sys.stderr)
        return False
        
    base_dir = os.path.dirname(os.path.abspath(html_path))
    
    try:
        with open(html_path, 'rb') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading HTML file: {e}", file=sys.stderr)
        return False
        
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Inline CSS Stylesheets (<link rel="stylesheet">)
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if not href:
            continue
            
        css_bytes = fetch_resource(href, base_dir)
        if css_bytes:
            try:
                css_text = css_bytes.decode('utf-8')
            except UnicodeDecodeError:
                css_text = css_bytes.decode('cp949', errors='ignore')
                
            style_tag = soup.new_tag('style')
            style_tag.string = f"\n/* Inlined: {href} */\n{css_text}\n"
            link.replace_with(style_tag)
            
    # 2. Inline Javascript (<script src="...">)
    for script in soup.find_all('script', src=True):
        src = script.get('src')
        if not src:
            continue
            
        js_bytes = fetch_resource(src, base_dir)
        if js_bytes:
            try:
                js_text = js_bytes.decode('utf-8')
            except UnicodeDecodeError:
                js_text = js_bytes.decode('cp949', errors='ignore')
                
            new_script_tag = soup.new_tag('script')
            new_script_tag.string = f"\n/* Inlined: {src} */\n{js_text}\n"
            script.replace_with(new_script_tag)

    # 3. Inline Images (<img src="...">)
    for img in soup.find_all('img'):
        src = img.get('src')
        if not src or src.startswith('data:'):
            continue
            
        img_bytes = fetch_resource(src, base_dir)
        if img_bytes:
            mime_type, _ = mimetypes.guess_type(src)
            if not mime_type:
                if src.endswith('.svg'):
                    mime_type = 'image/svg+xml'
                elif src.endswith('.png'):
                    mime_type = 'image/png'
                else:
                    mime_type = 'image/jpeg'
                    
            base64_data = base64.b64encode(img_bytes).decode('utf-8')
            img['src'] = f"data:{mime_type};base64,{base64_data}"
            print(f"Inlined image to Base64: {src}")

    # 4. Inline CSS backgrounds inside style attributes
    for element in soup.find_all(style=True):
        style_attr = element.get('style')
        url_matches = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', style_attr)
        for url_path in url_matches:
            if url_path.startswith('data:'):
                continue
            img_bytes = fetch_resource(url_path, base_dir)
            if img_bytes:
                mime_type, _ = mimetypes.guess_type(url_path)
                if not mime_type:
                    mime_type = 'image/png'
                base64_data = base64.b64encode(img_bytes).decode('utf-8')
                embedded_url = f"data:{mime_type};base64,{base64_data}"
                # Safe replace URL path inside style attribute
                style_attr = style_attr.replace(url_path, embedded_url)
        element['style'] = style_attr

    # Save output
    if not output_path:
        filename, ext = os.path.splitext(html_path)
        output_path = f"{filename}_integrated{ext}"
        
    try:
        with open(output_path, 'wb') as f:
            f.write(soup.encode('utf-8'))
        print(f"\nSuccess! Self-contained HTML created at: {output_path}")
        return True
    except Exception as e:
        print(f"Error writing output file: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python html_inliner.py <path_to_html_file> [output_file_path]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    inline_html(input_file, output_file)
