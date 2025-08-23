## File Management Principles

### CORE PRINCIPLE: Understand Before Acting
**When you see file references or imports - ALWAYS trace them to understand the system architecture**

Example of failure:
- Saw `.zshrc` loads files from `$ZSH_CONFIG/env/paths.zsh`
- Instead of exploring what `$ZSH_CONFIG` contains and how it's organized
- Created duplicate PATH settings in `.zshenv`
- Result: Conflicting configurations and confusion

### The Right Approach:
1. **See a reference? Follow it.** 
   - `.zshrc` loads from `~/automations/zsh/`? → Explore that ENTIRE structure
   - Understand naming conventions (env/, aliases/, scripts/, functions/)
   - Read existing files to understand their purpose

2. **Detect patterns before adding**
   - If you see `env/paths.zsh` - that's where ALL path configs should go
   - If you see `aliases/tool-*.zsh` - that's the pattern for tool aliases
   - Don't create `.zshenv` changes when `env/` directory exists

3. **Think like an architect, not a patcher**
   - Ask: "Where would a senior dev put this?"
   - Look for existing similar functionality
   - Respect the established organization

4. **When in doubt - READ MORE, not CREATE MORE**
   - See how similar problems were solved
   - Check if your "new" file already exists under different name
   - Understand WHY files are organized this way

### Red flags to avoid:
- ❌ "I'll just add this quickly to .zshrc/.zshenv"
- ❌ "I'll create a new file for this one line"
- ❌ "The existing structure seems complex, I'll make my own"
- ✅ "Let me understand how this project organizes configs first"