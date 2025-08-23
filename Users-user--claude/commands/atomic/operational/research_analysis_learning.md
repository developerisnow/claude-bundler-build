# 🔍 Research Analysis Patterns (NEW from Discord backup project)
<research_analysis_learnings>
  <core_principle>What user SAID > What research ASSUMES</core_principle>
  
  <requirement_extraction>
    <!-- Always re-read original requirements after research -->
    <pattern>
      1. Read original user prompts FIRST
      2. Note explicit statements ("похер" = they don't care)
      3. Identify implicit needs from context
      4. IGNORE features user didn't ask for
    </pattern>
    
    <red_flags>
      ❌ "User should want..." → Wrong, they said what they want
      ❌ "Best practices suggest..." → Unless user asked
      ❌ "Enterprise features..." → Check if user is enterprise
      ❌ "For future scalability..." → YAGNI until proven
    </red_flags>
  </requirement_extraction>
  
  <tool_selection_reality>
    <!-- Learned from analyzing 30+ Discord backup tools -->
    <criteria>
      1. **Maturity > Innovation** (15k stars > 50 stars)
      2. **Working > Perfect** (ship today not tomorrow)
      3. **Simple > Complex** (unless complexity needed)
      4. **Boring > Exciting** (boring often just works)
    </criteria>
    
    <decision_framework>
      IF setup_time > 2_hours AND user_said("похер") → SKIP
      IF requires_perfect_architecture AND user_is_pragmatic → SKIP
      IF solution_works_in_30_min → STRONG_CANDIDATE
    </decision_framework>
  </tool_selection_reality>
  
  <mcp_reality_check>
    <!-- MCP isn't always the answer -->
    <when_to_use>
      ✅ Need real-time access from Claude
      ✅ Complex ongoing automation
      ✅ User explicitly wants MCP
    </when_to_use>
    
    <when_to_skip>
      ❌ Simple CLI works fine
      ❌ Batch operations sufficient
      ❌ User wants quick solution
      → Start with CLI, add MCP later if needed
    </when_to_skip>
  </mcp_reality_check>
  
  <synthesis_patterns>
    <!-- How to handle multiple research reports -->
    <approach>
      1. More reports ≠ Better decision
      2. Look for consensus on mature tools
      3. Trust user's "I'm a programmer" statements
      4. First good solution often sufficient
    </approach>
    
    <anti_patterns>
      ❌ Analysis paralysis from too many options
      ❌ Feature comparison tables for features nobody needs
      ❌ Assuming user needs "proper" architecture
      ❌ Ignoring explicit "don't care" signals
    </anti_patterns>
  </synthesis_patterns>
</research_analysis_learnings>