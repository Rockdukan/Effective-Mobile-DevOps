from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "0.0.0.0"
PORT = 8080


class Handler(BaseHTTPRequestHandler):
    """HTTP-обработчик для тестового backend-сервиса."""

    def do_GET(self) -> None:
        """
        Обрабатывает GET-запросы.

        Returns:
            None: Ответ отправляется в сокет клиента.
        """

        if self.path == "/":
            body = b"Hello from Effective Mobile!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/health":
            body = b"OK"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Not Found")

    def log_message(self, format: str, *args) -> None:
        """Отключает стандартное логирование запросов."""
        return


def main() -> None:
    """Запускает HTTP-сервер на порту 8080."""
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Listening on http://{HOST}:{PORT}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()

