# 🎯 AGENT OUTPUT ENHANCEMENT FOR VDD (Voice Driven Development)
<agent_output_rules>
  <core_principle>Every agent session MUST produce structured, actionable output with full observability</core_principle>
  
  <session_report_structure>
    <!-- MANDATORY sections for ALL agent outputs -->
    
    ## 📊 Session Metrics
    - Duration: X minutes
    - Completion: XX% (e.g., 85%)
    - Satisfaction: X/10 (self-evaluation)
    - Tokens Used: XXk
    - Sub-agents: X (count)
    
    ## 🗺️ Decision Log (MANDATORY)
    <!-- Visualize your reasoning path -->
    ```mermaid
    graph TD
        A[Start: Task] --> B{Decision Point?}
        B -->|Option 1| C[Path taken]
        B -->|Option 2| D[Alternative considered]
        B -->|Option 3| E[Rejected because...]
        C --> F{Next decision?}
    ```
    <!-- Show WHY you made each choice -->
    
    ## 📁 Files Modified
    <!-- One-line explanation for each -->
    - `path/to/file.js` - Added authentication middleware
    - `controllers/` folder - Created 3 new controllers
    - Examined `docs/` - Understood existing patterns
    
    ## 💻 Commands Executed
    ```bash
    # 1. Purpose of command (links to Decision X)
    command here
    
    # 2. Another command with clear explanation
    next command
    ```
    
    ## 🤖 Sub-agent Summaries
    <!-- If you used sub-agents -->
    1. **Agent Type** (duration, tokens)
       - What they analyzed/did
       - Key findings
    
    ## 🎓 Teach Me Section
    <!-- How to repeat this task independently -->
    Key insights not obvious from the output:
    1. This codebase uses X pattern
    2. Always check Y before Z
    3. Critical: Don't forget about...
    
    ## 👤 Roles & Thinking Hats
    - **Role Used**: When and why
    - **Architecture Hat**: Planning phase
    - **Developer Hat**: Implementation
    
    ## 🔮 Next Steps & Reflection
    **Task Completion**: XX%
    **What's Next**:
    1. Immediate next action
    2. Future considerations
    
    **Open Questions**:
    - Should we consider X?
    - What about Y scenario?
  </session_report_structure>
  
  <evaluation_rules>
    <!-- Use sub-agent for independent evaluation -->
    <independent_evaluation>
      After completing task, spawn evaluator sub-agent:
      - Give full context of completed work
      - Request unbiased quality assessment
      - Include in final report
    </independent_evaluation>
    
    <self_evaluation>
      Rate your work 1-10 on:
      - Code quality
      - Architecture decisions
      - Documentation completeness
      - Overall satisfaction
    </self_evaluation>
  </evaluation_rules>
  
  <file_tracking>
    <!-- Be specific about what you touched -->
    <granularity>
      - Individual files: exact path + purpose
      - Folders: what pattern you studied
      - Repositories: high-level understanding gained
    </granularity>
    
    <avoid>
      ❌ "Examined various files"
      ❌ "Made some changes"
      ✅ "Studied auth pattern in controllers/*.js"
      ✅ "Modified 3 files for JWT integration"
    </avoid>
  </file_tracking>
  
  <decision_documentation>
    <!-- CRITICAL: Show your thinking -->
    <requirements>
      1. Every major decision needs a node in the diagram
      2. Show alternatives considered
      3. Explain why you chose specific path
      4. Link decisions to outcomes
    </requirements>
    
    <example>
      "Chose PostgreSQL over MongoDB because:
      - Existing codebase uses SQL
      - Team expertise
      - Transaction requirements"
    </example>
  </decision_documentation>
  
  <next_steps_interview>
    <!-- Help clarify what comes next -->
    <format>
      Instead of guessing, ask:
      Q: "Should this service handle auth internally?"
      Q: "What load should I optimize for?"
      Q: "Any compliance requirements?"
    </format>
  </next_steps_interview>
</agent_output_rules>

# 📈 VDD Session Management
<vdd_session_rules>
  <parallel_processing>
    <!-- Address the 2-3 hour audio processing bottleneck -->
    When user gives long voice input:
    1. Acknowledge receipt immediately
    2. Break into parallel sub-tasks
    3. Show progress indicators
    4. Deliver incremental results
  </parallel_processing>
  
  <context_preservation>
    <!-- Link everything to project structure -->
    Every session MUST identify:
    - Project it belongs to
    - Epic/Story/Task hierarchy
    - Previous related sessions
    - TMux session name (if applicable)
  </context_preservation>
  
  <bottleneck_awareness>
    <!-- Key bottlenecks to always consider -->
    1. Audio processing time
    2. Mac dependency
    3. Context switching cost
    4. Decision paralysis
    Always suggest infrastructure solutions when relevant
  </bottleneck_awareness>
</vdd_session_rules>

# 🚀 LEAN TEMPLATE RULES
<lean_documentation>
  <core_principle>Minimal documentation that enables maximum action</core_principle>
  
  <template_hierarchy>
    <!-- Use these templates for ALL project documentation -->
    <project_level>
      Template: LEAN-project-canvas.md
      Size: ONE PAGE MAX
      Voice time: 1 minute
      Content: Problem, solution, target, success metric
    </project_level>
    
    <epic_level>
      Template: LEAN-epic-template.md  
      Size: HALF PAGE MAX
      Voice time: 30 seconds
      Content: 10-word goal, in/out scope, single metric
    </epic_level>
    
    <story_level>
      Template: LEAN-story-template.md
      Size: STRUCTURED BUT BRIEF
      Voice time: 30 seconds
      Content: User story, acceptance criteria, AI context
    </story_level>
    
    <task_level>
      Template: LEAN-task-template.md
      Size: 3-5 LINES
      Voice time: 10 seconds
      Content: Action, verification, timebox
    </task_level>
  </template_hierarchy>
  
  <documentation_rules>
    <!-- What NOT to do -->
    <never_create>
      ❌ Multi-page requirement documents
      ❌ Detailed technical specs upfront
      ❌ Separate docs for same concept
      ❌ Version-controlled documentation
      ❌ PVD/PRD/TDD document sets
    </never_create>
    
    <always_do>
      ✅ One file per level (project/epic/story/task)
      ✅ Update inline (no versioning)
      ✅ Visual indicators (emojis)
      ✅ Single success metric
      ✅ Time-boxed scope (2 weeks max)
    </always_do>
  </documentation_rules>
  
  <voice_driven_creation>
    <!-- When user gives voice input -->
    <workflow>
      1. Identify level from keywords
      2. Use appropriate LEAN template
      3. Fill ONLY provided information
      4. Don't ask for optional fields
      5. Create in under 2 minutes
    </workflow>
    
    <keywords>
      "New project" → Project canvas
      "Epic" → Epic template
      "Story" or "As a" → Story template
      "Task" or "Do" → Task template
    </keywords>
  </voice_driven_creation>
  
  <github_integration>
    <!-- Auto-create issues from templates -->
    <mapping>
      Epic → GitHub Epic with child issues
      Story → GitHub Issue with checklist
      Task → GitHub Issue or checklist item
    </mapping>
  </github_integration>
  
  <success_metrics>
    Documentation is successful when:
    - Created in < 2 minutes
    - Read in < 30 seconds
    - Leads to action within 2 hours
    - Never needs "approval"
  </success_metrics>
</lean_documentation>