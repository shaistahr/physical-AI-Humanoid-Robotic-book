"""
Simple script to initialize the RAG chatbot with documentation content
"""
import requests
import json

# Backend API URL
API_BASE_URL = "http://localhost:8000/api"

def initialize_with_url(content_url):
    """
    Initialize the chatbot with content from a URL

    Args:
        content_url: The URL to scrape content from
    """
    print(f"Initializing chatbot with content from: {content_url}")

    try:
        # Call the initialization endpoint
        response = requests.post(
            f"{API_BASE_URL}/initialize",
            headers={"Content-Type": "application/json"},
            timeout=300  # 5 minutes timeout
        )

        if response.status_code == 200:
            result = response.json()
            job_id = result.get("job_id")
            print(f"✓ Initialization started! Job ID: {job_id}")
            print("This may take a few minutes...")

            # Check job status
            if job_id:
                status_response = requests.get(f"{API_BASE_URL}/initialize/{job_id}")
                if status_response.status_code == 200:
                    status = status_response.json()
                    print(f"Status: {status.get('status')}")
                    print(f"Progress: {status.get('progress', 0)}%")

                    if status.get('status') == 'failed':
                        print(f"✗ Error: {status.get('error')}")
                    elif status.get('status') == 'completed':
                        print("✓ Chatbot initialized successfully!")

            return True
        else:
            print(f"✗ Error: {response.status_code}")
            print(response.text)
            return False

    except Exception as e:
        print(f"✗ Error initializing chatbot: {e}")
        return False

def check_status():
    """Check if the chatbot is initialized"""
    try:
        response = requests.get(f"{API_BASE_URL}/status")
        if response.status_code == 200:
            status = response.json()
            print("\nCurrent Chatbot Status:")
            print(f"  Initialized: {status.get('initialized')}")
            print(f"  Content Source: {status.get('content_source', 'None')}")
            print(f"  Status: {status.get('status')}")
            print(f"  Last Updated: {status.get('last_updated')}")
            return status.get('initialized', False)
        return False
    except Exception as e:
        print(f"✗ Error checking status: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("RAG Chatbot Initialization Tool")
    print("=" * 60)

    # Check current status
    is_initialized = check_status()

    if is_initialized:
        print("\n✓ Chatbot is already initialized!")
        print("If you want to reinitialize, restart the backend server.")
    else:
        print("\n⚠ Chatbot is not initialized.")
        print("\nTo initialize the chatbot, you need to set CONTENT_URL in your .env file")
        print("Then run this script again.")
        print("\nExample .env configuration:")
        print("CONTENT_URL=https://example.com/your-documentation")

        # Quick test with example content
        print("\n" + "=" * 60)
        print("Quick Setup Option:")
        print("=" * 60)
        print("\nYou can manually initialize using curl:")
        print("\ncurl -X POST http://localhost:8000/api/initialize")
        print("\nMake sure CONTENT_URL is set in backend/.env file first!")
