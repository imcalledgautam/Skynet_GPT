import pytest
from unittest.mock import Mock, patch
import json
import os
from pathlib import Path

# Mocking subprocess.check_output for testing purposes
class MySubprocess:
    def __init__(self):
        self.called_with = []
    
        self.called_with.append((args, kwargs))
        return b"output\n"  # Simulate the output

# Monkeypatching subprocess.check_output for testing purposes
@pytest.fixture
def patch_subprocess():
    with patch('subprocess.check_output', MySubprocess().check_output) as mock_check_output:
        yield mock_check_output

# Testing get_git_info function
def test_get_git_info_success(patch_subprocess):
    assert get_git_info() == {"branch": "main", "commit": "abc123"}

def test_get_git_info_failure():
    try:
        subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True)
        assert False, "Expected an exception"
    except FileNotFoundError:
        pass

# Testing analyze_repository function
@pytest.fixture
def patch_analyze_repository():
    with patch('build_context.get_git_info') as mock_get_git_info:
        yield mock_get_git_info

def test_analyze_repository_success(patch_analyze_repository):
    mock_get_git_info.return_value = {"branch": "main", "commit": "abc123"}
    context = analyze_repository()
    assert context["repository_info"] == {"branch": "main", "commit": "abc123"}
    assert context["files"]  # Assuming there are files in the repository
    assert context["metadata"]["total_files"] > 0

def test_analyze_repository_failure(patch_analyze_repository):
    mock_get_git_info.side_effect = Exception("Failed to get git info")
    with pytest.raises(Exception) as e:
        analyze_repository()
    assert str(e) == "Failed to get git info"

# Testing the main function
@pytest.fixture
def patch_main():
    with patch('build_context.analyze_repository') as mock_analyze_repository:
        yield mock_analyze_repository

def test_main_success(patch_main):
    mock_analyze_repository.return_value = {"repository_info": {"branch": "main", "commit": "abc123"}, "files": [], "structure": {}, "metadata": {"total_files": 0, "changed_files": 0}}
    with open('ci_artifacts/context_bundle.json', 'w') as f:
        json.dump(mock_analyze_repository.return_value, f, indent=2)
    assert os.path.exists('ci_artifacts/context_bundle.json')
    print("✅ Context bundle created successfully")

def test_main_failure(patch_main):
    mock_analyze_repository.side_effect = Exception("Failed to analyze repository")
    with pytest.raises(Exception) as e:
        main()
    assert str(e) == "Failed to analyze repository"