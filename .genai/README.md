# GenAI Test Platform

Automated test generation using AI for your Skynet_GPT project.

## Usage

### Manually trigger workflow:
```bash
gh workflow run genai-testing.yml
```

### With specific files:
```bash  
gh workflow run genai-testing.yml -f files="src/pdf_utils.py,src/chat_utils.py"
```

### Auto-approve tests (for CI):
```bash
gh workflow run genai-testing.yml -f auto_approve=true
```

## Configuration

Edit `.genai/config.yml` to customize:
- Model selection (`qwen2.5-coder:1.5b`)
- File patterns to include/exclude
- Coverage thresholds

## Generated Tests

Tests are saved to `tests/generated/` and executed automatically.

## What Gets Tested

The AI will analyze your Python files and generate tests for:
- `src/pdf_utils.py` - PDF processing functions
- `src/chat_utils.py` - Chat interaction logic  
- `src/db_utils.py` - Database operations
- `src/app.py` - Main application logic
- `main.py` - Entry point functions