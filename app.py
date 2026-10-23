import http.server
import socketserver
import threading
import socket
import os
import json

import webview

socketserver.TCPServer.allow_reuse_address = True


def find_free_port(start_port=8080):
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return start_port


PORT = find_free_port(8080)


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        # список Spine-файлов в папке плеера (для автозагрузки проектов)
        if self.path.split('?')[0] == '/__list':
            exts = ('.json', '.skel', '.atlas', '.txt', '.png', '.jpg', '.jpeg', '.webp')
            out = []
            for root, dirs, files in os.walk('.'):
                dirs[:] = [d for d in dirs if d not in ('runtimes', 'legacy') and not d.startswith('.')]
                for f in files:
                    if f.lower().endswith(exts):
                        out.append(os.path.relpath(os.path.join(root, f), '.').replace(os.sep, '/'))
            body = json.dumps(sorted(out)).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        # без кеша, чтобы правки runtimes/index.html подхватывались сразу
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


def start_server():
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except Exception as e:
        print(f"Ошибка сервера: {e}")


if __name__ == '__main__':
    # Сервер раздаёт файлы из папки, где лежит скрипт (index.html + runtimes/)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    threading.Thread(target=start_server, daemon=True).start()

    webview.create_window(
        title='Spine Universal Viewer (3.7 / 3.8 / 4.0 / 4.1 / 4.2 / 4.3)',
        url=f'http://localhost:{PORT}/index.html',
        width=1280,
        height=860,
        resizable=True,
    )
    webview.start()
