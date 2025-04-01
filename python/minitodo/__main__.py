import os

import uvicorn


def main() -> None:
    from .server import app

    MINITODO_SERVER_PORT = int(os.getenv("MINITODO_SERVER_PORT", "5003"))
    uvicorn.run(app, host="0.0.0.0", port=MINITODO_SERVER_PORT)


if __name__ == "__main__":
    main()
