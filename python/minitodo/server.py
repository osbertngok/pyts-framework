from fastapi import FastAPI

from .routes.todos import router as todos_router

app = FastAPI(title="MiniTodo API", description="A simple Todo API")


@app.get("/api/v1/")
async def root() -> dict[str, str]:
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to MiniTodo API"}


# Include the todos router
app.include_router(todos_router)
