#!/usr/bin/env python3
"""cleanup-session-summary.py - Generates cleanup session summary"""
import json
import sys
from pathlib import Path
from datetime import datetime

def generate_session_summary():
    """Generate a summary of the cleanup session"""
    try:
        hook_input = json.load(sys.stdin)
        session_id = hook_input.get("session_id", "unknown")
        
        # Read session logs
        log_file = Path.home() / ".claude" / "logs" / "cleanup-operations.jsonl"
        
        if not log_file.exists():
            return
            
        # Analyze this session's operations
        total_space_freed = 0
        operations_count = 0
        failed_operations = 0
        targets_cleaned = []
        
        with open(log_file, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    if entry.get("session_id") == session_id:
                        operations_count += 1
                        total_space_freed += entry.get("space_freed_mb", 0)
                        if not entry.get("success", True):
                            failed_operations += 1
                        target = entry.get("target", "")
                        if target and target != "Unknown":
                            targets_cleaned.append(target)
                except:
                    continue
        
        # If we did any cleanup operations, show summary
        if operations_count > 0:
            summary = f"""

════════════════════════════════════════════════════════════════
                    🧹 CLEANUP SESSION SUMMARY
════════════════════════════════════════════════════════════════
📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📊 Operations: {operations_count} ({failed_operations} failed)
💾 Total Space Freed: {total_space_freed:.1f} MB ({total_space_freed/1024:.2f} GB)

🎯 Cleaned:
{chr(10).join(f'  ✓ {t}' for t in set(targets_cleaned)[:10])}

📁 Log saved to: ~/.claude/logs/cleanup-summary.txt
════════════════════════════════════════════════════════════════
"""
            print(summary, file=sys.stderr)
            
            # Save summary to file
            summary_file = Path.home() / ".claude" / "logs" / f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}-summary.txt"
            with open(summary_file, "w") as f:
                f.write(summary)
                
    except Exception as e:
        # Don't block on errors
        pass
    
    sys.exit(0)

if __name__ == "__main__":
    generate_session_summary()