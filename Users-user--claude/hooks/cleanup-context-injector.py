#!/usr/bin/env python3
"""cleanup-context-injector.py - Adds system info to cleanup prompts"""
import json
import sys
import subprocess
from datetime import datetime

def get_disk_usage():
    """Get current disk usage"""
    try:
        result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                parts = lines[1].split()
                if len(parts) >= 5:
                    return f"Disk: {parts[4]} used ({parts[3]} free)"
    except:
        pass
    return "Disk usage: Unknown"

def get_large_caches():
    """Find large cache directories"""
    cache_dirs = []
    paths_to_check = [
        "~/.npm",
        "~/.yarn", 
        "~/.cache",
        "~/Library/Caches",
        "~/.cargo/registry",
        "~/.gradle/caches"
    ]
    
    for path in paths_to_check:
        try:
            expanded = subprocess.run(["bash", "-c", f"echo {path}"], capture_output=True, text=True).stdout.strip()
            result = subprocess.run(["du", "-sh", expanded], capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                size, _ = result.stdout.strip().split('\t')
                cache_dirs.append(f"  • {path}: {size}")
        except:
            continue
    
    return "\n".join(cache_dirs) if cache_dirs else "  • No large caches found"

def inject_cleanup_context():
    """Inject system context for cleanup operations"""
    try:
        hook_input = json.load(sys.stdin)
        prompt = hook_input.get("prompt", "").lower()
        
        # Check if this is a cleanup-related prompt
        cleanup_keywords = ["clean", "cache", "disk", "space", "delete", "remove", "free"]
        if any(keyword in prompt for keyword in cleanup_keywords):
            
            context = f"""
=== 🧹 System Cleanup Context ===
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{get_disk_usage()}

📦 Large Cache Directories:
{get_large_caches()}

✅ Safe to clean:
  • ~/Library/Caches/* (app caches)
  • ~/.npm/_cacache (npm cache)
  • ~/.cache/* (general cache)
  • /tmp/* (temporary files)
  • brew cleanup (Homebrew cache)

⛔ Protected paths:
  • /System, /Library/Extensions
  • ~/Documents, ~/Desktop, ~/Pictures
  • /usr/bin, /usr/sbin

💡 Always use 'du -sh <path>' to check size before deletion
===
"""
            print(context)
            
    except Exception as e:
        # Silently fail - don't block the prompt
        pass

    sys.exit(0)

if __name__ == "__main__":
    inject_cleanup_context()