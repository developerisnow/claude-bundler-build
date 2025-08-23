#!/usr/bin/env python3
"""cleanup-safety-validator.py - Validates all cleanup commands for safety"""
import json
import sys
import re

# CRITICAL: Protected paths that should NEVER be deleted
PROTECTED_PATHS = [
    "/System",
    "/Library/Extensions", 
    "/usr/bin",
    "/usr/sbin",
    "/private/var/db",
    "/Applications/Utilities",
    "~/Documents",
    "~/Desktop",
    "~/Pictures",
    "~/Music",
    "~/Movies"
]

# Safe paths for cleanup
SAFE_CLEANUP_PATHS = [
    "~/Library/Caches",
    "~/Library/Logs",
    "~/.npm",
    "~/.yarn",
    "~/.cache",
    "/tmp",
    "/private/var/tmp"
]

# Dangerous command patterns
DANGEROUS_PATTERNS = [
    (r"\brm\s+-rf\s+/(?:\s|$)", "❌ BLOCKED: Attempting to delete root directory!"),
    (r"\brm\s+-rf\s+~(?:/|$|\s)", "❌ BLOCKED: Attempting to delete home directory!"),
    (r"\bsudo\s+rm\s+-rf", "⚠️ WARNING: sudo rm -rf detected - use with extreme caution!"),
    (r"\bdd\s+.*of=/dev/", "❌ BLOCKED: Direct disk write operation!"),
    (r"\b>\s*/dev/[sh]d", "❌ BLOCKED: Overwriting disk device!"),
]

def validate_cleanup_command(command):
    """Validate cleanup commands for safety"""
    
    # Check dangerous patterns
    for pattern, message in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            print(message, file=sys.stderr)
            if "BLOCKED" in message:
                sys.exit(2)  # Block execution
    
    # Check protected paths
    for path in PROTECTED_PATHS:
        if path in command and any(cmd in command for cmd in ["rm", "delete", "trash"]):
            print(f"❌ BLOCKED: Cannot delete from protected path: {path}", file=sys.stderr)
            sys.exit(2)
    
    # Suggest safer alternatives
    if "sudo" in command and any(safe in command for safe in SAFE_CLEANUP_PATHS):
        print("💡 INFO: sudo not needed for user cache directories", file=sys.stderr)
    
    # Warn about wildcards
    if re.search(r"rm.*-r.*\*", command):
        print("⚠️ WARNING: Recursive deletion with wildcards - double check the path!", file=sys.stderr)

# Main execution
try:
    hook_input = json.load(sys.stdin)
    
    if hook_input.get("tool_name") == "Bash":
        command = hook_input["tool_input"]["command"]
        validate_cleanup_command(command)
        
except Exception as e:
    print(f"Hook error: {e}", file=sys.stderr)
    sys.exit(1)

sys.exit(0)