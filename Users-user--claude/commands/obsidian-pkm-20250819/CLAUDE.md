# CLAUDE Agent Workflow Rules

## Article Backup
- Always save the full article content as a markdown file in the `_Outputs_External` folder.
- Use the filename format: `{YYYYMMDD}-{title}.md` (date = published or backup date).

## Atomic Summary Section
- At the top of the note, add a concise, ADHD-friendly summary section.
- Use emoji, numbers, lists, and a cheatsheet table for clarity.
- The summary heading must include a timestamp `{YYYYMMDD-hhmm}`.

## Obsidian Link
- At the end of the note, add an Obsidian-style link: `[[{title}]]`.

## Workflow Consistency
- Always follow this sequence: backup → summary → obsidian link.
- Never skip any step, even if the article is short.

## File Management
- If a file with the same name exists, append a new summary with a new timestamp at the top.
- Ensure no duplicate Obsidian links at the end of the file.

## Metadata
- If available, include metadata (source URL, author, tags) in the YAML frontmatter.


# Adhd Profile
```xml
<adhd_profile>
  <style>visual-first, learn-by-doing</style>
  <format>
    <must_have>emojis, tables, checklists</must_have>
    <visualize>mermaidjs for processes/connections</visualize>
    <structure>why→what→how→result</structure>
  </format>
  <cognitive>
    <compare>use analogies to known concepts</compare>
    <chunk>numbered steps (1,2,3)</chunk>
    <focus>practical value first</focus>
  </cognitive>
</adhd_profile>

## Communication Style
<adhd_optimized>
- Visual-first: tables > walls of text
- Always include: emojis 🎯, numbered steps, practical value
- Structure: Why matters → What it is → How to use → Expected result
- Comparisons: table format for A vs B
- Processes: mermaidjs diagrams
- Key points: ✅ checklists
</adhd_optimized>
The XML tags work because Claude was specifically trained on them. The ~10-15% improvement your friend mentioned is real - it's like using a language the model "thinks" in natively.

Keep the Russian version as your personal reference, but use these English versions in practice. The cognitive overhead of translation does impact response quality, especially for nuanced formatting instructions.
```

<adhd_task_protocol>
  ⚡ AUTOMATIC for 2+ step tasks
  📋 Start: TODO checklist  
  🔄 During: Update progress
  ✅ End: Completed summary
  
  Triggers: "track", "✅", "checklist", "todo"
</adhd_task_protocol>

## 📝 MARKDOWN FILE SAVING RULES
<markdown_output_rules>
  <mandatory_location>
    ALL markdown files MUST be saved to:
    /Users/user/____Sandruk/___PKM/__SecondBrain/Dailies_Outputs/
  </mandatory_location>
  
  <filename_format>
    <!-- ALWAYS use this exact format -->
    {yyyymmdd}-{HHMM}-{ActionType}-{category}-{title}.md
    
    Example: 20250626-1530-report-devops-tmux-setup.md
    Example: 20250626-0930-question-ai-claude-monitoring.md
    Example: 20250626-2100-todo-hypetrain-architecture.md
    Example: 20250626-1200-manual-zsh-configuration.md
  </filename_format>
  
  <action_types>
    question   - Q&A or exploratory discussions
    report     - Analysis, summaries, findings
    todo       - Task lists, action items
    manual     - How-to guides, documentation
    research   - Deep dives, investigations
    fix        - Problem solutions, troubleshooting
    plan       - Project plans, strategies
    log        - Activity logs, session notes
  </action_types>
  
  <categories>
    devops     - Infrastructure, CI/CD, automation
    ai         - Claude, LLMs, AI tools
    hypetrain  - HypeTrain project specific
    tmux       - Terminal multiplexer related
    zsh        - Shell configuration
    git        - Version control
    docker     - Containerization
    python     - Python development
    nodejs     - Node.js development
    general    - Other/misc topics
  </categories>
  
  <enforcement>
    ⚠️ NEVER save markdown files anywhere else
    ⚠️ ALWAYS follow the filename format exactly
    ⚠️ ALWAYS use lowercase for actiontype and category
    ⚠️ ALWAYS use hyphens (-) not underscores (_)
    ⚠️ ALWAYS zero-pad time (0930 not 930)
  </enforcement>
  
  <file_header>
    <!-- Start every markdown file with this metadata -->
    ---
    created: YYYY-MM-DD HH:MM
    type: {actiontype}
    category: {category}
    tags: [relevant, tags, here]
    ---
    
    # {Title}
  </file_header>
</markdown_output_rules>