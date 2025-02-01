from flask import Flask, request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    """Endpoint for service health verification"""
    return jsonify({"status": "healthy"})

@app.route("/chat", methods=["POST"])
def chat_completion():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        N_Yes = data.get("N_Yes")
        
        if N_Yes is None or not isinstance(N_Yes, int):
            return jsonify({"detail": "Invalid input, N_Yes must be an integer"}), 400
        
        if N_Yes <= 2:
            response = "Conservative"
        elif 2 < N_Yes <= 5:
            response = "Moderate"
        else:
            response = "Aggressive"
        
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Chat error: {str(e)}", exc_info=True)
        return jsonify({"detail": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
