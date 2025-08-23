#!/usr/bin/env python3
"""cleanup-results-logger.py - Logs all cleanup operations and space freed"""
import json
import sys
import re
import os
from datetime import datetime
from pathlib import Path

def extract_freed_space(output):
    """Extract freed space from command output"""
    patterns = [
        r"freed?\s+.*?(\d+(?:\.\d+)?)\s*(MB|GB|KB|TB)",
        r"(\d+(?:\.\d+)?)\s*(MB|GB|KB|TB)\s+freed?",
        r"освобожден[оы]?\s+.*?(\d+(?:\.\d+)?)\s*(MB|GB|KB|TB)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, output, re.IGNORECASE)
        if match:
            size = float(match.group(1))
            unit = match.group(2).upper()
            # Convert to MB
            multipliers = {"KB": 0.001, "MB": 1, "GB": 1024, "TB": 1048576}
            return size * multipliers.get(unit, 1)
    return 0

def log_cleanup_operation():
    """Log cleanup operations with details"""
    try:
        hook_input = json.load(sys.stdin)
        
        if hook_input.get("tool_name") == "Bash":
            command = hook_input["tool_input"]["command"]
            response = hook_input.get("tool_response", {})
            stdout = response.get("stdout", "")
            
            # Check if this was a cleanup operation
            cleanup_commands = ["rm", "delete", "clean", "purge", "trash", "brew cleanup"]
            if any(cmd in command for cmd in cleanup_commands):
                
                # Extract what was cleaned
                target = "Unknown"
                if "rm -rf" in command:
                    match = re.search(r"rm -rf\s+([^\s&;|]+)", command)
                    if match:
                        target = match.group(1)
                elif "brew cleanup" in command:
                    target = "Homebrew cache"
                elif "npm cache clean" in command:
                    target = "npm cache"
                elif "yarn cache clean" in command:
                    target = "yarn cache"
                
                # Create log entry
                log_entry = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "command": command,
                    "target": target,
                    "exit_code": response.get("exit_code", -1),
                    "space_freed_mb": extract_freed_space(stdout),
                    "session_id": hook_input["session_id"],
                    "success": response.get("exit_code", -1) == 0
                }
                
                # Create logs directory
                log_dir = Path.home() / ".claude" / "logs"
                log_dir.mkdir(parents=True, exist_ok=True)
                
                # Append to log file
                log_file = log_dir / "cleanup-operations.jsonl"
                with open(log_file, "a") as f:
                    json.dump(log_entry, f)
                    f.write("\n")
                
                # Also create a human-readable log
                readable_log = log_dir / "cleanup-summary.txt"
                with open(readable_log, "a") as f:
                    f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
                    f.write(f"Target: {target}\n")
                    f.write(f"Command: {command[:80]}...\n" if len(command) > 80 else f"Command: {command}\n")
                    f.write(f"Space freed: {log_entry['space_freed_mb']:.1f} MB\n")
                    f.write(f"Status: {'✅ Success' if log_entry['success'] else '❌ Failed'}\n")
                    f.write("-" * 50 + "\n")
                    
    except Exception as e:
        # Don't block execution on logging errors
        pass
    
    sys.exit(0)

if __name__ == "__main__":
    log_cleanup_operation()