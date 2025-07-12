"""
Test LiteLLM with Vertex AI integration
"""
import os
import sys
from pathlib import Path

# Add the TinyTroupeLiteLLM directory to sys.path
sys.path.append('/workspaces/TinyTroupeLiteLLM')

try:
    from tinytroupe import litellm_utils
    print("✅ Successfully imported litellm_utils")
except ImportError as e:
    print(f"❌ Failed to import litellm_utils: {str(e)}")
    sys.exit(1)

# Try to authenticate with Google Cloud
try:
    import google.auth
    try:
        credentials, project = google.auth.default()
        print(f"✅ Successfully authenticated with Google Cloud. Project ID: {project}")
    except Exception as e:
        print(f"❌ Failed to authenticate with Google Cloud: {str(e)}")
        print("Setting project ID to 'default-project' for testing purposes")
        project = "default-project"
except ImportError as e:
    print(f"❌ Failed to import google.auth: {str(e)}")
    sys.exit(1)

# Try to use litellm_utils to get a response from Vertex AI
try:
    print("\nTrying to get a response from Vertex AI using litellm_utils...")
    
    # Set project ID for Vertex AI
    os.environ["GOOGLE_CLOUD_PROJECT_ID"] = project
    
    # Try to get a response from Vertex AI
    response = litellm_utils.get_completion(
        provider="vertex_ai",
        model="gemini-1.5-flash",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        max_tokens=50
    )
    
    print("✅ Successfully got a response from Vertex AI:")
    print(response)
except Exception as e:
    print(f"❌ Failed to get a response from Vertex AI: {str(e)}")
    
    # Print more detailed error information
    import traceback
    print("\nDetailed error information:")
    traceback.print_exc()
