<markdown_output_rules>
  ## 🚨 MANDATORY DOCUMENT HEADER - NO EXCEPTIONS

  **EVERY SINGLE MARKDOWN FILE MUST START WITH THIS EXACT FORMAT:**
  ```yaml
  ---
  version: "x.y.z"  # Semantic versioning: major.minor.patch
  last_edited: "YYYY-MM-DD HH:MM"
  created: "YYYY-MM-DD HH:MM" 
  status: "draft|review|final"
  type: "index|research|playbook|manual|report|todo|question|fix|plan|log"
  category: "relevant-category"
  tags: [tag1, tag2, tag3]
  prompt: "brief description of what user requested"
  ---
  ```

  ## 🔗 MANDATORY NAVIGATION (When part of series)

  **MUST include navigation block after title:**
  ```markdown
  **Previous:** [file.md](./prev) | **Next:** [file.md](./next)
  **Related:** [doc1.md](./doc1), [doc2.md](./doc2)

  ---
  ```

  ## 📋 MANDATORY REQUEST TRACKING

  **MUST include request checklist in every file:**
  ```markdown
  ## 📋 Request Checklist
  What you asked for:
  - [x] Item 1 from request
  - [ ] Item 2 from request  
  - [x] Item 3 (completed)

  ## 🎯 Your Original Request
  > {Brief 1-2 line summary of what user wanted}
  ```

  ## ⚠️ ENFORCEMENT RULES

  **CRITICAL FAILURES - THESE WILL CAUSE ERRORS:**
  1. ❌ Missing version header → FAIL
  2. ❌ Wrong datetime format → FAIL  
  3. ❌ No navigation in series → FAIL
  4. ❌ Missing request tracking → FAIL
  5. ❌ No type/category/tags → FAIL

  **AUTO-CHECK BEFORE WRITING:**
  ```
  BEFORE creating ANY .md file, verify:
  ✅ Version header complete?
  ✅ Navigation appropriate?  
  ✅ Request tracking included?
  ✅ Metadata complete?
  ✅ File follows naming convention?
  ```

  **Version increment rules:**
  - Major (x): Breaking changes, complete rewrites, new document series
  - Minor (y): New features, significant additions, major updates  
  - Patch (z): Bug fixes, small corrections, typos, formatting

  **When to include navigation:**
  - ✅ Part of document series (2+ related files)
  - ✅ Follow-up to previous work
  - ✅ References other documents
  - ❌ Single standalone documents (use "N/A" for Previous/Next)
</markdown_output_rules>