from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="RuleBasedUserType")

class RuleRequest(BaseModel):
    N_Yes: int

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

# Cleanup function
# Startup event


# Endpoints
@app.get("/health")
def health_check():
    """Endpoint for service health verification"""
    return {
        "status": "healthy",
    }


@app.post("/chat")
async def chat_completion(
    request: RuleRequest,
    background_tasks: BackgroundTasks
):
    """Main chat endpoint"""
    try:
      if(request.N_Yes<=2):
        return {
            "response": 'Conservative',
        }
      elif 2<request.N_Yes<=5:
        return {
            "response": 'Moderate',
        }
      else:
         return {
            "response": 'Aggresive',
        }
    except Exception as e:
        logger.error(f"Chat error: {str(e)}", exc_info=True)
        raise HTTPException(500, f"Chat completion failed: {str(e)}")