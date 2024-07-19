
# Make sure the project is in the Python path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))


# Import the main module
import semiprompt

# Run the app
semiprompt.app.run_in_window()
