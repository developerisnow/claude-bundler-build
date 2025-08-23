---
allowed-tools: Task, TodoWrite, Read, Glob, LS
description: Execute task with aggressive parallelization using multiple sub-agents simultaneously
argument-hint: [task requiring parallel execution]
---

# ⚡ Parallel Execution Request

**Task**: $ARGUMENTS

## 🚀 PARALLEL-FIRST ORCHESTRATION

Use the **universal-orchestrator** agent with **AGGRESSIVE PARALLELIZATION**.

### 🎯 Execution Strategy: MAP/REDUCE

```
PARALLEL PHASE (Map):
├── Research Stream 1: Explore solution space
├── Research Stream 2: Find best practices  
├── Research Stream 3: Identify existing patterns
├── Analysis Stream: Deep dive into requirements
└── Prototype Stream: Rapid MVP creation

SYNTHESIS PHASE (Reduce):
└── Merge all findings → Unified solution
```

### ⚡ Parallelization Directives:

1. **IMMEDIATELY** spawn multiple agents for independent aspects
2. **NEVER** wait sequentially if tasks can run concurrently  
3. **AGGRESSIVELY** decompose into smallest parallelizable units
4. **PROACTIVELY** use research agents in parallel
5. **SIMULTANEOUSLY** explore multiple solution approaches

### 📊 Parallel Patterns to Apply:

#### Pattern 1: Scatter/Gather
- Scatter work across 3-5 specialized agents
- Each explores different dimension
- Gather and synthesize results

#### Pattern 2: Pipeline with Parallel Stages
- Stage 1: PARALLEL research (3+ agents)
- Stage 2: PARALLEL implementation (2+ agents)
- Stage 3: PARALLEL validation (2+ agents)

#### Pattern 3: Competitive Parallel
- Multiple agents solve same problem differently
- Compare and select best approach
- Merge beneficial aspects from each

### 🎭 Agent Coordination:
```yaml
Preferred Parallel Agents:
- adhd-research-discovery + solution-researcher + github-code-explorer
- rapid-prototyper + spec-planner (different approaches)
- code-analyst + synthesis-validator (validation)
- parallel-research-orchestrator (meta-parallelization)
```

### ✅ Success Metrics:
- [ ] Minimum 3 agents running concurrently
- [ ] No sequential waiting for independent tasks
- [ ] All exploration paths pursued simultaneously
- [ ] Results synthesized from multiple streams
- [ ] 2-5x faster than sequential execution

**CRITICAL**: Default to parallel execution. Only go sequential if explicitly required by dependencies. When in doubt, parallelize.