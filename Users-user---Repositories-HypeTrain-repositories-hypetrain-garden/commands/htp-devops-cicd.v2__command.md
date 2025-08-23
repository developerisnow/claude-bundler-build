---
allowed-tools: Task, TodoWrite, Read, Glob, LS
description: Orchestrate complex tasks using multiple specialized sub-agents intelligently
argument-hint: [task description or requirements]
---
# Context Hypetrain Devops
Think harder.
Be aware of best practices to use sub-agents task tool @ai_docs/anthropic-publisher/sub-agents__anthropic.md.
Orchestrate tasks smart. Use sub-agents to orchestrate multiple task in parallel (prefer if possible) or sequence to accomplish my goals.
If task has a big output, run and monitor process or something like that you could run it with sub-agent.
Imporant to think more to provide all necessary context and output expected @ai_docs/20250729-1400-anthropic-agent-system-analysis.md

## About Project
@docs/dev/00-intro/intro-project-docs.md

## About infrastructure
- Backend:
  - @docs/dev/01-architecture/key-facts.md
  - @docs/dev/01-architecture/overview.md
  - @docs/dev/01-architecture/diagrams.md

## Working files
- @.github/workflows/garden-debug.yml

## Infrastructure

### Parts of infra

### Knowning issues and common mistakes

## Available tools
You have logged in CLIs tools: gh, gcloud, kubectl.

# 🎯 Task Orchestration Request

## Objectives
**Objective**: $ARGUMENTS

## 📋 Orchestration Requirements

Use the **htp-devops-universal-orchestrator** agent to coordinate this complex task.

### Key Directives:
1. **Decompose** the task into parallelizable components
2. **Identify** specialized agents for each component
3. **Execute** with maximum parallelization where quality permits
4. **Synthesize** results into cohesive output
5. **Document** key insights in memory bank

### Orchestration Priorities:
- ⚡ **Speed**: Parallelize independent operations
- 🎯 **Quality**: Use domain-expert agents
- 🧠 **Context**: Preserve main thread for oversight
- 📊 **Completeness**: Address all aspects systematically

### Expected Approach:
1. Analyze task complexity and domains
2. Map to available specialized agents
3. Create execution plan (parallel vs sequential)
4. Execute with progress tracking
5. Validate and synthesize results

### Success Criteria:
- [ ] All sub-tasks identified and assigned
- [ ] Parallel execution where appropriate
- [ ] Results properly synthesized
- [ ] Knowledge preserved for future use
- [ ] Clear, actionable output delivered

**Remember**: Think like a conductor orchestrating an AI symphony. Each agent is a virtuoso - coordinate them to create something greater than the sum of their parts.